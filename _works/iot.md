---
title: 홈 IoT 컨트롤 허브
description: 
date: 2021-07-06
image: /assets/images/works/iot/main.png
layout: post
---
[서비스 링크](https://iot.luftaquila.io){:target="blank"}{:class='link'}
&emsp;
[GitHub 저장소](https://github.com/luftaquila/iot){:target="_blank"}{:class='link'}  

IoT로 설계되지 않은 집 안의 여러 요소를 ESP8266을 활용하여 IoT 장치로 만들고, 이를 한 곳에서 제어할 수 있도록 만든 컨트롤 허브입니다.

IoT 장치들과 컨트롤 허브는 서버와 소켓 통신으로 연결되어 실시간으로 제어 내용이 반영됩니다. 허브를 통하지 않더라도 HTTP Request로 제어할 수 있도록 Express.js를 통한 [REST API](https://luftaquila.io/docs/iot/){:target="blank"}{:class='link'}가 구현되어 있습니다.

관련된 작업은 [ESP12 IoT 전등 스위치 제작](https://luftaquila.io/blog/diy/esp12-iot-switch/){:target="blank"}{:class='link'}과, [멀쩡한 선풍기 IoT 선풍기로 만들기](https://luftaquila.io/blog/diy/arduino-turn-fan-into-iot/){:target="blank"}{:class='link'}에서 확인하실 수 있습니다.