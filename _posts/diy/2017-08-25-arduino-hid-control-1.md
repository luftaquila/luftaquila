---
title: 아두이노로 마우스 & 키보드 입력 제어 (1)
description: HID 장치가 뭐길래
category: diy
assets: /assets/posts/diy/2017-08-25-arduino-hid-control-1
image: /assets/posts/diy/2017-08-25-arduino-hid-control-1/main.png
layout: post
---

예전에 하던 전투기 시뮬레이션 게임 중에 Tom Clancy's H.A.W.X 라는 게임이 있었다. 조이스틱이 없어 키보드로 조작을 했었는데, 아무리 그래도 비행 시뮬레이션인데 조이스틱으로 플레이해주는 게 예의가 아닌가 싶어 한 번 알아보았다. 그런데 웬걸, 제일 허접한 제품도 5만원 돈은 하는게 아닌가. 그래서 직접 만들기로 했다. 아두이노만 있으면 세상에 못 만들 게 없다고 믿던 시절이었다. 초저가 저예산 아두이노 조이스틱 프로젝트 시작.  

<br>
#### 준비물
<div class='center'><img src='{{ page.assets }}/1.png'></div>

아두이노 보드 1(또는 2)개, 조이스틱 모듈 1개, 강인한 정신력, 불굴의 의지  

<br>
#### 전투 준비
만약 이 글을 보고 있는 당신의 손에 들려있는 보드가 아두이노 레오나르도가 아니라면, 심심한 위로의 말씀을 드리고 싶다. 이 글에 적힌 온갖 삽질을 앞으로 같이 해야 하기 때문이다. 혹시 야크 털 깎기라고 들어보았는가? 처음 들어본다면 [이 글](https://www.lesstif.com/software-engineering/yak-shaving-29590364.html){:target="_blank"}{:class="external"}을 읽어보는 것도 나쁘지 않을 것 같다. 이 작업은 처음부터 끝까지 야크 털에 파묻혀 앞이 보이지 않기 때문이다. 마음의 준비가 됐다면 바리깡을 손에 쥐고 전투를 치르러 가 보자.  

<div class='center'><img src='{{ page.assets }}/2.png'></div>

만약 레오나르도 보드를 가지고 있다면, 바로 [(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}으로 넘어가도 된다.

<br>
##### 목차
[(1) HID 장치가 뭐길래](https://luftaquila.io/blog/diy/arduino-hid-control-1/){:class="link"}  
[(2) HoodLoader2](https://luftaquila.io/blog/diy/arduino-hid-control-2/){:class="link"}  
[(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}

<br>
#### 왜 그러시는데요
레오나르도에 이렇게 특혜를 주는 이유는, 레오나르도 등에 탑재된 ATmega32u4 프로세서가 `HID 장치`로 인식되는 것을 기본으로 지원하기 때문이다. 레오나르도 외에도 릴리패드, 윤 등이 포함된다. 

<div class='center'>
  <img src='{{ page.assets }}/3.png' style='width: 45%'>
  <img src='{{ page.assets }}/4.png' style='width: 45%'>
</div>

생긴 것부터 다르다. 32u4는 이쁘장한 SMD타입이지만, 328P는 다시마처럼 생겼다. 물론 DIP타입만 있는 건 아니고 SMD타입 328P도 존재하긴 한다.

컴퓨터의 입력 장치를 제어하려면 Human Interface Device, HID라는 인터페이스가 필요하다. 우리가 사용하는 마우스와 키보드도 모두 이 HID 인터페이스를 사용해 컴퓨터의 입력을 제어하고 있다. 윈도우를 사용하고 있다면 <code class='highlighter-rouge'><i class='fab fa-windows'></i> + R</code>을 눌러 실행 창을 띄우고 `devmgmt.msc` 를 입력해 장치 관리자를 실행해 보자. `마우스 및 기타 포인팅 장치` 탭을 확장하면 HID 규격 마우스 같은 이름으로 나오는 장치가 하나쯤은 있을 것이다.

이 기능을 레오나르도를 필두로 한 ATmega32u4는 기본으로 지원한다. 업로드한 코드가 HID 라이브러리를 사용한다면 USB로 컴퓨터에 꽂으면 바로 HID 장치로 인식된다. 하지만 나머지 보드는... 그런 거 없다. 아두이노 스케치의 툴 - 보드 설정에서 보드를 우노로 설정하고, 파일 - 예제 - 09.USB 탭의 예제를 아무거나 컴파일해 보자. 분명 `Mouse.h`와 `Keyboard.h`가 설치되어 있고, #include 문으로 불러온 상태지만 컴파일 에러가 발생한다.  
```
'Mouse' 가 없습니다. 스케치에서 '#include < Mouse.h>' 를 포함했나요?
'Keyboard' 가 없습니다. 스케치에서 '#include < Keyboard.h>' 를 포함했나요?
```
여기서 정말 거품물고 쓰러지는 줄 알았다. 이게 왜 안 되는지, 프로세서가 HID 장치 지원을 안 하기 때문이라는 걸 깨닫기까지 3시간이 걸렸다. 똑같은 예제를 다시 툴 - 보드 설정에서 레오나르도로 변경하고 컴파일하면 전혀 문제가 없다. 이게 다 망할 다른 보드들이 HID 장치를 지원하지 않기 때문이다.

<br>
#### 불가능이란 없다
하지만 MCU가 32u4가 아닌 다른 보드들도 HID 장치로 인식시키는 방법이 있다. 물론, 조금 더 복잡하다. 센서들만 가지고 행복하게 작업하던 좋은 시절은 다 갔다. 부트로더를 갈아엎어야 한다. MCU에 대한 조금 더 높은 수준의 이해가 필요하지만, 다 이러면서 성장하는 것 아니겠는가.

<div class='center'><img src='{{ page.assets }}/5.png'></div>

아두이노 보드들에는 두 개의 MCU 칩이 들어가 있다. 우노에는 사진과 같이 주황색으로 표시한 ATmega16u2와, 빨간색으로 표시한 <del>다시마</del>Atmega328P가 있다.

<div class='center'><img src='{{ page.assets }}/main.png'></div>

우노의 핀맵을 보자. 핀마다 라벨이 덕지덕지 붙은 보드 가장자리의 핀들은 전부 328P가 컨트롤하는 핀이다. 사진 상단의 연갈색 상자에 적힌 몇 개의 핀만 16u2가 담당하는 핀이다. 평소에는 왜 있는지 모르겠고 여분의 5V 출력 단자로 쓰던 그 2x3핀 ICSP 단자다. 흔히 아두이노를 쓴다고 하는, 디지털/아날로그 핀으로 값 읽고 쓰고 하는 건 전부 328P가 담당한다. I/O라고 한다. Input / Output 즉 입출력이다. 반면 16u2는 USB to Serial 기능을 한다. 컴퓨터와 통신을 담당한다고 보면 된다.  

따라서 보드에 스케치를 업로드하면 그 코드가 가는 곳은 I/O를 제어하는 328P이고, 16u2는 사용자가 프로그래밍하는 것이 불가능하게 되어 있다. 레오나르도의 MCU인 ATmega32u4는 혼자 I/O 제어하고 USB 통신하고 다 할 수 있다. u라는 문자가 USB 시리얼이 활성화되어있다는 뜻이다. AVR 칩셋들의 명명 규칙에 대해서는 나중에 더 알아보기로 하자.  

우노의 경우도 u가 들어가는 16u2가 붙어있어 컴퓨터와 통신할 수 있는 것이다. 다만 이 16U2는 HID로 인식시킬 수는 있지만 연결된 I/O 핀이 없어 소용이 없다. 프로그래밍이 불가능한 것은 덤이고.  

<br>
#### 해결책
이 상황을 타개할 해결책은 두 가지가 있다. 첫 번째는 dfu-programmer 라는 툴을 이용한 펌웨어 바꿔치기다. 하지만 이 방법은 큰 함정이 있다. HID 펌웨어를 설치하면 코드 업로드가 불가능하다(!) 아두이노로 뭘 만들다 보면 코드 조금 바꾸고 다시 업로드하는게 일상인데, 그게 안 된다는 말이다. 코딩해서 업로드하고, 기본 펌웨어 지우고 HID 펌웨어 깔고 테스트해보고, 안 돌아가네? HID 펌웨어 지우고 기본 펌웨어 깔고, 코드 수정해서 업로드하고, 기본 펌웨어 지우고 HID 펌웨어 깔고 테스트... 생각만 해도 끔찍하다.

다른 방법이 바로 HoodLoader2라는 부트로더이다. HoodLoader는 아두이노의 기본 DFU 부트로더를 대신하는 CDC 부트로더와 고속 USB 시리얼 브릿지로 구성되어 있다. CDC 부트로더는 이름에 u가 붙는 USB 통신 MCU를 프로그래밍 할 수 있게 만들어 주고, 고속 USB 시리얼 브릿지는 동시에 I/O MCU를 프로그래밍할 수 있게 만들어 준다.

<div class='center'><img src='{{ page.assets }}/6.png'></div>

HoodLoader2의 동작 개념도이다. 16u2를 프로그래밍 가능하게 만들고, 328P와 하드웨어 시리얼로 연결한다. 두 MCU가 서로 시리얼 통신을 주고받을 수 있도록 만드는 것이다. 328P가 I/O 핀으로 조이스틱 상태를 검출하면, 16u2가 컴퓨터에 HID 인터페이스로 전송할 수 있게 된다. 다만 HoodLoader에서 CDC 프로그래밍을 위해 57600 보드 레이트는 사용이 제한되니 유의해야 한다. HoodLoader2를 아두이노에 올리는 작업은 다음 글 [(2) HoodLoader2](https://luftaquila.io/blog/diy/arduino-hid-control-2/){:class="link"} 에서 마저 하겠다.

<br>
##### 목차
[(1) HID 장치가 뭐길래](https://luftaquila.io/blog/diy/arduino-hid-control-1/){:class="link"}  
[(2) HoodLoader2](https://luftaquila.io/blog/diy/arduino-hid-control-2/){:class="link"}  
[(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}