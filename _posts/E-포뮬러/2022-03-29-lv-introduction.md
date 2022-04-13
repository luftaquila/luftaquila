---
title: E-포뮬러 전기시스템 제작기
description: 2. LV 시스템 개요
category: e-formula
assets: /assets/posts/e-formula/2022-03-29-lv-introduction
image: /assets/posts/e-formula/2022-03-29-lv-introduction/main.png
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

### LV 시스템 개요
<div class='center'><img src='{{ page.assets }}/main.png'></div>
LV 시스템은 차량의 고전압 구동계통 외에 제어, 편의 등 다른 모든 전기 계통에 사용되는 저전압 시스템을 말한다. 상용 차량에서와 같이 차체 프레임에 접지되며 12V를 사용한다.

#### 접지
먼저 접지(혹은 그라운드)라는 것은 한 회로 시스템의 전압 기준점을 정하는 것이다. 전압은 종종 전기적인 위치 에너지로 표현된다. 어떤 물체의 위치 에너지는 <dfn>9.8mh</dfn>로 계산할 수 있다. 이 때, 높이 <dfn>h</dfn>을 알기 위해서는 높이의 기준점이 있어야 한다. 하늘을 나는 비행기의 고도는 해수면을 기준으로 재고, 책상 위에서 물리학 실험을 할 때에는 책상을 높이의 기준점, 즉 고도 0m로 잡는다.

전압 또한 마찬가지로 어떤 기준점 0V가 있어야 그 기준점과의 상대적인 전위차, 즉 전압을 잴 수 있다. 우리 LV 시스템의 전압 기준점은 12V 배터리의 -단자이다. 우리는 이 -단자를 차체 프레임과 전선으로 연결해 줌으로써 차체 전체를 우리 LV에 대한 기준점(0V)로 만들어 줄 수 있게 된다. 어디서든 배터리의 -극이 필요하면 차체를 가져다 쓸 수 있다는 말이다.

접지의 진정한 목적은 누설전류를 안전하게 처리하는 데 있다. 누설 전류는 전류가 본래 흘러야 할 전선 외에 다른 곳으로 흐르는 전류를 뜻한다. 누구나 한 번쯤 노트북이나 전기장판 표면에서 뭔가 찌릿한 느낌을 받아 본 적이 있을 것이다. 이것이 바로 누설 전류이다. 접지가 제대로 되지 않으면 이렇게 인간의 피부처럼 적절하지 않은 경로로 전류가 흐르게 된다.

일반적인 누설 전류는 미미하지만 전자제품의 수명을 단축시키고 인간을 기분나쁘게 한다. 한편, 무언가 잘못되었을 때 큰 누설전류가 흐르면 생명에 위협을 줄 수도 있다. 접지저항은 인체 저항보다 낮으므로 접지가 되었을 때 누설전류는 인체 대신 접지된 기준점으로 흘러 안전하게 처리된다.

접지는 또한 노이즈 안정성을 확보할 수 있게 해 준다. 모든 전기 회로는 약간씩의 의도치 않은 용량성(C) 혹은 유도성(L) 성분을 갖게 된다. 길이가 남는 전선을 정리하려고 돌돌 말아주기만 해도 코일이 되어 유도성 성분을 가져 전압이 일정하게 유지되는 것을 방해한다. 접지는 이러한 노이즈 성분을 제거해 줌으로써 전압을 보다 안정하게 유지할 수 있도록 해 준다.

접지를 섀시에 하는 것은 섀시가 자동차에서는 그나마 가장 전기용량이 크기 때문이다. 보통 건물에서 전기공사를 하면 접지는 땅에 한다. 자동차에서는 이것이 불가능하므로 프레임에 접지하게 된다.  
<br>
<hr>
<br>

#### 1. LV 배터리 
LV 시스템은 전원이 필요한 모든 곳에 사용된다. HV를 제어하는 BMS와 모터 컨트롤러조차 작동 전원으로는 12V LV를 사용한다. LV 배터리는 상용 차량에서는 납축 전지를 많이 사용하지만 우리는 HV 배터리와 똑같이 리튬이온 전지를 사용한다. 리튬이온 전지를 4s3p로 구성하여 13.2~16.8V의 전압을 12V DC-DC 컨버터를 통해 12V로 만들어 사용하게 된다.

#### 2. 차단 회로 Shutdown Circuit
LV는 배터리 팩 단자를 제어하는 AIR에 전원을 공급한다. LV 배터리에서 AIR로 가는 회로에는 여러 안전장치들이 직렬로 연결되어 있다. 그 중 하나라도 문제가 생겼을 때 차단 회로는 개방되어 AIR의 전원을 차단하게 된다. 차단 회로의 구성 요소는 다음과 같다.

##### 1. LV MASTER SWITCH
LV 메인 스위치 `LV MASTER`는 차단 회로 요소 중 LV 배터리와 가장 가까운 곳에 연결된 스위치이다. 이 스위치를 켜야만 모든 LV 시스템이 전원을 공급받는다.

##### 2. LATCHED CRITICAL RELAYS
BMS와 IMD, BSPD가 문제(FAULT) 신호를 발생시키면 차량의 HV 시스템은 정지해야 한다. 이 세 요소의 FAULT 신호로 작동하는 릴레이를 각각 하나씩 사용해 AIR 전원을 제어해 문제가 생기면 AIR를 차단한다.  

한편, 이 세 요소에 문제가 생겼을 때는 드라이버가 운전석에서 구동시스템을 재활성화할 수 있어서는 안 된다. 반드시 기술팀이 별도의 리셋 절차를 거쳤을 때에만 다시 HV를 활성화할 수 있어야 한다. 따라서 이 세 요소의 릴레이는 문제가 생겨 열렸을 때, LV가 끊겨 전원을 잃어도 같은 상태를 유지해야 한다. 이러한 이유로 latching 기능을 가진 릴레이를 사용하여, 별도의 리셋 버튼을 눌렀을 때만 재활성화될 수 있도록 한다.

##### 제동시스템 타당성 장치 BSPD(Brake System Plausibility Device)
BMS와 IMD는 HV 시스템 개요에서 설명하였으나, BSPD는 LV 시스템에 포함되므로 여기서 간략히 설명하고자 한다. 제동시스템 타당성 장치(BSPD, Brake System Plausibility Device)는 제동계통이 정상적으로 작동하는지 확인하는 장치이다. 브레이크 페달에 가해지는 압력과 모터에 전달되는 전력을 측정하여, 차량이 강한 제동을 함과 동시에 모터에 일정 수준 이상의 전력이 전달되면 차단 회로를 개방한다.

##### 3. HVD Interlock
<div class='center'><img src='{{ page.assets }}/1.jpg'></div>
HVD 인터락은 HV 시스템에서 설명한 HVD 커넥터에 포함된 작은 전기 접점이다. HVD 메인 배선이 실제로 HV 전선을 분리한다면, HVD 인터락은 이를 감지하여 차단 회로를 개방한다.

##### 4. 제동계통 미작동 감지 장치 BOTS(Brake Over-Travel Switch)
BOTS는 브레이크 페달 아래에 부착되는 작은 토글스위치이다. 정상 상태에서 브레이크는 적절한 유압 압력을 유지하여 페달이 끝까지 밟히지 않는다. 유압계통에 문제가 생겨 브레이크가 제대로 작동하지 않고 끝까지 밟힐 경우 해당 스위치가 눌리며 차단 회로를 개방한다.

##### 5. HV MASTER
HV 메인 스위치 `HV MASTER`는 사람이 수동으로 직접 작동시켜 AIR의 전원을 차단할 수 있는 스위치이다.

##### 6. HV AUX
HV 보조 비상정지 스위치 `HV AUX`는 HV MASTER와 같은 역할을 하는 스위치이다. 총 3개로, 운전석과 차량 좌우측에 하나씩 부착된다.

#### 3. 마이크로컨트롤러 MCU(Micro Controller Unit)
차량은 주행 가능 상태(RTD, Ready To Drive) 모드를 관리해야 한다. 차량은 HV가 활성화되었다고 가속 페달을 밟았을 때 모터가 바로 작동해서는 안 된다. 반드시 브레이크를 밟고 RTD 버튼을 눌러야만 RTD 모드가 활성화되며 주행 가능 표시음을 발신하고 모터가 가속 페달에 응답해야 한다.  

RTD 모드의 관리에 MCU를 사용한다. 이 외에도 MCU는 CAN 통신을 통해 BMS, 모터 컨트롤러 등 다양한 장치로부터 데이터를 수집한다. 수집한 데이터는 SD카드에 저장하여 이후 분석에 사용하거나, 드라이버를 위해 각종 정보를 대시보드에 시현하는 데에 사용한다. MCU는 개발 편의를 위해 CAN 통신을 기본 지원하는 ARM 아키텍쳐의 STM32F 계열 코어의 개발보드를 사용한다.

#### 4. 등화장치 Lightings
브레이크 페달 작동 시 점등하는 제동등이다.

#### 5. 냉각 시스템 Coolings
모터 및 모터컨트롤러 인버터를 냉각시키기 위한 수랭 계통을 작동시키는 워터펌프와, HV 배터리 팩을 냉각하는 공랭 팬으로 구성된다.

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