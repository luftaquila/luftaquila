---
title: 아두이노 USB 파워미터 DIY
description: 당신의 전기료는 안녕하십니까
category: diy
assets: /assets/posts/diy/2017-07-21-usb-wattmeter-diy
image: /assets/posts/diy/2017-07-21-usb-wattmeter-diy/main.png
layout: post
---

[ESP12 IoT 전등 스위치](https://luftaquila.io/blog/diy/esp12-iot-switch/){:target="_blank"}{:class="link"}를 만들고 나니 슬슬 걱정이 되었다. 1년 365일 핸드폰 충전기로 전원을 공급받는데 전기료가 어떻게 나올지 전혀 감이 안 잡히기 때문이었다. 전체 시스템이 다 합해봐야 한 200mA 쓸 테니 넉넉잡아도 1W 정도밖에 안 되긴 하지만, 그래도 두 눈으로 직접 확인해봐야 하지 않겠는가.

그래서 인터넷에 검색해 봤더니 파워미터라는 이름으로 이런 제품들이 눈에 띄었다.
<div class='center'><img src='{{page.assets}}/1.png'></div>
오 괜찮은데? 하고 가격을 보니 4만 원이 넘었다. 성능이 의심되는 저가형 제품들도 만얼마씩은 했다. 그냥 궁금했을 뿐이지 여기에 돈을 쓰고 싶은 생각은 없다. 그래서 직접 만들기로 했다.

파워미터는 적산전력계와 같다. 간단하게 설명하면 매 순간의 전압과 전류를 측정하고 <dfn>전력 P = 전압 V &times; 전류 I</dfn> 을 이용해 전력을 구한 다음 다 더해주면 된다.

#### 준비물
<div class='center'><img src='{{page.assets}}/2.png'></div>
아두이노와 전압 센서, 전류 센서, LCD 모니터 등등을 준비한다. 깔끔하게 제작해보려고 PCB 보드도 하나 구매했다.

<div class='center'><img src='{{page.assets}}/3.png'></div>
PCB에 부품 배치를 잡기 위해서 실사이즈로 그려 보았다. 캐드로 작성하면 좋겠지만, 아직 그렇게까지 다룰 줄은 모른다. 계획에 있는 ACS712는 홀 효과를 이용한 전류 센서인데, 특성상 자기장에 영향을 많이 받는다. 실사용에 사용하기 곤란해서 션트 저항을 사용하는 INA219로 대체하였다. 우측 하단에 개념도가 있다. 마이크로 5핀 커넥터로 입력을 받아 USB A타입 커넥터 두 개로 출력한다. 그 사이에 병렬로 연결한 전압 센서와 직렬로 연결한 전류 센서가 있다.
<div class='center'><img src='{{page.assets}}/7.png'></div>
요약하면 이 그림과 같다.

<div class='center'><img src='{{page.assets}}/4.png'></div>
Fritzing을 이용해서 그래픽으로도 그려 보았다. 굉장히 복잡하다. 필요없을 듯 하다.

#### 제작

<div class='center'>
  <img src='{{page.assets}}/5.png' style='width: 45%'>
  <img src='{{page.assets}}/6.png' style='width: 45%'>
</div>

입력 커넥터와 출력 커넥터를 연결할 때는 핀에 유의해야 한다. 데이터 라인은 연결할 필요가 없다. GND와 VCC만 연결해 주면 된다. 커넥터 사이에 들어갈 전류 센서 INA219에는 여섯 개의 핀이 있다. 그 중 네 개만 사용하면 된다.  
  
|INA219||아두이노|
|:-----:|:-----:|:-----:|
|Vcc|↔|+5V|
|Gnd|↔|GND|
|Scl|↔|A5|
|Sda|↔|A6|
  
<br>
이렇게 연결하면 된다. 전압 센서의 경우 저항이 <dfn>37.5kΩ</dfn> 인데, 이 정도면 전압계 치고는 저항이 아주 낮은 편이다. 멀티미터들의 경우 최소 수십 메가옴 정도는 한다. 도선에 그리 크지 않은 저항 하나를 병렬로 연결한 셈으로, 전류가 조금 깎여나가게 된다. 전압계를 사용하지 않고 INA219의 sensor219.getBusVoltage_V() 함수를 이용해 버스 전압을 재도 얼추 비슷하게 나온다.

다음은 LCD 디스플레이를 연결할 차례다. I2C 통신을 사용하지 않고 16핀을 그대로 사용하면 연결할 핀이 조금 많다. 
<div class='center'><img src='{{page.assets}}/8.png'></div>
LCD는 이렇게 생겼다. 제일 좌측 핀이 1번이고, 제일 우측 핀이 16번이다.  
1, 5, 15번 핀은 +5V / 2, 16번 핀은 GND / 3번 핀은 <dfn>2kΩ</dfn> 저항과 연결한 후 GND에 연결한다.  
4, 6, 11, 12, 13, 14번 핀은 각각 다른 디지털 핀에 대응시켜 준다. 여기서는 순서대로 D12 ~ D7에 대응시켰다.

마지막으로 입력 장치로 사용할 택트 스위치 하나를 D5에 연결했다.

<div class='center'>
  <img src='{{page.assets}}/9.png' style='width: 45%'>
  <img src='{{page.assets}}/10.png' style='width: 45%'>
</div>
먼저 부품을 하나하나 꽂고 납땜해 고정한다.

<div class='center'>
  <img src='{{page.assets}}/11.png' style='width: 45%'>
  <img src='{{page.assets}}/12.png' style='width: 45%'>
</div>
다음은 배선 지옥이다. LCD 때문에 연결할 케이블이 많아 시간이 꽤 걸렸다.

<div class='center'><img src='{{page.assets}}/main.png'></div>

뒷면은 전쟁터이지만, 그래도 앞면은 깔끔한 편이다.

<div class='center'>
  <img src='{{page.assets}}/13.png' style='width: 45%'>
  <img src='{{page.assets}}/14.png' style='width: 45%'>
</div>
LCD 테스트할 겸 샘플 코드를 몇 개 올려 장난을 좀 쳐 보았다. 하드웨어를 완성했으니 이제 프로그램을 올릴 차례다.

#### 프로그래밍
소프트웨어는 라이브러리만 있으면 간단하다.  
[Adafruit_INA219](https://github.com/adafruit/Adafruit_INA219){:target="_blank"}{:class="external"}  
[LiquidCrystal](https://playground.arduino.cc/Main/LiquidCrystal/){:target="_blank"}{:class="external"}  

이 두 개의 라이브러리를 이용해서 500ms마다 전류와 전압을 측정하고 전력을 계산해 전력량을 구한다. 코드가 길어 깃허브에 올려 두었다.  
[USB-Wattmeter-Dustmeter](https://github.com/luftaquila/USB-Wattmeter-Dustmeter){:target="_blank"}{:class="link"}  

이것저것 기능을 추가하다 보니 미세먼지 측정기 기능도 들어가 있다. 코드에서 `DustmeterLoop.ino` 부분을 제거하고 사용하면 된다.

<div class='center'>
  <video controls>
    <source src="{{ page.assets }}/video.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
  </video>
</div>
작동 시연 영상이다.