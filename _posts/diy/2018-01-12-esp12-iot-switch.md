---
title: ESP12 IoT 전등 스위치 만들기
description: 지구 반대편에서도 끄고 켜는 초특급 와이파이 스위치!
category: diy
assets: /assets/posts/diy/2018-01-12-esp12-iot-switch
image: /assets/posts/diy/2018-01-12-esp12-iot-switch/main.png
layout: post
---

힘든 하루를 마치고 침대에 누우면 기분이 참 좋습니다. 이대로 잠이 들 것 같은데 방에 불이 켜져있습니다. 세상에서 불 끄러 일어나기가 제일 귀찮은데 안타깝게도 불 좀 끄라고 부를 동생이 없습니다. 그렇다면 방법은 하나입니다. 직접 대신 꺼줄 누군가를 만드세요!

···에서 시작한 원격 전등 스위치를 처음 만든 게 무려 3년 전입니다.

<center>
  <img src='{{ page.assets }}/1.png'>
</center>
2015년에 만들었던 최초 버전입니다. 블루투스 통신을 위해 HC-06이 붙어있는 걸 볼 수 있습니다.  
<del>폭탄인가?</del>

원격 스위치를 만들 때 가장 문제가 되는 부분은 기존 스위치와의 연결입니다. 기존 전등 스위치의 접점에 릴레이를 그대로 붙여버리면 둘 중 한 쪽에서만 제어가 가능해집니다. 무슨 말이냐 하면, 

<center>
  <img src='{{ page.assets }}/2.png'>
</center>
마치 이런 상황이 되어 한 쪽에서 스위치를 닫아버리면 다른 쪽이 무슨 짓을 해도 닫힌 회로가 되어 불이 꺼지지 않습니다. 그렇다고 스위치를 없애버리자니 스마트폰이 있어야만 불을 끌 수 있는 상태가 되어 버립니다.

<center>
  <img src='{{ page.assets }}/3.png'>
</center>
그렇다면 작동에 방해가 되는 것들은 전부 치워버립니다. 아예 물리적인 스위치 부분을 뜯어버리고, 물리적인 스위치의 역할까지 MCU가 통제하도록 만들면 됩니다. 동그란 건 물리적인 스위치를 대체할 정전용량 터치 센서라고 쓰고 그냥 흔한 금속판이라고 읽는 물건입니다. 무선 신호를 받거나 금속 판에 무언가 닿으면 릴레이를 조작하도록 만들어 보겠습니다.


#### 제작
<center>
  <img src='{{ page.assets }}/4.png'>
</center>
배선은 다음과 같습니다. 예전 글을 짬뽕해서 재작성하다 보니 MCU가 아두이노였다가 ESP12였다가 왔다갔다하는데, 감안해서 보시기 바랍니다. 릴레이 제어를 아두이노로 하면 둘 다 로직 레벨이 5V이기 때문에 아무 문제가 없지만, ESP12는 로직 레벨이 3.3V이므로 릴레이에 열심히 HIGH, LOW를 줘봤자 동작하지 않습니다. 로직 레벨 컨버터를 쓰면 되지만, 컨버터는 손톱만한 주제에 몇천 원씩이나 합니다. 50원짜리 트랜지스터 하나면 대체가 가능합니다.

이 프로젝트는 와이파이를 통해 인터넷에 연결해 제어하는 방식이므로 당연히 서버가 필요합니다. 하지만 집에 불 좀 핸드폰으로 끄겠다고 개인 서버를 차릴 수는 없는 노릇입니다. 다행히 Blynk라는 서비스를 이용하면 쉽게 구성할 수 있습니다. 아두이노 스케치에서 Blynk를 사용하기 위한 라이브러리를 [Blynk C++ Library](https://github.com/blynkkk/blynk-library){:target='_blank'}{:class='external'} 에서 다운받아 설치해 줍니다.

또, ESP8266에 아두이노 프로그래밍이 가능하게 만드려면 펌웨어 변경이 필요합니다. 여기에는 FTDI 모듈과 3.3V 전원이 필요합니다. ESP의 TX, RX를 각각 FTDI의 RX, TX에 연결하고, CH_PD와 VCC에는 3.3V를 공급합니다. 전원과 ESP, FTDI의 GND는 모두 하나로 연결해 줍니다. ESP의 GPIO0 핀도 GND에 연결합니다.  

<center>
  <img src='{{ page.assets }}/main.png'>
</center>
ESP-12는 각 핀 사이의 간격인 핀 피치가 2mm로 2.54mm인 아두이노보다 작습니다. 아무것도 없는 에폭시 덩어리 주제에 개당 천 원씩이나 하는 [어댑터 보드](https://www.esp8266.com/viewtopic.php?f=13&t=6505){:target='_blank'}{:class='external'}를 사자니 뭔가 억울하지만, 있으면 편리합니다. 보드 뒷면에 662k 3.3V 레귤레이터를 붙이고 앞면의 0이라고 적힌 SMD 저항을 제거하면 어댑터 보드의 <dfn>VCC</dfn>에 5V를 공급해도 MCU에는 3.3V가 들어갑니다.

배선이 끝났으면 FTDI 모듈과 컴퓨터를 연결하고, 아래 두 파일을 다운로드합니다. `esp8266_flasher.exe`를 실행하고 Bin을 클릭해서 `v0.9.2.2 AT Firmware.bin` 파일을 선택해 줍니다. COM1 부분은 FTDI 모듈이 연결된 포트 번호로 바꿔주어야 합니다. 윈도우 장치관리자(devmgmt.msc)의 포트 탭에서 FTDI 모듈의 포트 번호를 확인할 수 있습니다. 마지막으로 Download 버튼을 누르면 펌웨어 덮어쓰기를 시작합니다.

[<i class='fas fa-download'></i> esp8266_flasher.exe](https://luftaquila.io/droppy/$/AYpDi)
[<i class='fas fa-download'></i> v0.9.2.2 AT Firmware.bin](https://luftaquila.io/droppy/$/mtJCC)

#### 진짜 제작
준비할 게 많았습니다. 이제 진짜 프로그래밍 단계입니다.
<center>
  <img src='{{ page.assets }}/5.png'>
</center>
스마트폰에 Blynk 앱을 다운로드하고 프로젝트를 생성한 뒤, 푸쉬 버튼을 하나 배치해 줍니다. 버튼 세팅의 OUTPUT 탭에서 SWITCH모드, Select pin - Virtual - V0을 선택해 가상 핀을 지정해 줍니다.  
Blynk 앱에서 프로젝트를 생성하면 Auth Token이 발급됩니다. 코드에 이 토큰을 첨부해야 하니, <del>옮겨 적</del>이메일 전송 기능을 이용해서 컴퓨터로 옮깁니다.

드디어 코드 업로드입니다. Auth Token 자리에 아까 옮긴 토큰을, SSID NAME 부분에는 연결할 와이파이의 이름을, Password 부분에 비밀번호를 입력합니다. 공개 와이파이의 경우 공백("")으로 남겨둡니다. 핀 배선을 다르게 했다면 코드에서 핀을 수정해 줍니다.
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
하지만 코드 업로드도 그냥 아두이노만큼 만만치 않습니다. NodeMCU같은 ESP 개발 보드는 해당사항이 없지만 일반 ESP 모듈은 프로그래밍 모드로 부팅해야만 프로그램 업로드가 가능합니다.  
프로그래밍 모드는 GPIO0에 GND를 입력하면 활성화됩니다. 전원 공급 시에 GPIO0이 LOW여야 합니다. 그렇지 않을 경우, 일반 모드로 실행되어 업로드된 프로그램을 실행합니다.

<video controls style='width: 100%; height: auto'>
  <source src="{{ page.assets }}/movie.mp4" type="video/mp4">
  Sorry, your browser doesn't support embedded videos.
</video>
업로드를 마치고 일반 모드로 재부팅하면 이렇게 작동합니다. 이제 방 스위치를 떼어내고 이걸 집어넣기만 하면 됩니다. 작업할 때 전기 안전에 유의합니다.

<center>
  <img src='{{ page.assets }}/6.png' style='width: 30%'>
  <img src='{{ page.assets }}/7.png' style='width: 30%'>
  <img src='{{ page.assets }}/8.png' style='width: 30%'>
</center>
잘 집어넣고 닫아줍니다.

<center>
  <video controls>
    <source src="{{ page.assets }}/video.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
  </video>
</center>
작동 영상은 ESP12일 때 찍어놓은게 없어서 HC-06을 이용한 블루투스 통신 버전일 때 영상을 첨부합니다.


