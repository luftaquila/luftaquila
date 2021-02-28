---
title: 32 &times; 16 RGB LED 매트릭스 제어
description: 직접 만들어 쓰는 전광판
category: diy
assets: /assets/posts/diy/2017-10-08-led-matrix-control
image: /assets/posts/diy/2017-10-08-led-matrix-control/main.png
layout: post
---

어떤 분께서 버스에 들어가는 전광판을 만들고 남은 모듈을 무료나눔한다는 글을 보고 연락을 드려 받아왔다. 택배로 보낼 사이즈가 아니라 직접 와야 한다기에 구성역까지 지하철을 타고 가겠다고 했다. 16kg 나가는데 괜찮겠냐 하시기에 괜찮다고 했는데, 실제로 받아와보니 전혀 괜찮지 않았다.
<div class='center'><img src='{{page.assets}}/1.png'></div>
엄청나게 무거웠다. 역에서 집까지 짊어지고 오는 동안 팔이 만신창이가 됐다.

자세히 보니 전광판 하나에 32 &times; 16 LED 매트릭스가 다섯 개 붙어있는 형태다. LED가 총 2560개 있는 셈이다. 인터페이스는 HUB-75 규격으로, 1/8의 Scan rate를 가지는 패널이다. 만만하게 생각하고 아두이노로 제어를 시도했다. Adafruit사가 개발한 [RGB-matrix-Panel](https://github.com/adafruit/RGB-matrix-Panel){:target="_blank"}{:class="external} 와 [Adafruit-GFX-Library](https://github.com/adafruit/Adafruit-GFX-Library){:target="_blank"}{:class="external}를 사용했다. 다섯 개나 패널을 이어붙인 사례는 없었지만, 동일한 32 &times; 16 패널 하나를 제어한 사례가 많아서 당연히 될 거라고 생각했다.

<div class='center'><img src='{{page.assets}}/2.png'></div>
12V 노트북 어댑터로 전원을 공급하고 아두이노 테스트 코드를 업로드해 실행해 봤다. 

<div class='center'><img src='{{page.assets}}/3.png'></div>
사진을 보면 제일 우측 패널은 정상적으로 출력되지만, 다음 세트부터 픽셀이 아래로 한 칸씩 밀리는 현상이 있다. 도무지 이 현상을 해결할 수가 없어 일단 포기했었는데, 나중에 알고 보니 아두이노의 램이 모자라서 생기는 현상이었다. 아두이노 우노의 램은 32KB이다. 2560개의 LED를 컨트롤하니 램이 부족해 작동을 멈춘 것이다. 그래서 라즈베리파이로 넘어가기로 했다.

라즈베리파이 3B+는 2GB의 메모리 사이즈를 가지고 있다. [rpi-rgb-led-matrix](https://github.com/luftaquila/rpi-rgb-led-matrix){:target="_blank"}{:class="external} 라이브러리의 Python binding을 이용해 작성하니 아무 문제없이 잘 출력이 됐다. 글자 세트는 bdf 확장자의 폰트 파일을 사용하는데, 한글 폰트를 bdf 형식으로 바꾸어 사용하면 한글 출력도 문제없이 사용할 수 있었다.
<div class='center'><img src='{{page.assets}}/main.png'></div>