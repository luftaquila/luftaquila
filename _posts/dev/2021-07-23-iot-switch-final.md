---
title: IoT 컨트롤 허브 개발
description: IoT스위치_최종_진짜마지막_끝_완성본.html
category: dev
assets: /assets/posts/dev/2021-07-23-iot-switch-final
image: /assets/posts/dev/2021-07-23-iot-switch-final/main.png
layout: post
---

이런저런 짝퉁 IoT([ESP12 IoT 전등 스위치 제작](https://luftaquila.io/blog/diy/esp12-iot-switch/){:target="_blank"}{:class='link'}, [멀쩡한 선풍기 IoT 선풍기로 만들기](https://luftaquila.io/blog/diy/arduino-turn-fan-into-iot/){:target="_blank"}{:class='link'})를 만들고 보니, 얘는 여기서 제어하고 쟤는 저기서 제어하는게 맘에 들지 않았다. 이사도 온 김에 다 새로 만들기로 했다. 이전 버전을 만든 지도 3년이 지났으니, 뭔가 개선할 수 있을 것 같았다. 한 화면에서 개조한 것들을 전부 제어할 수 있도록 Google Home 같은 걸 만들어 보기로 했다. ~~그냥 구글 홈을 사면 되잖아?~~ 

#### 문제 1
위 ESP12 IoT 전등 스위치의 최대 단점은, **별도의 전원 공급**이 필요하다는 거다. 가정용 AC 전원은 활선(Line)과 중성선(Neutral)으로 구성되어 있다. 요즘 아파트들은 스마트홈을 구축한다고 스위치박스에 중성선도 들어가는 것 같지만, 대부분 아파트의 스위치박스에는 활선과, 부하(전등 등)에 연결된 로드선(Load)만 들어 있다. 중성선은 전등의 로드선 반대편 단자에 전기공사되어 벽이나 천장 속에 들어 있다. 

스위치를 켜면 *활선 - 스위치 - 로드선 - 전등 - 중성선* 순으로 연결되어 전등이 전원을 공급받는다. 여기서 스위치의 양쪽에는 활선과 로드선만 있기 때문에, 이걸 가지고 상시 전원을 만들어낼 수는 없다.. 라고 생각했는데, [방법](https://patents.google.com/patent/KR100716016B1/ko){:target="_blank"}{:class='external'}이 있기는 한 것 같다. 근데 저런 회로까지 만들 자신은 없었다.  

#### 문제 2
스위치박스에 중성선이 없다면 있는 곳으로 찾아가면 된다. 부하인 전등은 스위치를 켜면 양 전선이 활선과 중성선이 되어 전원을 공급받는다. 여기에 제어 모듈을 붙여 놓고 스위치는 항상 켜 두면 된다. 다만 이러면 또 문제가 생긴다. 제어 모듈이 천장의 전등에 붙어 있어서, **수동 조작이 불가능**하다. 

<div class='center'><img src='{{ page.assets }}/1.png'></div>

제어를 하겠다고 릴레이를 기존 스위치와 병렬로 붙여 놓으면 위와 같은 회로가 된다. 스위치나 릴레이 중 하나만 켜져 있어도 무조건 닫힌 회로가 되어 반대편에서 아무리 조작을 해도 작동하지 않는다. 전등 제어는 무조건 제어 모듈에 맡기고, 수동 조작 스위치도 제어 모듈이 인식하게 만들어야 한다. *ESP12 IoT 전등 스위치 제작* 처럼 터치 스위치를 붙이거나, 기존 스위치를 연결해도 된다. 그래서 제어 모듈을 천장에 붙이면 또 수동 스위치 배선이 어려워진다.

<div class='center'><img src='{{ page.assets }}/2.png'><br>할머니집에나 있던 줄스위치를 쓰는게 아니고서야...</div>

#### 해결책
문제가 있다면 과연 그 문제가 해결해야 하는 문제인지 곰곰히 생각해 보자. 수동 조작 스위치가 없다면 제어 모듈을 통해서 핸드폰으로만 불을 껐다 켤 수 있다. 내가 핸드폰이 없는데 방 불을 켜야 할 상황이 있을까? 핸드폰이 없더라도 컴퓨터는 거의 항상 켜져 있어 컴퓨터로도 제어할 수 있으니 가벼운 마음으로 수동 스위치는 해결을 포기하고 천장의 전등에 제어 모듈을 붙이기로 했다. 이 시스템을 만들어 사용한지 2주 정도 지났지만 아직 불편한 적은 없었다.

#### 하드웨어
<div class='center'><img src='{{ page.assets }}/3.png'></div>

제어에는 ESP-12F 모듈을 사용한다. ESP계열 MCU들은 1달러밖에 안 하는 가격에 알리에서 살 수 있는데다 아두이노로도 프로그래밍할 수 있다. 다만 핀 피치가 2mm로 아두이노의 2.54mm와 달라 기존의 점퍼 케이블 등을 사용하기 어렵다. 그리고 로직 레벨이 3.3V라서 전원 공급용으로 쓸 핸드폰 충전기의 5V를 그대로 사용할 수 없다는 단점이 있다. 이런 단점은 사진의 하얀색 어댑터 보드로 해결할 수 있다.

<div class='center'>
  <img src='{{ page.assets }}/4.png' style='width: 45%'>
  <img src='{{ page.assets }}/5.png' style='width: 45%'>
</div>

어댑터 보드 뒷면에 3.3V 레귤레이터를 붙이고 앞면의 <dfn>0Ω</dfn> 저항인 <dfn>R2</dfn>를 제거하면 아래 사진처럼 5V를 주어도 ESP의 파워라인에는 3.3V가 들어간다. 다만 레귤레이터 사이즈는 AMS1117-3.3V이 딱 맞는 SOT-223 규격의 크기인데 AMS1117-3.3V은 단자 배열이 안 맞아 사용할 수가 없다. 배열은 662K와 딱 맞는데 이 친구는 SOT-23 규격이라 눈꼽만 하다. 무슨 레귤레이터를 쓰라고 PCB를 만들어 놓은 건지 모르겠다. 662k는 너무 작아 납땜하기 힘들어서 AMS1117을 어거지로 저렇게 괴상하게 배선했다.

<div class='center'>
  <img src='{{ page.assets }}/6.png' style='width: 45%'>
  <img src='{{ page.assets }}/7.png' style='width: 45%'>
</div>

제어할 릴레이는 흔한 5V 릴레이인데 ESP-12F의 로직 레벨은 3.3V라 신호 라인에 HIGH를 주었을 때 동작할 지 장담할 수 없다. 릴레이의 SIG 핀과 5V 핀은 충전기의 +라인과 바로 연결하여 항상 켜진 상태로 둔다. 우리는 NPN 트랜지스터를 이용해서 ESP의 GPIO 핀으로 릴레이의 GND와 충전기의 -라인을 뗐다 붙였다 할 예정이다.

<div class='center'><img src='{{ page.assets }}/8.png'><br>나름 열심히 그렸는데..</div>

제어 모듈인 CONTROLLER는 CHARGER라고 적힌 5V 휴대폰 충전기 회로로부터 전원을 공급받는다. ESP는 3.3V 레귤레이터를 거쳐 전원을 공급받고, 릴레이 또한 5V핀과 S핀은 모두 충전기의 +선에 연결되어 -선만 GND에 연결되면 바로 켜지면서 릴레이 스위치를 닫는다. 트랜지스터의 베이스는 GPIO핀과 연결되어 HIGH 신호를 받으면 이미터와 컬렉터 사이를 연결하는 스위치가 된다. 이미터는 충전기 -선에 연결하고 컬렉터는 릴레이의 GND에 연결하여 신호를 받으면 릴레이를 켜도록 한다. S1은 벽에 붙어있는 스위치로, 항상 켜 두어야 제어 모듈이 전원을 공급받을 수 있다.

<div class='center'>
  <img src='{{ page.assets }}/9.png' style='width: 30%'>
  <img src='{{ page.assets }}/10.png' style='width: 30%'>
  <img src='{{ page.assets }}/11.png' style='width: 30%'>
</div>

다 만들면 이렇게 된다. ESP는 GPIO0이 LOW인 상태로 전원을 켜야 프로그램을 업로드할 수 있다. GND와 GPIO0을 연결하는 택트 스위치를 하나 붙여 편하게 업로드할 수 있도록 했다. 프로그램을 업로드하고 전등에 달아 준다. 전기공사 할 때 차단기는 반드시 내려야 하는데.. 어차피 벽 스위치가 꺼져 있어 전기 통할 일이 없으니 그냥 작업했다. **목숨이 소중하다면** 차단기 작동 테스트도 할 겸 내리고 작업하자. 프로그램은 Blynk를 이용한다면 [ESP12 IoT 전등 스위치 제작](https://luftaquila.io/blog/diy/esp12-iot-switch/){:target="_blank"}{:class='link'}의 코드를 이용하면 된다. GPIO 핀 번호만 바꿔도 작동한다. 나는 서버까지 직접 만들 예정이라 [서버와 소켓 통신하는 코드](https://github.com/luftaquila/iot/blob/master/devices/passive_switch/passive_switch.ino){:target="_blank"}{:class='external'}를 작성해서 사용했다.

<div class='center'><img src='{{ page.assets }}/12.png'><br>코드가 작동하는지 확실히 확인하지 않으면 이런 불상사가 일어날 수 있다.</div>

#### 소프트웨어
갈 길이 멀다. 이제 위에서 만든 모듈과 소켓 통신하는 서버도 만들어야 하고 REST API를 위해서 Express 서버도 작성해야 한다. 앱은 만들 줄 몰라서 웹 어플리케이션으로 만들어야 하니 웹 프론트엔드도 해야 한다. Blynk 서비스를 이용하면 하나도 안 해도 된다. 그냥 회원가입하고 프로젝트 만들어서 설정 몇 개 하면 끝난다. 예전엔 Blynk 유료 버전 같은 거 누가 돈내고 쓰나 했는데 직접 만들어보니 알겠다. **그냥 돈 내는게 편하고 빠르다.** 그래도 내 스타일대로 만들기로 했으니 눈물을 머금고 코딩을 한다. 돈 낼 거였으면 IoT 스위치도 사서 썼겠지. 다 만드는데 한 20시간 걸렸나...?

만든 웹 인터페이스는 [IoT Control Hub](https://iot.luftaquila.io/){:target="_blank"}{:class='link'}에서, 서버와 프론트엔드 코드 전체는 [Github 프로젝트](https://github.com/luftaquila/iot){:target="_blank"}{:class='external'}에서 확인할 수 있다.

언제 무슨 바람이 불어 또 다른 걸 IoT로 개조하겠다고 할 지 모르니 [device.js](https://github.com/luftaquila/iot/blob/master/devices/device.mjs){:target="_blank"}{:class='external'}에서 확장성을 고려하여 각 장비를 Class로 구현했다. 방금 만든 전등 스위치는 신호를 받아서 껐다켰다만 해주면 되니 <kbd>PassiveSwitch</kbd>라고 이름을 지었다. 버튼이 방 전등 하나만 있으면 좀 썰렁해서 데스크탑 컴퓨터를 원격으로 켤 수 있게 WOL 스위치도 구현했다. 얘는 현재 상태를 알 필요도 없이 신호를 받으면 버튼을 딸깍 누르기만 하면 되니 <kbd>PassiveTactSwitch</kbd>라고 이름지었다.

#### 작동 테스트

<div class='center'>
  <video controls>
    <source src="{{ page.assets }}/video.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
  </video>
</div>

전부 다 만드는데 작업 시간으로만 꼬박 하루정도 걸렸다. 방 불 켜는데 5초, 컴퓨터 켜는 데 5초가 걸린다고 치고 하루에 불 네 번, 컴퓨터 두 번 켠다고 하면 매일 30초 정도 된다. 매일 30초의 시간을 편하게 살기 위해 24시간을 투자했으니 본전을 뽑으려면 <dfn>24 &times; 3600 &divide; 30 = 2880</dfn>일 정도 사용해야 한다. 약 7.9년이다. 그냥 구글 홈 사서 쓰는 것도 나쁘지 않을 것 같다.
