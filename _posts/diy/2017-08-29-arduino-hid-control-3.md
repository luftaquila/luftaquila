---
title: 아두이노로 마우스 & 키보드 입력 제어 (3)
description: 조이스틱 제작 단계
category: diy
assets: /assets/posts/diy/2017-08-29-arduino-hid-control-3
image: /assets/posts/diy/2017-08-29-arduino-hid-control-3/main.jpg
layout: post
---

##### 목차
[(1) HID 장치가 뭐길래](https://luftaquila.io/blog/diy/arduino-hid-control-1/){:class="link"}  
[(2) HoodLoader2](https://luftaquila.io/blog/diy/arduino-hid-control-2/){:class="link"}  
[(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}

#### 환승입니다
드디어 준비 단계가 다 끝나고 진짜로 조이스틱을 만들 차례다. 앞선 과정을 따라오면서 HoodLoader2를 업로드했다면, 그 보드에 있는 MCU 두 개, 즉 USB MCU와 I/O MCU는 모두 프로그래밍이 가능하다. 아두이노와 컴퓨터를 연결하면 기본적으로 인식되는 MCU는 USB MCU인 16u2이다. 이걸 I/O MCU인 328P로 인식되게 하려면,

<div class='center'><img src='{{ page.assets }}/1.png'></div>
사진의 두 핀을 빠르게 두 번 합선시켜 주면 된다.

<div class='center'><img src='{{ page.assets }}/2.png'></div>
한 번만 합선시키면 16u2로 인식되고, 두 번 빠르게 합선시키면 328P로 인식한다. 이렇게 두 MCU 사이를 갈아타면서 모든 MCU에 원하는 코드를 업로드하면 된다. 택트 스위치를 이용하면 편리하다.

<div class='center'>
  <img src='{{ page.assets }}/3.png' style='width: 45%'>
  <img src='{{ page.assets }}/4.png' style='width: 45%'>
</div>
왼쪽이 스위치를 한 번 눌러 USB MCU로 인식시켰을 때, 오른쪽이 두 번 눌러서 I/O MCU로 인식시켰을 때의 보드 설정이다.

#### 라이브러리 설치
그럼 다시 본래의 목적을 찾아 HID 라이브러리를 설치해야 한다. [HID](https://github.com/NicoHood/HID){:target="_blank"}{:class="external"}에서 저장소를 클론받아 라이브러리를 설치한다. 이제 모든 준비가 끝났다. 

#### 조이스틱 만들기
I/O MCU는 조이스틱 모듈로부터 입력을 받아 USB MCU에 시리얼 통신으로 전송하는 내용이다. 여기에는 두 가지 선택지가 있다. 조이스틱 입력을 컴퓨터에 키보드 키 입력으로 전달할 수도, 마우스 조작으로 전달할 수도 있다. 마우스로 입력할 때는 조이스틱 핀이 잘 연결되어 있는지 주의해야 한다. 제대로 연결되지 않아 노이즈가 낄 경우 마우스가 혼자 폭주하기 시작한다. 제멋대로 커서를 옮기고 클릭해서 아두이노 보드에 수정할 코드를 업로드할 수 없게 만들어 버린다.

조이스틱 모듈에는 조이스틱을 아래로 누르면 눌리는 택트 스위치 입력이 하나 더 있다. 이 버튼을 키보드/마우스 조작을 전환하는 스위치로 이용한다. 코드는 다음과 같다.

```cpp
const int xAxis = A0;         // 조이스틱 모듈 X축 입력 핀
const int yAxis = A1;         // 조이스틱 모듈 Y축 입력 핀

boolean Mode = true;          // 키보드/마우스 전환 모드
int range = 12;               // X축, Y축 동작 범위
int responseDelay = 5;        // 응답 딜레이 5ms 지정
int threshold = range / 4;    // 리셋 위치 지정
int center = range / 2;       // 중심 위치 지정
 
void setup() {
  Serial.begin(115200);
  pinMode(2, INPUT_PULLUP);
  pinMode(13, OUTPUT);
}
 
void loop() {
  // 조이스틱 모듈에서 X, Y축 아날로그 값 읽기
  int xReading = readAxis(A0);
  int yReading = readAxis(A1);
 
  /*
  시리얼 통신을 이용해 읽어온 데이터를 USB MCU로 전송한다.
  X, Y축 데이터를 순서 없이 보내면 이 데이터가 어느 축의 데이터인지 구분할 수가 없다.
  따라서 조금의 문자열 조작이 필요하다.
  */
 
  String xySeparator = ","; // X축과 Y축 데이터를 구분할 분리 문자
  String modeSeparator = "@"; // 축 데이터와 모드 데이터를 구분할 분리 문자
  String packetSeparator = "|"; // 한 패킷을 구분할 분리 문자
 
  /*
  X축 값 + 축 구분 문자 + Y축 값 + 데이터 구분 문자 + 모드 데이터 + 세트 구분 문자를 한 패킷으로 만든다.
  예를 들어 X, Y축 값이 각각 3, 5이고 2번 핀이 HIGH라면 패킷은 3,5@HIGH| 가 된다.
  연속적으로 보내면 2,4@HIGH|1,3@HIGH|4,5@HIGH|2,6@LOW| 와 같이 전송될 것이다.
  */
  String Data = xReading + xySeparator + yReading + modeSeparator + digitalRead(2) + packetSeparator;
 
  char Packet[20]; // 패킷을 담을 문자열 배열을 선언한다.
  Data.toCharArray(Packet, 20); // 패킷을 문자열 배열에 담아서
  Serial.write(Packet); // 시리얼 통신으로 쏘아 준다.
  
  // 빌트인 LED로 현재 모드를 표시한다.
  if(Mode) digitalWrite(13, HIGH);
  else digitalWrite(13, LOW);
  
  delay(responseDelay); // 약간의 딜레이를 준다.
}
 
// 조이스틱 모듈에서 아날로그 값을 읽는 함수
int readAxis(int thisAxis) {
  int reading = analogRead(thisAxis);
  reading = map(reading, 0, 1023, 0, range);
  int distance = reading - center;
  if (abs(distance) < threshold) distance = 0;
  return distance;
}
```

<br>
USB MCU는 시리얼 통신으로 받은 값을 파싱한 후, 컴퓨터에 입력으로 전달한다. 코드는 다음과 같다.
```cpp
#include <Keyboard.h>
#include <Mouse.h>
#include <HID.h>
 
boolean Mode = true;
 
int xValue;
int yValue;
int lastButtonReceive = 1;
unsigned long int time1 = 0;
 
void setup() {
  Serial1.begin(115200);
  Keyboard.begin();
  Mouse.begin();
}

void loop() {
  String receive = Serial1.readStringUntil('|');
  Serial.println(receive);
 
  int xySeparator = receive.indexOf(',');
  int modeSeparator = receive.indexOf('@');
 
  int buttonReceive = receive.substring(modeSeparator + 1).toInt();
  receive.remove(modeSeparator);
   
  yValue = receive.substring(xySeparator + 1).toInt()
  receive.remove(xySeparator);
  xValue = receive.toInt();
 
  if(!lastButtonReceive && lastButtonReceive != buttonReceive) time1 = millis(); // push
     
  if(lastButtonReceive && lastButtonReceive != buttonReceive) { // release
    if(millis() - time1 > 1000) Mode = !Mode;
    else Keyboard.write(KEY_RETURN);
  }
  
  lastButtonReceive = buttonReceive;
 
  if(Mode) Mouse.move(xValue, yValue, 0);
  else {     
    if(xValue > 0)  Keyboard.write(KEY_RIGHT_ARROW);
    if(xValue < 0)  Keyboard.write(KEY_LEFT_ARROW);
    if(yValue < 0)  Keyboard.write(KEY_UP_ARROW);
    if(yValue > 0)  Keyboard.write(KEY_DOWN_ARROW);
  }
}
```
<div class='center'><img src='{{ page.assets }}/5.png'></div>
야크 털이 너무 많이 쌓여 앞이 보이지 않는다. 하드웨어도 만들어 주어야 한다. 조이스틱이 너무 짧아 조작하는 맛이 안 나서 고장난 분광기 경통을 위에 끼웠다. 그랬더니 이번에는 경통이 너무 무거워 지지가 되지 않아서 고장난 기포발생기를 받침으로 썼다. 삽질은 성공적이다. 만든 조이스틱으로 비행하는 영상으로 글을 마무리한다.

<div class='center'>
  <video controls>
    <source src="{{ page.assets }}/video.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
  </video>
</div>

나중에 외주 작업을 받아 이 때 작업한 내용을 이용해 컨트롤러도 만들었다. 케이스를 모델링하고 3D 프린터로 뽑아 작업한 조이스틱이다.
<div class='center'><img src='{{ page.assets }}/6.png'></div>
<div class='center'><img src='{{ page.assets }}/main.jpg'></div>

##### 목차
[(1) HID 장치가 뭐길래](https://luftaquila.io/blog/diy/arduino-hid-control-1/){:class="link"}  
[(2) HoodLoader2](https://luftaquila.io/blog/diy/arduino-hid-control-2/){:class="link"}  
[(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}