---
title: 무료 회로도 작성 프로그램 3선
description: Fritzing, TinyCAD, TinkerCAD
category: diy
assets: /assets/posts/diy/2017-08-01-free-circuit-drawing-tools
image: /assets/posts/diy/2017-08-01-free-circuit-drawing-tools/main.png
layout: post
---

아두이노 같은 걸 만지작거리다 보면 종종 회로도를 그려야 할 때가 있습니다. 보통은 다른 사람과 공유하기 위해서지만, 프로젝트가 커지면 자기가 알아보기 위해서도 필요합니다.  

하지만 아무리 경건한 마음으로 펜을 잡아도 종이에 그리자니 선이 삐뚤어지기 일쑤입니다. 잘못 그려서 지우려 하면 문제가 더 심각해집니다. 머리에 반도체가 든 사람이 아니라면 복잡한 회로도를 처음부터 완전히 머리에 집어넣고 그릴 수는 없습니다.

다행히도 우리 옆에는 머리에 반도체가 든 '컴퓨터'라는 훌륭한 친구가 있습니다. 무료 회로도 그리기 프로그램 중 가장 자주 사용하는 세 종류를 소개합니다. 회로 시뮬레이션이 되는 것도 있다구요!
<br><br>

#### Fritzing
무료 회로설계 프로그램에서 선두를 달리는 Fritzing입니다.  
<del>[http://fritzing.org/download/](http://fritzing.org/download/){:target="_blank"}{:class="link"}에서 No Donation을 선택하면 무료로 다운로드할 수 있습니다.</del>  
0.9.4 버전부터 유료화됐습니다. (···)  
무료였던 0.9.3b까지 구글에서 쉽게 구할 수 있습니다.  

프로그램을 실행하면 브레드보드, 스케메틱, PCB, Code 4개의 탭이 있습니다.  
1. 브레드보드
<img src='{{ page.assets }}/main.png'>
회로 기호가 아니라 이미지화된 실제 부품으로 회로도를 그릴 수 있습니다. 오른쪽의 라이브러리에서 부품을 끌어와 배치하면 됩니다. 회로도보다 덜 딱딱하고 알아보기 쉬워서 비전공자나 초심자에게 설명할 때 주로 사용합니다. 기본 회로 소자는 전부 포함되어 있고, 아두이노나 라즈베리파이같은 다양한 보드나 센서류도 대부분 있습니다. 없는 부품이더라도 구글에 `[부품명] fritzing part`로 검색하면 십중팔구 나옵니다.  

2. 스케메틱
<img src='{{ page.assets }}/1-fritzing.png'>
'회로도'를 실제로 그리는 곳입니다. 브레드보드 탭에서는 부품들이 이미지화되어 있었다면 여기서는 모두 기호화되어 있습니다. 부품의 빨간색 다리를 잡고 드래그하면 소자들끼리 연결할 수 있습니다.
<br><br>
다만, 소자를 연결한다고 배선이 자동으로 각이 잡히는 게 아닙니다. 최단거리 대각선으로 연결되어 일일히 각을 잡아줘야 하고, 부품을 회전시키면 가로 길이와 세로 길이가 달라 격자에 안 맞는 경우가 굉장히 많습니다. Fritzing의 스케메틱 기능은 7%정도 모자란 느낌입니다. 그래서 저는 진짜 회로도를 그릴 때는 다음에 소개할 프로그램을 주로 이용합니다. 일단 다음 탭부터 알아봅시다.

3. PCB, 4. Code  
PCB와 Code 탭은 각각 PCB를 설계하거나 아두이노처럼 프로그램 업로드가 필요한 경우에 업로드를 지원하는 기능입니다. 정말 쓸 일이 없습니다. PCB는 실제 설계에 쓰자니 뭔가 모자라고, 이걸로 아두이노에 업로드 하느니 그냥 스케치 쓰는게 훨씬 낫습니다.

요약하자면 Fritzing은 브레드보드 그래픽 디자인 말고는 쓸 기능이 없습니다. 빠르게 다음으로 넘어가겠습니다.
<br><br>

---
<br>
#### TinyCAD
기호로 정형화된 회로를 그릴 때 사용하는 오픈소스 툴인 TinyCAD입니다.
[http://tinycad.sourceforge.net](http://tinycad.sourceforge.net/){:target="_blank"}{:class='external'}
에서 다운로드할 수 있습니다.  

<img src='{{ page.assets }}/2-tinycad.png'>
왼쪽의 라이브러리에서 부품을 끌어 배치하고, Wiring 도구로 노드끼리 원하는 대로 연결할 수 있습니다. 알아서 각도 잡아 줍니다. 각 부품에 L1, R1같은 라벨링도 가능합니다.  
<br>
굳이 단점을 하나 꼽자면, 라이브러리가 너무 방대해서 원하는 부품을 찾기가 어렵다는 겁니다. 그래서 일상 생활에 자주 사용하는 부품만 따로 모아둔 라이브러리 파일을 공유합니다.  

[<i class='fas fa-download'></i> favorites.TCLib](https://luftaquila.io/droppy/$/zoltT)  


파일을 다운받아 TinyCAD 설치 폴더 안의 library 폴더에 집어넣거나, <kbd>Libraries...</kbd>도구에서 Add로 파일을 선택해 추가하면 왼쪽의 라이브러리 목록에서 볼 수 있습니다.  

심지어, 제한적인 회로 시뮬레이션도 가능합니다. 시뮬레이션에 관한 내용은 [Getting Started with Simulation Using TinyCad](http://www.users.on.net/~DrinkAlnwickRum/pages/tinycad/getstartOO.html){:target="_blank"}{:class='external'}을 참고하시면 됩니다.  
<del>개인적으로 기초전기실험 보고서 쓸 때 굉장히 유용하게 사용했습니다.</del>
<br><br>

---
<br>
#### TinkerCAD
마지막은 TinkerCAD입니다. 사용하기 쉬운 그래픽 UI와 함께하는 회로 시뮬레이션이 장점이지만, 오프라인 프로그램이 없는게 최대 단점입니다. 웹에서만 사용이 가능합니다.  
[https://www.tinkercad.com](https://www.tinkercad.com/){:target="_blank"}{:class='external'}에서 회원가입 후 `Circuits` 메뉴로 들어가면 됩니다.  

<img src='{{ page.assets }}/3-tinkercad.png'>
우측 상단의 Components 버튼을 이용해 부품을 끌어 배치하는 방식입니다. Fritzing과 굉장히 유사하지만 그래픽은 좀 더 아기자기한 편입니다. 다만 브라우저에서 돌아가다보니 자잘한 끊김과 버그가 있습니다.  

각 부품을 클릭하면 부품의 이름과 속성을 지정할 수 있습니다. `Shift`나 `Delete`, `Ctrl + C, V, Z` 등 기본적인 단축키도 지원합니다. Code Editor 기능으로 보드에 코드 업로드도 할 수 있지만, 마찬가지로 그냥 아두이노 사용자 분들은 아두이노 스케치 쓰는게 최고라고 생각합니다.  

회로 시뮬레이션도 아기자기한 그림 위에서 그대로 돌릴 수 있습니다. 회로 시뮬레이션 모드로 들어가 보겠습니다.
<img src='{{ page.assets }}/5-tinkercad-example-2.png'>
멀티미터 6개와 저항 하나, LED 2개, 파워서플라이를 가져왔습니다.  
LED 두 개를 병렬로 연결하고, 저항을 직렬로 연결해 줍니다.  

<img src='{{ page.assets }}/6-tinkercad-example-3.png'>
전부 다 연결하면 좀 정신없습니다. 전원을 아직 안 켰기 때문에 전류가 다 0A인 것을 볼 수 있습니다. 전압계에 전압이 잡히는 건 저항계의 전압인 것 같은데, 확실히는 모르겠네요.

<img src='{{ page.assets }}/7-tinkercad-example-4.png'>
전원을 켜면 값들이 찍힙니다. 전류가 흐르는 회로의 저항계에 에러가 나는 것까지 구현(?)되어 있습니다.  

오실로스코프 시뮬레이션도 가능합니다.  
<center>
<img src='{{ page.assets }}/8-tinkercad-example-5.png' style='width: 45%'>
<img src='{{ page.assets }}/9-tinkercad-example-6.png' style='width: 45%'>
</center>
가변 저항을 돌리면 아두이노의 디지털 핀 출력이 꺼졌다 켜지는 간격이 변화하며 LED가 점멸하는 시간도 달라집니다. 간단하게 아두이노로 파형을 만들었지만, 부품에 함수 제너레이터도 있습니다.