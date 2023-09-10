---
title: 컴퓨터 파워로 만드는 실험용 전원공급장치
description: 없으면 만들어 쓰는 헝그리 DIY
category: diy
assets: /assets/posts/diy/2018-01-14-power-supply-diy
image: /assets/posts/diy/2018-01-14-power-supply-diy/main.png
layout: post
---

이것저것 DIY를 하다 보면 전원공급장치가 필요한 경우가 많다. 라즈베리파이일 수도 있고, 어디선가 따로 떼어낸 부품에 전원을 인가해 볼 때도 필요하다. 특히 아두이노 계열이 대부분 5V에서 동작하기 때문에 5V가 빈번하게 필요하다. 하지만 주변에 마땅한 5V 소스로 쓸만한 건 해봐야 핸드폰 충전기나 보조배터리가 전부다. 이마저도 단자가 없어 단선된 케이블 피복을 벗겨 쓰곤 했다. 내구성이 정말.. 눈 뜨고 못 볼 수준이다. 하지만 어쩌겠는가. 학교 실험실만 가도 널린 파워 서플라이는 아무리 허접해 보여도 10만 원은 나간다. 여기에 10만 원을 쓰기엔 사야 할 게 너무 많다.  

그러던 중 아두이노 대신 ESP8266 계열을 주로 사용하게 되면서 3.3V 소스를 도무지 구할 수가 없어 결국 파워 서플라이를 하나 장만하기로 했다. 쓰는 전압이야 해봤자 3.3V와 5V 정도니 컴퓨터 파워를 개조해서 쓰면 될 것 같았다. 그래서 중고 컴퓨터 파워 하나를 구해 왔다. 

<div class='center'><img src='{{page.assets}}/1.png'></div>

몸체에 적힌 제원에 따르면 정격 출력은 3.3V 35A, 5V 25A, 12V 30A이다. 오버스펙이다. 5V 2A 충전기만 쓰다가 열 배는 높아진 출력 전류를 보니 흐뭇하다. 어떻게 개조할 지 생각을 좀 해보다가 인터넷에서 비슷한 작업을 한 사람들의 글을 좀 참고했다. 터미널 블록을 부착한 사람도 있고, 바나나 잭을 붙인 사람도 있어서 전부 다 가져다 때려넣기로 했다. 언제 어떻게 쓸 지 모르는데 많으면 많을 수록 좋은 것 아니겠는가.

대충 구상이 끝났으니 일단 뜯어볼 차례다. 원래 계획같은 건 하다보면 다 생기기 마련이다. 

<div class='center'><img src='{{page.assets}}/2.png'></div>

구매한 색깔별 바나나잭 4개와 토글 스위치, 작동 표시등 LED 등을 적당한 위치를 잡아 구멍 뚫고 고정해준다. 작동 표시등은 3.3V 라인에서 전선을 한 가닥 빼서 <dfn>1kΩ</dfn> 저항과 함께 연결했다.  
이 파워는 220V 전원 케이블 밑에 전원 스위치가 시소스위치로 딸려 있긴 하지만, 시소스위치는 껐다 켜는 맛이 없다. 끄고 켜기 편하게 앞면에 토글 스위치를 달았다. 다만, 이 토글 스위치로 220V를 직접 컨트롤하지는 않는다.

<div class='center'><img src='{{page.assets}}/3.png'></div>

컴퓨터 파워서플라이의 케이블 규격이다. 보통 메인 커넥터는 Version 2.0이라고 써진 규격을 사용한다. 여기서 녹색으로 마킹된 <dfn>PS_ON#</dfn> 을 COM, 즉 GND와 묶어 LOW 상태로 만들어야 파워가 작동한다. 그래서 이 <dfn>PS_ON#</dfn> 과 COM 사이에 토글스위치를 연결해 주었다.

그나저나.. 전선이 어마어마하게 많다. GND만 20가닥이고, 12V, 5V도 열몇 가닥씩은 된다. 다 합하면 거의 50가닥의 전선이 있다. 신나는 전선 피복 벗기기 노가다의 시작이다. 니퍼로 하나하나 피복을 까서 납을 먹이고 바나나잭에 납땜해 주면 된다.

<div class='center'><img src='{{page.assets}}/4.png'></div>

체험 삶의 현장 - 무한 납땜 편

각 전압별 출력 전류가 20A가 한참 넘어가므로 바나나잭에 연결할 때는 납을 들이부어 준다. AWG 전선 규격표에 따르면 30A의 전류를 흘려보내려면 전선 직경이 3.7mm는 되어야 한다. 땜질이 끝나면 케이블타이를 이용해서 전선을 깔끔하게 묶어 준다. -5V와 -12V는 잘 안 쓸 것 같아 말아서 안쪽에 넣었다. PWR_OK 라인도 전원 신호 라인으로 크게 필요하지 않으니 말아넣어 준다.

<div class='center'><img src='{{page.assets}}/5.png'></div>

여기까지 했으니 잠깐 뚜껑을 닫아서 잘 작동하는지 중간 점검을 한다. 파워 넣으면 들어오는 작동 LED 색깔이 예쁘다.

<div class='center'>
  <img src='{{page.assets}}/6.png' style='width: 30%'>
  <img src='{{page.assets}}/7.png' style='width: 30%'>
  <img src='{{page.assets}}/8.png' style='width: 30%'>
</div>

이제 USB포트와 핀헤더 등 다양한 출력 포트를 만들 차례다. USB포트의 경우 데이터 라인은 연결할 필요가 없고, 맨 끝의 전원 핀만 연결해 주면 된다. 그런데 철판인 파워서플라이 케이스를 잘라낼 방법이 마땅치 않다. 드릴로 구멍 뚫고 줄톱을 집어넣으면 잘리긴 하겠지만, 힘들고 무엇보다 절단면이 깔끔하지 않을 것 같았다. 종종 가는 경기중소벤처기업청 시제품제작터에 있는 금속레이저커터로는 잘릴 것 같았지만, 연구원 분께서 주석 섞인 합금이라 안 될 것 같다고 하셨다. 그래서 그냥 만만해보이는 통풍구 쪽의 벌집 몇 개를 뜯어내기로 했다.

<div class='center'><img src='{{page.assets}}/9.png'></div>

적당히 사이즈 맞춰서 끼우고 사이에 아크릴 조각을 잘라다가 순간접착제로 고정시켰다.

<div class='center'><img src='{{page.assets}}/10.png'></div>

이 단자들도 메인 출력에서 선을 따서 연결해주면 된다.

<div class='center'>
  <img src='{{page.assets}}/main.png' style='width: 45%'>
  <img src='{{page.assets}}/11.png' style='width: 45%'>
</div>

바나나잭 단자와 작동 표시등에도 이름을 적어 준다. 영롱한 파란색 아주 맘에 든다.

<div class='center'>
  <img src='{{page.assets}}/12.png' style='width: 30%'>
  <img src='{{page.assets}}/13.png' style='width: 30%'>
  <img src='{{page.assets}}/14.png' style='width: 30%'>
</div>

이제 제대로 작동하는지 확인해 본다. 12V 라인이 약간 모자라게 나오는 것은 5V 라인에 저항을 걸어 주면 해결된다고 한다. 부하 걸면 전압이 좀 떨어질 테니 조금 높게 나오는 것은 문제없어 보인다. 

<div class='center'><img src='{{page.assets}}/15.png'></div>

핀헤더 출력도 바나나잭 쪽과 완벽히 똑같게 나온다.

<div class='center'><img src='{{page.assets}}/16.png'></div>

USB 출력 포트가 네 개나 돼서 이것저것 한번에 많이 돌릴 수도 있다. 한 방에 작동이 잘 되니 만족스럽다.