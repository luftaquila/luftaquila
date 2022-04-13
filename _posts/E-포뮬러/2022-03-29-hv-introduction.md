---
title: E-포뮬러 전기시스템 제작기
description: 1. HV 시스템 개요
category: e-formula
assets: /assets/posts/e-formula/2022-03-29-hv-introduction
image: /assets/posts/e-formula/2022-03-29-hv-introduction/main.png
layout: post
---
### 목차
<div style="margin-left: 2rem;">
<ol>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/introduction/">들어가며</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/hv-introduction/">HV 시스템 개요</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/lv-introduction/">LV 시스템 개요</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/hv-detail/">HV 시스템 세부사항</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/lv-detail/">LV 시스템 세부사항</a></li>
</ol>
</div>
<br>

### HV 시스템 개요
<div class='center'><img src='{{ page.assets }}/main.png'></div>
HV 시스템의 목적은 모터를 구동하기 위한 전력을 차체 내에 비축하고 있다가, 필요할 때 모터에 전달하기 위한 것이다. 간단하게는 배터리 팩과 모터 컨트롤러(인버터), 모터로 구성된다. 여기에 방전 회로, HVD 등이 추가로 붙는다. 사용하는 모터에 따라 150~600V의 고전압을 사용하며 무슨 일이 있어도 LV와 완벽하게 절연되어 있어야 한다. 여기서는 각 구성 요소와 함께 알아야 할 개념에 대해서만 간단하게 설명하고, 회로와 함께 각 요소를 설계하는 것은 나중에 보다 상세하게 알아보도록 하자.

#### 1. 고전압 배터리 팩
고전압 배터리 팩은 모터를 구동하는 데 필요한 에너지를 저장하기 위한 것으로 여러 구성 요소를 포함하고 있다. 배터리 팩 내부의 몇 가지 요소(TSAL 등)은 반드시 배터리 팩 안에 있어야 하는 것은 아니다. 각 팀의 선택에 따라 배치하면 된다.

##### 1. 고전압 배터리
전기자동차의 배터리는 리튬이온 전지를 사용한다. 우리는 삼성SDS의 `INR-21700-40T` 셀 490개를 사용한다. 고방전 배터리인 만큼 배터리는 충분히 잘 냉각되어야 한다. 제작에 도움이 될 리튬이온 전지에 대한 몇 가지 사실은 다음과 같다.

1. 리튬이온 전지의 전압은 완전 충전 시 4.2V, 완전 방전 시 2.7~3.3V이다. 통상 3.7V의 전압을 가진다. 완전 방전 전압은 배터리 관리 시스템(BMS)이나 배터리 보호회로(PCM)가 정한다. 완전 방전에 가깝게 방전할수록 배터리 음극이 영구적인 손상을 입어 배터리의 수명과 용량이 조금씩 감소한다.

1. 배터리의 용량을 나타내는 단위는 mAh 혹은 Ah를 사용한다. *(밀리)암페어시* 라고 읽으며 한 시간동안 흘려줄 수 있는 전류의 양을 의미한다. 배터리 용량이 2,000mAh라면 2A의 전류를 한 시간동안 흘려줄 수 있다는 뜻이다.

1. 동일한 배터리를 직렬로 연결하면 배터리의 전압은 두 배가 되지만 용량은 그대로다. 반면 병렬로 연결하면 전압은 그대로지만 용량과 흘려줄 수 있는 전류는 두 배가 된다. 배터리 세그먼트를 몇 개의 직렬과 병렬로 구성했는지는 70s7p와 같이 표현한다. 이는 70개의 직렬(serial) 연결, 7개의 병렬(parallel) 연결로 구성되었다는 뜻이다. 따라서 총 사용한 셀 개수는 490개가 된다.  

<blockquote style='font-size: 0.9rem'>
여기서 잠깐 우리의 배터리 `INR-21700-40T`의 간단한 스펙을 살펴보자.
<div class='center'>
<table>
<tr><th>specification</th><th>value</th></tr>
<tr><td>capacity</td><td>4,000mAh</td></tr>
<tr><td>discharge current</td><td>35A</td></tr>
<tr><td>weight</td><td>70g</td></tr>
</table>
</div>
병렬로 7셀을 연결하였으므로 우리의 배터리 용량은 4,000 &times; 7 = 28,000mAh = <dfn>28Ah</dfn> 이다. 전류는 35 &times; 7 = <dfn>245A</dfn>이며 이 값은 셀이 손상 없이 연속적으로 흘려줄 수 있는 전류를 의미한다. 배터리 전압은 직렬로 70셀을 연결하였으므로 만충 시 최대 70 &times; 4.2 = <dfn>294V</dfn> 이다.  
<br>
한편, 배터리 모델의 21700이라는 숫자는 직경 21mm, 높이 70mm의 원통형(0) 셀이라는 의미다. 18650 규격이 가장 보편적으로 사용된다.
</blockquote>

##### 2. 배터리 관리 시스템 BMS(Battery Management System)
리튬이온 전지는 굉장히 높은 에너지 밀도를 가지고 있다. 에너지 밀도가 높다는 것은 불안정하다는 것이다. 뉴스에서 리튬이온 전지 화재 사고를 본 적이 있을 것이다. 특히 여러 셀을 직렬/병렬로 연결한 경우에는 셀마다 충전량이 달라지는 상황이 생길 수 있다. 특정 셀이 다른 셀보다 더 많이 충전되고 더 많이 방전된다면 이는 과충전, 과방전으로 이어져 화재 등 여러 문제를 일으킬 수 있다. 이를 막기 위해 배터리 셀을 감시하며 셀 밸런싱, 과충전 방지, 과방전 방지, 과열 방지, 과전류 방지 등의 기능을 하는 것이 BMS이다. 우리 팀은 *Orion* 사의 *Orion BMS 2* 모델을 사용한다.

##### 3. 메인 HV 릴레이 AIR(Accumulator Isolation Relay)
고전압을 사용하는 만큼 배터리팩은 사용하지 않을 때 적절히 꺼질(외부와 절연될) 필요가 있다. 이를 위해 배터리의 양 극에 릴레이를 붙여 +/- 각 극을 독립적으로 개폐할 수 있도록 하는 것이 AIR이다. +/- 단자를 끄고 켜는 스위치라고 생각하면 된다.

<blockquote style='font-size: 0.9rem'>
릴레이는 전기로 동작하는 스위치이다. 
<div class='center'><img src='{{ page.assets }}/1.png'></div>
릴레이 아래의 코일에 전압을 가해 주면 코일은 전자석이 되어 접점을 끌어당긴다. 따라서 접점은 아래쪽 단자와 붙어 전기적으로 연결된다. 전압을 끊으면 스프링에 의해 점점은 원래 자리로 돌아가게 된다. 사람의 손 대신 전기 신호(전압)을 이용해 접점을 개폐하는 스위치라고 생각하면 편하다.
<br>
릴레이에는 NO와 NC 타입이 있다. SPDT 릴레이의 경우 NO와 NC 단자가 둘 다 있다. 위 예시 사진이 두 단자를 모두 가지고 있는 형태이다. NO 단자는 Normally Open으로, 전압을 가하지 않은 상태에서 열려 있어 전기가 흐르지 않으며 전압을 가하면 회로가 닫힌다. 반대로 NC 단자는 Normally Closed이며 평소에 닫혀 있다가 전압을 가하면 열리게 된다.
</blockquote>

##### 4. 초기 충전 회로 Precharge Circuit
모터를 제어하는 모터 컨트롤러는 회로에 커패시터(축전기)를 가지고 있다. AIR를 닫아 HV 배터리의 전압을 모터 컨트롤러에 공급하면 이 축전지들은 0V로 방전된 상태에서 갑자기 300V에 가까운 전압을 공급받게 된다. AIR가 닫히는 순간 높은 전압차로 인해 큰 돌입 전류가 흐르게 되며, 이는 모터 컨트롤러를 손상시킬 수 있다. 따라서 AIR를 닫기 전 미리 모터 컨트롤러의 축전기들을 배터리 전압의 95% 정도로 서서히 충전한 후에 AIR를 닫음으로써 돌입 전류로 인한 손상을 방지해야 한다. 이 역할을 하는 것이 초기 충전 회로이다.

##### 5. 절연 감시 장치 IMD(Isolation Monitoring Device)
HV 시스템은 LV 시스템과 완벽한 절연을 유지해야 한다. 만약 절연이 제대로 유지되지 않으면 탑승자는 차체 프레임에 접촉하는 것만으로도 HV와 같은 그라운드를 공유하여 감전될 위험이 있다. IMD는 HV 시스템과 LV 시스템 간의 저항값 등을 측정하여 적절한 절연을 유지하고 있는지 감시하는 장치이다. 대회 측에 의해 모델이 정해져 있으며 *Bender*사의 ISOMETER IR155-3204를 사용한다.

##### 6. 고전압 표시 장치 TSAL(Tractive System Active Light) & 전압 표시계 VI(Voltage Indicator)
TSAL은 현재 차량에 어떠한 전기 시스템이 활성화되어 있는지를 표시하는 장치이다. LV가 활성화될 경우 녹색 LED를 점등하며 HV까지 활성화되면 적색 LED를 점등한다. 이 LED들은 소프트웨어를 통해 HV의 상태를 추정하여 점등되어서는 안 되며, 직접 HV의 전압을 감지하여 점등되어야 한다.  
TSAL이 차량 주변 어디에서나 볼 수 있도록 차량 상단에 부착되는 반면, VI는 배터리 팩 자체에 부착되어 배터리 팩의 활성화 상태를 표시한다. TSAL처럼 HV/LV를 구분하지는 않고 HV가 활성화되어 있을 때 LED를 점등한다. 
<br>

#### 2. 모터 컨트롤러와 모터
AC(교류) 모터는 DC(직류) 모터에 비해 구조적으로 유리하여 동급 출력에서 보다 저렴하고 수명이 길며, 효율이 좋다. 이러한 이유로 우리의 전기차 또한 AC 모터를 사용한다. 반면, 우리의 배터리 팩은 직류이다. 따라서 모터를 구동하기 위해 배터리의 DC를 AC로 변환해야 할 필요가 있다. 이를 인버터라고 한다. 이 인버터에 차량 전용으로 속도 제어, CAN 통신, 릴레이 제어 등 다양한 기능을 추가한 것이 모터 컨트롤러이다. 우리는 *CASCADIA MOTION*사의 PM100DX 모델을 사용한다.

#### 3. 방전 회로
앞서 초기 충전 회로에서 설명한 것처럼, 모터 컨트롤러는 커패시터로 인해 정전용량 성분을 가지고 있다. 이 커패시터들은 AIR가 열려 HV가 끊겨도 300V로 충전되어 있다. 방전 회로는 이 잔류 고전압을 제거하기 위한 것이며, 릴레이와 저항으로 구성되어 있다.

#### 4. 고전압 분리기 HVD
우리는 배터리의 각 단자를 AIR를 통해 제어한다. 그런데 우리는 AIR에 모종의 문제가 생겨 AIR 전원을 끊어도 HV 회로가 열리지 않고 닫힌 상태를 유지하는 상황을 생각해 볼 수 있다. 이러한 예상치 못한 상황에서 HV 배선을 직접 물리적으로 끊어 구동 시스템 전원을 차단할 수 있도록 하는 플러그가 바로 HVD이다. 복잡한 회로 없이 단순하게 잘 절연된 플러그와 HVD의 분리를 감지하기 위한 인터락으로 구성된다.

#### 5. 에너지 미터 & 구동시스템 전압 측정 포인트 TSMP(Tractive System Measuring Point)
에너지 미터는 대회 측에서 제공하는 장치이다. 주행 중 HV 전류와 전압을 측정해 규정된 최대 출력을 초과하지 않는지 감시한다. TSMP는 전기기술검사 시 구동시스템 전압을 측정하기 위한 단자로, HV 배선에 전류 제한 저항과 함께 연결되어 잘 절연된 바나나 잭이다.

<br>

### 목차
<div style="margin-left: 2rem;">
<ol>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/introduction/">들어가며</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/hv-introduction/">HV 시스템 개요</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/lv-introduction/">LV 시스템 개요</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/hv-detail/">HV 시스템 세부사항</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/lv-detail/">LV 시스템 세부사항</a></li>
</ol>
</div>