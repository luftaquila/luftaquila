---
title: 멀쩡한 선풍기 IoT 선풍기로 만들기
description: 아두이노로 만드는 사물인터넷
category: diy
assets: /assets/posts/diy/2017-09-18-arduino-turn-fan-into-iot
image: /assets/posts/diy/2017-09-18-arduino-turn-fan-into-iot/main.png
layout: post
---

모든 과학기술과 공학의 원천이 귀찮음에서 비롯된 것은 명백하다. 책상에 앉아 불과 2m 떨어진 선풍기를 켜기 위해 일어나는 것이 귀찮아서 선풍기를 핸드폰으로 제어할 수 있도록 만들기로 했다. 작동 영상을 먼저 준비했다.

<div class='center'>
  <video controls>
    <source src="{{ page.assets }}/video.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
  </video>
</div>

DIY에서 중요한 것은 내가 만든 걸 어떻게 하면 최대한 안 보이게 하느냐이다. 내가 만든 <del>조잡한</del> 회로가 안 보일수록 더 완성도있어 보인다. 추가로 붙인 회로를 전부 선풍기 안에 집어넣어 외관상 매우 깔끔해 보인다.

#### 준비물
준비물이 아주 간단하다.  
아두이노 보드(나노) 1개  
HC-06 블루투스 통신 모듈 1개  
NPN 트랜지스터(2N3904) 3개  
전원공급장치 아무거나 1개

선풍기는 AC 220V로 전원을 공급받지만 이걸 아두이노에게 넘겨줬다간 숯불구이가 될 게 불보듯 뻔하므로 5V DC로 바꿔줄 방법이 필요하다. GMS0205와 같은 AC-DC 컨버터를 이용해도 무방하지만 제일 간단한 건 주위에 널린 스마트폰 충전기 하나 분해해서 회로만 빼다 넣는 거다. 아두이노가 워낙 저전력이라 다이소에서 파는 제일 싸구려 충전기로도 거뜬하다.

#### 메스!
일단 선풍기를 분해해 보자.
<div class='center'><img src='{{page.assets}}/1.png'></div>
요즘 나오는 선풍기는 전부 전자식이다. 사실 고전적인 푸쉬스위치형 선풍기가 발로 눌러 끄기도 좋고 더 편리하다고 생각한다. 더 최근에 나온 선풍기들은 그나마 전원 버튼이라도 따로 달려있는데, 이 선풍기는 과도기에 나와서 그런지 전원버튼조차 없다. 버튼을 누르면 미풍-약풍-강풍-꺼짐 순으로 순회한다. 미풍 쐬다가 끄고 싶으면 버튼을 무려 세 번이나 눌러야 한다는 얘기다. 세상에 이렇게 귀찮을 수가 없다.

<div class='center'><img src='{{page.assets}}/2.png'></div>
선풍기 회로는 이렇게 생겼다. 이걸 뜯어고쳐서 무선제어가 가능하게 만드는 건 불가능에 가깝다. MCU가 뭔지도 모르겠거니와 프로그래밍하려면 온갖 야크를 데려다가 털을 깎아야 할 것이 뻔하기 때문이다. 하드웨어 해킹을 통해 옆에 기생하는 아두이노가 버튼을 '누르게' 만들면 된다.

하지만 아두이노가 스위치를 '물리적' 으로 누르게 만드는 건 여러모로 귀찮다. 기계적으로 누르려면 서보 모터가 필요하고 모터를 돌리려면 모터 드라이버가 있어야 하고 또... 그만 생각하자.  

스위치라는 건 접점 두 곳을 합선시켜주는 부품이다. 아두이노가 '전자적'으로 접점을 합선시켜 스위치를 '누르게' 만들면 된다. 우리는 이러한 기능을 하는 훌륭한 부품을 두 개 정도 알고 있다. 하나는 릴레이이고 다른 하나는 트랜지스터이다. 릴레이는 부피도 크고 비싸다. 같은 동작을 50원짜리 트랜지스터로도 할 수 있다. 바로 고등학교 1학년 때 배우는 트랜지스터의 스위칭이다.

<div class='center'><img src='{{page.assets}}/4.png'></div>
트랜지스터로 다양한 동작을 할 수 있지만, 기본적으로 NPN 트랜지스터는 MCU에 쓰기 좋은 스위치이다. 가운데 단자인 베이스에 전압을 걸어 HIGH 상태로 만들면 컬렉터와 이미터가 도통된다. 선풍기 회로의 스위치 접점 양 쪽에 이미터랑 컬렉터를 하나씩 연결하고, 아두이노의 디지털 핀 하나를 베이스에 연결하면 스위치 완성이다. 디지털 핀에 HIGH 출력을 잠깐 줬다 끄면 스위치가 '전자적'으로 '눌린'다. 대신, 이미터와 아두이노의 GND를 연결해 주어야 한다.

여기에 이러쿵저러쿵 해서 HC-06으로 블루투스가 되게 만들고 코딩만 하면 된다. ESP8266을 알았다면 Wi-Fi와 Blynk를 이용해서 더 접근성 좋게 만들었겠지만, 아쉽게도 이걸 만들 때는 ESP8266 계열을 몰랐었다.

<div class='center'><img src='{{page.assets}}/5.png'></div>
선풍기에 스위치가 세 개 달려있으므로 트랜지스터 세 개를 준비해 각각 아두이노와 연결하다. 배선하기 쉽도록 PCB를 작게 톱질해서 가져다 썼다.

<div class='center'><img src='{{page.assets}}/3.png'></div>
그리고 이 회로를 선풍기 회로에 가져다가 스위치 접점에 연결해준다. 선풍기 기판 위쪽에 보이는 건 분해한 충전기 회로이다. 선풍기에 들어가는 220V를 끌어다가 충전기 회로에 연결하고, 출력 부분을 아두이노에 공급해주면 된다.

#### 코딩
<div class='center'><img src='{{page.assets}}/main.png'></div>
다음은 신나는 코딩이다. 어째서 한방에 모든 기능이 완벽하게 작동하는 코드를 짤 수는 없는 걸까.

```cpp
#include <SoftwareSerial.h>
SoftwareSerial BT(6, 7); //블루투스 TX, RX
 
boolean ROT = false;
boolean POWER = false;
int mode = 0;
int timer = 0;
 
String cmd = "";

void setup() {
  BT.begin(9600);
  pinMode(2, OUTPUT); // 회전 버튼
  pinMode(3, OUTPUT); // 전원/모드 버튼
  pinMode(4, OUTPUT); // 타이머 버튼
}
 
void loop() {
  // 블루투스 통신 수신
  while(BT.available()) {
    char RCV = (char)BT.read();
    cmd += RCV;
    delay(5);
  }
  
  // 수신 내용이 있다면
  if(!cmd.equals("")) {
    // 각종 스위치 동작
    if(cmd == "power" && !POWER) {
      pressButton(3, 1);
      POWER = true;
      mode = 1;
    }
    else if(cmd == "power" && POWER) Power_Off();
       
    if(cmd == "slow" && POWER) setWind(1);
    if(cmd == "mid" && POWER) setWind(2);
    if(cmd == "fast" && POWER) setWind(3);
    
    if(cmd == "rot" && POWER) {
        pressButton(2, 1);
        ROT = !ROT;
    }
 
    if(cmd == "timerReset" && POWER) Timer_Reset();
    if(cmd == "1h" && POWER) setTimer(1);
    if(cmd == "2h" && POWER) setTimer(2);
    if(cmd == "4h" && POWER) setTimer(4);
  }
  
  cmd = "";
  delay(50);
}
 
// 스위치를 눌러주는 함수.
void pressButton(int buttonNum, int pressTime) {
  for(int i = 1; i <= pressTime; i++) {
    digitalWrite(buttonNum, HIGH);
    delay(100);
    digitalWrite(buttonNum, LOW);
    delay(100);
  }
}

// 선풍기를 끄는 함수
void Power_Off() {
  if(mode == 1) pressButton(3, 4);
  else if(mode == 2) pressButton(3, 3);
  else if(mode == 3) pressButton(3, 2);

  POWER = false;
  mode = 0;
}

// 타이머 끄는 함수
void Timer_Reset() {
  if(timer == 1) pressButton(4, 7);
  else if(timer == 2) pressButton(4, 6);
  else if(timer == 4) pressButton(4, 4);
  timer = 0;
}

//타이머 설정 함수
void setTimer(int hour) {
  Timer_Reset();
  pressButton(4, hour);
  timer = hour;
}

// 바람 세기 지정 함수
void setWind(int windspeed) {
  Power_Off();
  POWER = true;
  pressButton(3, windspeed);
  mode = windspeed;
}
```

이 코드에는 한 가지 문제가 있다. 현재 선풍기의 버튼 상태를 아두이노가 '기억'하고 여기에 맞춰서 버튼을 누르기 때문에 선풍기에서 물리적으로 버튼을 누르면 동기화가 안 되어 바로 꼬이게 된다. 스위치에 디지털 핀 세 개를 추가로 연결하고 digitalRead()로 물리적인 누르기 동작까지 추적하면 해결할 수 있을 듯하다. 수정하기 귀찮아서 하지 않았다. 만약 수정할 일이 있다면 HC-06부터 뜯어버리고 ESP8266으로 Wi-Fi 통신부터 시킬 것이다.