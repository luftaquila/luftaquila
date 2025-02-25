---
title: 6. 초기충전 회로
description: "E-포뮬러 제작기: HV 배터리 내부"
category: e-formula
assets: /assets/posts/e-formula/2023-09-01-precharge
image: /assets/posts/e-formula/2023-09-01-precharge/oscilloscope_tau.jpg
layout: post
---

### 안내

**본문은 포럼의 [6. 초기충전 회로](https://dnf.luftaquila.io/t/e-formula/27) 에서 읽으실 수 있습니다.**

{% include_relative notice.md %}

{% include_relative index.md %}

## 개요
초기충전 회로는 앞서 [1. HV 시스템 개요](https://luftaquila.io/blog/e-formula/hv-introduction/)에서 살펴본 것처럼 AIR+, AIR-를 모두 닫아 모터 컨트롤러에 HV를 본격적으로 공급하기 전에 컨트롤러를 서서히 충전하기 위한 것이다. 차량기술규정 제 51조는 AIR를 모두 닫기 전에 구동시스템 전압을 HV 전압의 90% 이상이 되도록 1초 이상의 시간 동안 초기충전할 것을 규정하고 있다.

컨트롤러는 정전 용량을 가지고 있어 HV 회로에서 용량성 부하로 작용한다. 컨트롤러는 팀별로 사용하는 회사와 모델이 다양하지만, 어느 컨트롤러나 마찬가지다. 컨트롤러 데이터시트를 보면 정전용량이 얼마인지 명시되어 있다.

<div class='center'><img src='{{ page.assets }}/pm100dx_cap.png'></div>

우리 팀이 사용하는 PM100DX의 정전용량은 440μF라고 한다. 실제로 측정해 보면 바로 알 수 있다.

<div class='center'><img src='{{ page.assets }}/cap_measure.jpg'></div>

440μF는 전자공학의 세계에서 꽤 큰 정전용량이다. 일부 모델은 1mF가 넘어가기도 하는데, 이러한 정전 용량은 일반적인 전자 회로에서는 구경하기도 힘들다. 거기다 전압이 구동시스템 전압이니 저장하는 에너지도 막대하다.

한편, 옛날옛적 고등학교 물리 시간에 배웠던 RC 회로를 떠올려 보자.

<div class='center'><img src='{{ page.assets }}/rc.png' style='width: 50%'></div>

스위치를 닫는 순간 <dfn>C</dfn> 는 전원 전압으로 충전되기 시작한다. 스위치를 닫은 직후인 <dfn>t = 0</dfn> 의 상황을 생각해 보자. 회로에는 전류가 흐르기 시작한다. 이 때 축전기는 전혀 충전되어 있지 않은 상태이므로 축전기 전압은 0V이다. 즉, 저항 R에 모든 전원 전압이 걸린다.

이 때의 전류 <dfn>I<sub>0</sub> = V<sub>R</sub> / R</dfn> 이다. 시간이 흐르며 축전지가 충전되면 전류는 감소한다. 시간에 따른 전류 <dfn>i = V / R * e ^ (-t / RC)</dfn> 이다. 뭐, 이 정도는 사실 필요 없다. 우리는 안전하게 컨트롤러를 충전하기만 하면 된다. 그래프로 그려보면 다음과 같다.

<div class='center'><img src='{{ page.assets }}/tau.gif' style='width: 70%'></div>

3τ 시간동안 충전하면 규정에서 정의하는 90% 이상 충전을 만족시킬 수 있다. 여기서 RC 시정수 <dfn>τ = R &times; C</dfn>이다.

## 초기 충전
이제 우리 HV 시스템을 한 번 추상화해보자.

<div class='center'><img src='{{ page.assets }}/rc_hv.png' style='width: 50%'></div>

위의 RC 회로와 완전히 똑같은 회로이다. 이제 HV 마스터 스위치를 켜서 AIR를 모두 닫는다고 생각해 보자. 이 때 회로의 저항 <dfn>R</dfn> 은 우리가 따로 설치한 것이 없으므로, 그저 HV 배선의 도선저항이 될 뿐이다.

우리 팀은 HV 배선에 50sq 전선을 사용한다. 50sq 구리 전선 1m의 도선저항은 0.336mΩ이다. 전원 전압은 구동시스템 전압인 294V이다. 자, 이제 회로의 초기 전류 <dfn>I<sub>0</sub></dfn>은 얼마일까? <dfn>294V / 0.000336 = 875000(A)</dfn>이다. 87만 암페어가 흐르는 회로에서 축전지는 진즉 숨을 거두었을 것이다. 여기서 축전지는 모터 컨트롤러의 HV 추상화 모델임을 잊지 말자. 우리는 방금 수백만 원짜리 컨트롤러를 잃고 몇 달의 추가 배송 기간을 얻었다.

이런 일을 막기 위해 우리는 R을 유의미한 값으로 달아준다. 이것이 초기충전 회로의 전부이다. 규정이 초기충전을 1초 이상 하라고 했으므로, 3τ는 1보다 커야 한다. 우리 컨트롤러가 440μF이니 대충 1kΩ를 달면 <dfn>τ = 0.44</dfn> 이 된다. 3τ면 1.32초이다.

<div class='center'><img src='{{ page.assets }}/precharge.png' style='width: 50%'></div>

이 때 초기 전류 <dfn>I<sub>0</sub></dfn> 을 다시 계산해보면 0.294A가 된다. 고작 300mA라니, 이 정도면 이제 안전하다.

그런데 이 회로에는 썩 마음에 들지 않는 부분이 있다. 바로 초기충전 저항 R이 회로에 계속 연결되어 있다는 것이다. 차량이 주행하는 중에도 R에는 계속 전류가 흘러 손실이 발생한다. HV라인에 80A가 흐르면 저항에서 나는 발열 <dfn>P = I<sup>2</sup>R = 6400(kW)</dfn>이다. 이 정도면 전기가 아까운게 문제가 아니라 저항이 불탄다.

따라서 초기충전 저항은 역할을 다하고 나면 회로에서 썩 꺼져줄 필요가 있다.

<div class='center'><img src='{{ page.assets }}/precharge_hv.png' style='width: 50%'></div>

처음 HV를 활성화하면 AIR+와 AIR-를 닫는 것이 아니라 PRECHARGE와 AIR-를 닫는다. AIR+는 열린 상태로 둔다. 구동시스템 전압이 충분히 충전될 만큼의 시간이 흐르거나, 실제로 전압을 측정해 원하는 수준에 다다르면 AIR+를 닫는다. 그리고 PRECHARGE를 열면 초기충전이 깔끔하게 완료된다. PRECHARGE에는 적당한 정격 전류를 갖는 범용 릴레이를 사용하면 된다. 우리 팀은 초기충전과 방전을 포함한 대부분의 고전압 또는 고전류 경로에 G2RL-1 DC12 릴레이를 사용했다.


## 릴레이 제어
여기서 PRECHARGE, AIR+, AIR-를 어떻게 제어하는지는 팀의 구현에 따라 달라진다. 우리 팀이 사용하는 PM100DX는 알아서 초기충전을 수행한다. 컨트롤러에서 main contactor drive와 precharge contactor drive 디지털 출력이 나와서, 알아서 자기가 원하는 만큼 초기충전하고 AIR를 닫아 준다. 아주 간편하다.

<div class='center'><img src='{{ page.assets }}/oscilloscope_tau.jpg' style='width: 70%'></div>

실제로 우리 컨트롤러가 초기충전을 수행하는 모습이다. AIR+가 닫히며 구동시스템 전압이 HV 전압과 같아지는 지점이 보인다.

이러한 기능이 없다면 초기충전 제어 회로를 직접 구현해야 한다. 방법은 크게 두 가지가 있다. 3τ 만큼의 시간이 흐르도록 RC 충전 + 비교기(<del>초기초기충전</del>)회로나 타이머를 이용해서 시간지연을 일으킨 후에 AIR+를 닫는 방법과, VI처럼 구동시스템 전압을 비교기에 집어넣어서 원하는 수준 이상이 되면 AIR+를 닫는 방법이다.

## 저항 선정
초기충전 저항이 1kΩ면 된다지만 PCB에서나 쓰던 탄소피막저항 이런 거 가져다 쓰면 바로 저항이 터질 것이다. 저항을 쓰기 전에는 반드시 저항의 와트 수를 계산해 보아야 한다. 저항 선정에 관해서는 바로 다음 글인 방전 회로에서 다룰 예정이다. 초기충전이나 방전이나 사실상 동일한 회로의 RC 충방전이기 때문에 따로 설명할 이유가 없다.


{% include_relative index.md %}

</details>
