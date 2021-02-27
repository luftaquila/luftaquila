---
title: ESP12 IoT 전등 스위치 제작
description: 지구 반대편에서도 끄고 켜는 와이파이 스위치 만들기
category: diy
assets: /assets/posts/diy/2018-01-12-esp12-iot-switch
image: /assets/posts/diy/2018-01-12-esp12-iot-switch/main.png
layout: post
---

하루를 마치고 침대에 누우면 잠이 솔솔 온다. 이대로 잠들어버리면 참 좋을 텐데 아차, 방에 불을 끄지 않았다.  불 끄러 침대에서 일어나는게 세상에서 제일 귀찮은데 안타깝게도 불 좀 끄라고 부를 동생이 없다면 방법은 하나다. 대신 불을 끌 누군가를 직접 만드는 수밖에.

<center>
  <img src='{{ page.assets }}/1.png'>
</center>
2015년에 제작한 원격 전등 스위치의 최초 버전이다. 블루투스 통신을 위한 HC-06이 보인다.  
<del>폭탄인가?</del>

원격 스위치를 만들 때 가장 문제가 되는 부분은 기존 스위치와의 연결이다. 기존 전등 스위치의 양 접점에 릴레이를 그대로 붙이면 제어에 문제가 발생한다.

<center>
  <img src='{{ page.assets }}/2.png'>
</center>
마치 이런 상황이 되어 릴레이나 스위치 둘 중 한 쪽만 켜도 무조건 닫힌 회로가 된다. 한 쪽에서 불을 켜면 다른 쪽은 무슨 짓을 해도 불을 끌 수가 없다. 그렇다고 물리적인 스위치를 제거하면 스마트폰이 있어야만 불을 끄고 켤 수 있는 상태가 된다.

<center>
  <img src='{{ page.assets }}/3.png'>
</center>
그렇다면 작동에 방해가 되는 스위치는 그냥 치워버리자. 아예 물리적인 스위치 부분을 뜯어버리고, 물리적인 스위치의 역할까지 MCU가 통제하도록 만들면 된다. 그림의 동그란 물체는 물리적인 스위치를 대체할 정전용량 터치 센서라고 쓰지만 그냥 흔한 금속판이라고 읽는 물건이다. 무선 신호를 받거나 금속 판에 무언가 닿으면 릴레이를 조작하도록 만들어 보자.


#### 제작
<center>
  <img src='{{ page.assets }}/4.png'>
</center>
배선은 다음과 같다. MCU가 아두이노였다가 ESP12였다가 왔다갔다하는 이유는 예전에 작성했던 글들을 합쳐 재작성하다 보니 그런 것이다. 릴레이 제어를 아두이노로 하면 둘 다 로직 레벨이 5V이기 때문에 아무 문제가 없지만, ESP12는 로직 레벨이 3.3V이므로 릴레이에 열심히 HIGH, LOW를 줘봤자 동작하지 않는다. 로직 레벨 컨버터를 쓰면 되지만, 컨버터는 손톱만한 주제에 몇천 원씩이나 한다. 50원짜리 트랜지스터 하나면 대체할 수 있다.

이 프로젝트는 와이파이를 통해 인터넷에 연결해 제어하는 방식이므로 당연히 서버가 필요하다. 지금이야 개인 서버를 하나 가지고 있지만 이걸 만들 당시에는 없었고, 집에 불 좀 핸드폰으로 끄겠다고 개인 서버를 차릴 수는 없는 노릇아닌가. 다행히 Blynk라는 서비스가 있다. 아두이노 스케치에서 Blynk를 사용하기 위한 라이브러리는 [Blynk C++ Library](https://github.com/blynkkk/blynk-library){:target='_blank'}{:class='external'} 에서 다운로드할 수 있다.

또, ESP8266 계열 MCU에 아두이노 프로그래밍이 가능하게 만드려면 펌웨어를 바꿔 써야 한다. 여기에는 FTDI 모듈과 3.3V 전원이 필요하다. ESP의 TX, RX를 각각 FTDI의 RX, TX에 연결하고, CH_PD와 VCC에는 3.3V를 공급한다. 전원과 ESP, FTDI의 GND는 모두 하나로 연결한다. ESP의 GPIO0 핀도 GND에 연결해야 한다.  

<center>
  <img src='{{ page.assets }}/main.png'>
</center>
ESP-12는 각 핀 사이의 간격인 핀 피치가 2mm로 2.54mm인 아두이노보다 작다. 아무것도 없는 에폭시 판때기 주제에 개당 천 원씩이나 하는 [어댑터 보드](https://www.esp8266.com/viewtopic.php?f=13&t=6505){:target='_blank'}{:class='external'}를 사자니 뭔가 억울하지만, 있으면 확실히 편리하다. 보드 뒷면에 662k 3.3V 레귤레이터를 붙이고 앞면의 0이라고 적힌 SMD 저항을 제거하면 어댑터 보드의 <dfn>VCC</dfn>에 5V를 공급해도 MCU에는 3.3V를 줄 수 있다.

배선이 끝났으면 FTDI 모듈과 컴퓨터를 연결하고, 펌웨어를 새로 업로드한다. 펌웨어 업로드에는 아래 두 파일이 필요하다. `esp8266_flasher.exe`에서 Bin을 클릭해서 `v0.9.2.2 AT Firmware.bin` 파일을 선택한다. 포트 번호인 COM1 부분은 실제 FTDI 모듈이 연결된 포트 번호로 바꿔주어야 한다. FTDI 모듈의 포트 번호는 윈도우의 경우 장치관리자(devmgmt.msc)의 포트 탭에서 확인할 수 있다. Download 버튼을 누르면 펌웨어 덮어쓰기를 시작한다.

[<i class='fas fa-download'></i> esp8266_flasher.exe](https://luftaquila.io/droppy/$/AYpDi)
[<i class='fas fa-download'></i> v0.9.2.2 AT Firmware.bin](https://luftaquila.io/droppy/$/mtJCC)

#### 진짜 제작
준비할 게 많았지만, 이제 정말 프로그래밍이다.
<center>
  <img src='{{ page.assets }}/5.png'>
</center>
스마트폰에 Blynk 앱을 다운로드하고 프로젝트를 생성한 뒤, 푸쉬 버튼을 하나 배치한다. 버튼 세팅의 OUTPUT 탭에서 SWITCH모드, Select pin - Virtual - V0을 선택해 가상 핀으로 지정한다.  
Blynk 앱에서 프로젝트를 생성하면 Auth Token이 발급된다. 코드에 이 토큰을 첨부해야 하니, <del>옮겨 적</del>이메일 전송 기능을 이용해서 컴퓨터로 옮기자.

Auth Token 자리에 아까 옮긴 토큰을, SSID NAME 부분에는 연결할 와이파이의 이름을, Password 부분에 비밀번호를 입력한다. 공개 와이파이의 경우 비밀번호는 공백("")으로 남겨둔다. 핀 배선을 코드와 다르게 했다면 핀 번호를 수정해야 한다.

``` cpp
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <CapacitiveSensor.h>
 
CapacitiveSensor CS = CapacitiveSensor(4, 5);
 
char auth[] = "Auth Token";
char ssid[] = "SSID NAME";
char pass[] = "Password";
 
boolean RLY;
 
void setup() {
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  RLY = false;
 
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
}
 
void loop() {
  Blynk.run();
   
  long TCH = CS.capacitiveSensorRaw(30);
  if(TCH > 10000) {
    if(RLY) {
      digitalWrite(13, LOW);
      Blynk.virtualWrite(V0, 0);
      RLY = false;
      delay(200);
    }
    else {
      digitalWrite(13, HIGH);
      Blynk.virtualWrite(V0, 1);
      RLY = true;
      delay(200);
    }
  }
}
 
BLYNK_WRITE(V0) {
  int rcv = param.asInt();
  if(rcv) {
    digitalWrite(13, HIGH);
    RLY = true;
  }
  else {
    digitalWrite(13, LOW);
    RLY = false;
  }
}
 
BLYNK_CONNECTED() { Blynk.syncVirtual(V0); }
 
BLYNK_APP_CONNECTED() {
  if(RLY) Blynk.virtualWrite(V0, 1);
  else Blynk.virtualWrite(V0, 0);
}
```

ESP8266 계열은 코드 업로드도 그냥 아두이노만큼 만만치 않다. NodeMCU같은 ESP 개발 보드는 해당사항이 없지만 일반 ESP 모듈은 프로그래밍 모드로 부팅해야만 프로그램 업로드가 가능하다.  
프로그래밍 모드는 GPIO0에 GND를 입력하면 활성화된다. 전원 공급 시에 GPIO0이 LOW여야 한다. 그렇지 않을 경우, 일반 모드로 실행되어 기존의 업로드된 프로그램을 실행한다.

<video controls style='width: 100%; height: auto'>
  <source src="{{ page.assets }}/movie.mp4" type="video/mp4">
  Sorry, your browser doesn't support embedded videos.
</video>
업로드를 마치고 일반 모드로 재부팅하면 이렇게 작동한다. 이제 방 스위치를 떼어내고 이걸 집어넣기만 하면 된다. 작업할 때는 항상 전기 안전에 유의한다. 상용 220V는 굉장히 위험하다.

<center>
  <img src='{{ page.assets }}/6.png' style='width: 30%'>
  <img src='{{ page.assets }}/7.png' style='width: 30%'>
  <img src='{{ page.assets }}/8.png' style='width: 30%'>
</center>
잘 집어넣고 닫아준다. 어차피 스위치 안에 들어가니 패키징에는 따로 신경쓰지 않았다.

<center>
  <video controls>
    <source src="{{ page.assets }}/video.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
  </video>
</center>
작동 영상은 ESP12 버전일 때 찍어놓은게 없어서 HC-06을 이용한 블루투스 통신 버전일 때 영상을 첨부한다.


