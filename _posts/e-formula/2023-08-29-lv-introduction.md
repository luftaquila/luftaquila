---
title: 2. LV 시스템 개요
description: E-포뮬러 전기시스템 제작기
category: e-formula
assets: /assets/posts/e-formula/2023-08-29-lv-introduction
image: /assets/posts/e-formula/2023-08-29-lv-introduction/lv.jpg
layout: post
---

### 안내

**본문은 포럼의 [2. LV 시스템 개요](https://dnf.luftaquila.io/t/e-formula/23) 에서 읽으실 수 있습니다.**

{% include_relative notice.md %}

{% include_relative index.md %}

## LV 시스템 개요
LV 시스템은 차량의 고전압 구동계통 외에 제어, 편의 등 다른 모든 전기 계통에 사용되는 저전압 시스템을 말한다. 상용차와 같이 차체 프레임에 접지된 12V를 사용한다. LV 배터리와 차단 회로, RTD, 제동등, 냉각 계통 및 마이크로컨트롤러(MCU) 등으로 구성되어 있다.

### 1. LV 배터리
사실상 LV 시스템은 HV 계통을 제외한 모든 전기 계통을 말한다. HV를 제어하는 BMS와 AIR, 모터 컨트롤러조차 작동 전원으로는 LV를 사용한다. 상용 차량은 납축 또는 인산철 배터리를 많이 사용하지만 이러한 배터리는 크고 무겁다.

우리는 HV 배터리처럼 리튬이온 전지를 4s3p 구성으로 묶어 공칭 14.4V, 최대 16.8V를 내는 [제품](https://batteryworld.co.kr/product/kc%EC%9D%B8%EC%A6%9D-%EB%A6%AC%ED%8A%AC%EC%9D%B4%EC%98%A8-18650-%EB%B0%B0%ED%84%B0%EB%A6%AC%ED%8C%A9-144v-10050mah-35e-4s3p/2444/category/26/display/1/)을 LV 배터리로 사용한다. LV 배터리는 반드시 보호회로를 내장하여 단락 사고로부터 보호받아야 한다.

예전에는 이 전압을 DC-DC 컨버터를 통해 정확히 12V로 만들어 차량에 공급했으나 이는 잘못된 설계였다. LV의 각 구성요소는 12V가 아닌 LV 최대 전압에서도 문제없이 작동할 수 있는 부품들로 구성되어야 하고, LV 전원은 항상 12V보다 최소 1V 이상 높은 전압을 유지할 수 있어야 한다. 이에 대한 자세한 내용은 [½. 리빙 포인트](https://luftaquila.io/blog/e-formula/living-point/)의 *2-6. LV 전원과 전압 강하* 를 참고하기 바란다.

### 2. 차단 회로 (Shutdown Circuit)
우리의 궁극적인 목적은 차량의 주행이다. 차량이 주행하려면 모터 컨트롤러가 HV 전원을 공급받아야 한다. 즉, HV가 활성화되어야 한다. 이전 글에서 알아본 것처럼 HV가 활성화되기 위해서는 두 AIR가 모두 전원을 공급받아 접점을 닫아 주어야 한다.

요약하면 차량이 주행하려면 AIR를 닫아야 한다는 말이다. AIR가 열고 닫는 접점부는 HV이지만, AIR를 제어하는 코일 전원은 LV이다. LV 배터리와 AIR를 연결해 놓기만 하면 차량은 HV를 공급받아 주행할 수 있게 된다.

그러나 차량이 아무 때나 시동이 걸려 있으면 상당히 곤란하다. 특히 학교 한구석에서 대학생들이 직접 뚝딱뚝딱 만든 차량에 고전압이 흐를 때는 더욱 그렇다. **차량은 우리가 의도했을 때에만, 그리고 상태가 멀쩡할 때에만 HV를 공급받아야 한다.** 이 기능을 수행하는 것이 차단 회로이며, 차량 전기시스템의 핵심이다.

차단 회로는 LV 배터리와 AIR 전원 사이에 많은 차단 구성 요소를 직렬로 끼워넣는다.

<div class='center'><img src='{{ page.assets }}/shutdown.png'><br>클릭하면 확대할 수 있다.</div>

그냥 이게 전부다. LV 배터리로 AIR 두 개를 켜는 건데, 그 사이에 낀 사공이 많을 뿐이다. 그 중 하나라도 작동하면 회로가 끊기고 AIR는 떨어진다. 이제 구성 요소를 하나씩 알아보자.

#### 2-1. LV 마스터 스위치
위 그림을 보면 알 수 있는 것처럼, LV 마스터 스위치는 LV 배터리와 가장 가까운 곳에 존재한다. 이 스위치를 켜면 `LV` 라고 표시된 지점이 전원을 공급받게 된다. 여기에 연결된 많은 저전압 부품들(MCU, TSAL 등)이 작동하기 시작한다. 따라서 TSAL도 녹색으로 점등될 것이다. 배터리 팩에도 LV 전원이 공급되어 BMS가 켜지고 IMD가 절연 감시를 시작한다.

#### 2-2. HV 마스터 스위치
위 그림에서 LV, HV 마스터만 다른 스위치들과 모양이 다른 것에 주목하자. 마스터 스위치들은 작동시키면 접점이 붙는 구조이다. 반면 다른 구성요소들은 작동시키면 접점이 떨어진다. 이들은 평소에는 회로를 연결해 놓고 있다가, 문제가 생기면 작동해 회로를 끊어놓는 부품들이다.

다른 구성요소들이 전부 정상 상태일 때, HV 마스터 스위치를 켜면 AIR가 전원을 공급받는다. HV는 차량으로 공급되고, TSAL, VI가 적색으로 점등된다. LV 배터리를 아끼기 위해 HV가 활성화될 때만 켜져도 되는 LV 구성요소들(냉각 계통 등)도 HV 마스터 스위치 뒤에서 전원을 공급받으면 된다.

#### 2-3. 제동장치 미작동 감지 장치 (BOTS, Brake Over-Travel Switch)
위 그림에서 BOTS부터 HVD 인터락까지 구성 요소들의 순서는 그렇게 중요하지 않다. 뭐 하나만 꺼져도 어차피 AIR가 떨어지기 때문이다. 그래도 순서대로 하나씩 알아보자.

<div class='center'><video controls><source src='{{ page.assets  }}/bots.mp4' type='video/mp4'></video></div>

BOTS는 브레이크 페달에 달린 토글 스위치이다. 브레이크를 끝까지 밟으면 페달 축이 토글 스위치를 건드려 끌 수 있도록 되어 있다. 브레이크에 압력이 정상적으로 잡혀 있을 때는 절대 사람 힘으로 밟을 수 없는 위치에 있다. 라인에 압력이 빠졌거나 공기가 차서 제동이 불가능한 상황일 때, 드라이버가 브레이크를 밟으면 페달이 쑥 눌리고 이 스위치를 건드려 HV를 차단한다.

#### 2-4. HV 보조 비상정지 스위치
차량의 양 옆과 운전석에 하나씩 존재해야 하는 보조 비상정지 스위치이다. 평소에는 연결된 상태를 유지하다가 간단하게 누르기만 하면 회로를 끊어 놓는다. 차량기술규정에 크기와 형태가 정해져 있다.

<div class='center'><img src='{{ page.assets }}/switch.jpg'></div>

맨 위에 있는 빨간색 동그라미가 보조 비상정지 스위치다. 빨간색 키가 꽂힌 스위치 중 위쪽에 있는 것이 LV 마스터, 아래쪽이 HV 마스터 스위치이다. 차량기술규정에 의해 LV, HV 마스터 스위치는 키를 돌려 켜는 방식이어야 하고, 키를 분리할 수 있어야 한다.

#### 2-5. FAULT 래칭 시스템
그림에서 IMD, BMS, BSPD라고 적힌 요소가 보조 비상정지 스위치와 다르게 생긴 점에 주목하자. 이 스위치들은 다른 구성요소처럼 사람이 작동하는 스위치가 아니다. 그저 회로도에 간단하게 표시할 수 있게 추상화했을 뿐, 이 요소들은 회로의 전기적 신호에 의해 작동한다.

차량기술규정에 따라 IMD, BMS, BSPD가 문제를 감지해 차단 회로를 개방하면 HV가 재활성화돼서는 안 된다. LV까지 껐다가 켜더라도 HV를 활성화할 수 없어야 한다. 반드시 기술팀이 별도의 리셋 절차를 거쳐야만 HV가 활성화되어야 한다.

이러한 동작을 가장 십게 구현할 수 있는 것은 래칭 릴레이이다. 래칭 릴레이는 공급 전원이 끊겨도 마지막 상태를 유지한다. set 코일과 reset 코일을 각각 가지고 있는 2-coil 래칭 릴레이와 한 코일로 set, reset을 모두 수행하는 1-coil 래칭 릴레이가 있다.

래칭 릴레이는 흔하게 사용하는 릴레이가 아니기 때문에 다소 비싸다. 우리 팀은 처음에는 PANASONIC의 ADJ14012를 사용했는데, 개당 15,000원이 넘는다. 세 개의 래칭 릴레이가 필요하니 릴레이 값만 5만 원 가까이 된다. 지금은 TE의 [RT424F12](https://www.eleparts.co.kr/goods/view?no=3978016)를 사용하고 있다. 그나마 저렴한 개당 4천 원 정도에 신뢰성 있게 동작한다.

래칭 릴레이는 그 내부 구조가 복잡한 만큼 가끔 오동작을 일으킨다. 아마 릴레이 내부에서 상태가 꼬이는 듯하다. 리셋 버튼 외에도 다른 확실한 수동 리셋 수단을 갖추는 것을 추천한다. 가끔 리셋 버튼을 눌러 리셋 코일에 전류를 흘려도 리셋이 안 될 때가 있는데, 회로에 직접 점퍼선으로 12V를 걸면 리셋이 된다. 미리 방법을 강구해놓지 않으면 기판을 차에서 통째로 분리해 리셋하고 다시 장착해야 한다.

<div class='center'><img src='{{ page.assets }}/latch.jpg'><br>이런 불상사가 일어날 수 있다.</div>

#### 2-6. HVD 인터락
HVD 인터락에 대해서는 이미 이전 글의 HVD 항목에서 설명했다. 해당 인터락이 직접 AIR  전원을 끊도록 하여 HVD 분리 시 차단 회로가 끊어질 수 있도록 해야 한다.

<br>

### 3. 제동시스템 타당성 장치 (BSPD, Brake System Plausibility Device)
BSPD는 쉽게 말하면 급발진 상황을 감지하고 차단 회로를 개방하는 장치이다. 운전자가 강한 제동을 하고 있는 중에 모터에 5kW 이상의 전력이 전달되는 상황이 0.5초 이상 지속되면 급발진 상황이라고 간주하고 HV를 비활성화한다. 모터에 전달되는 전력을 감지하기 위해 HV 배선에 장착된 홀 센서와 강한 제동을 감지하기 위한 브레이크 레일 압력 센서로부터 입력을 받아 작동한다.

차량 검차 시 BSPD의 작동을 검증하기 위해 차량의 구동륜을 지면에서 띄워 놓은 상태에서 브레이크와 엑셀을 동시에 밟아 보라고 한다. 만약 이것이 불가능할 경우 사전에 미리 BSPD가 작동하는 상황과 같은 조건을 설정하여 BSPD의 작동을 검증하는 영상을 검차 시 제출해야 한다.

### 4. 주행 가능 상태 (RTD, Ready-To-Drive)
차량기술규정에 따라 차량은 HV를 인가했다고 바로 주행 가능한 상태가 되어서는 안 된다. 반드시 RTD라는 한 가지 절차를 더 거쳐 주행 가능한 상태로 진입해야 한다. 이 RTD를 활성화하기 전까지는 HV가 활성화되어 있더라도 엑셀을 밟았을 때 모터가 굴러서는 안 된다.

소프트웨어 제어를 허용하지 않는 TSAL, VI 등 다른 많은 구성 요소와는 다르게 소프트웨어 제어에 대한 별도의 제약이 없다. 따라서 MCU를 이용한 RTD 상태 통제가 가능하다. RTD를 활성화하면 차량은 RTDS라고 하는 신호음을 1~5초간 발신해야 한다. 검차 시 규정에 따라 차량 주변 1m 거리에서 80dBA 이상의 소리가 나는지 음향 검사를 한다.

### 5. 제동등
브레이크 페달 작동 시 점등하는 차량 후미의 제동등이다.

<div class='center'><img src='{{ page.assets }}/brake.jpg'></div>

### 6. 냉각 시스템
이미 이전 글인 HV 시스템에서 300V DC-DC 컨버터를 통한 냉각 시스템에 대해 언급한 바 있다. 이러한 컨버터를 사용할 여건이 되지 않는다면 LV 배터리로 냉각 계통을 작동시키는 수밖에 없다. 다 합치면 12V 10A 정도는 기본으로 사용하는 전기 먹는 하마들이다.

### 7. 마이크로컨트롤러 (MCU, Micro Controller Unit)
MCU는 주행에 필수적인 요소는 아니다. 하지만 차량을 처음 굴리고 나면 반드시 데이터 분석에 대한 필요성을 느끼게 된다. 차량이 실제로 HV를 얼마나 끌어다 쓰는지, 최대 토크는 얼마나 내는지 등을 파악하고 문제를 해결하려면 데이터로깅이 반드시 필요하다.

대부분의 모터 컨트롤러와 BMS는 CAN 통신을 통해 서로 정보를 주고받고, 그 외에도 자신에 대한 많은 정보를 CAN 버스에 broadcasting한다. CAN 버스에 낀 MCU가 이 메시지들을 모니터링하면 주행 중에 무슨 일이 일어났는지 파악할 수 있게 된다.

그러나 데이터로깅을 정말 실제 활용이 가능한 수준으로 구현하려면 많은 노력이 든다. CAN 버스를 모니터링해야 할 뿐 아니라 수신한 값을 나중에 확인할 수 있도록 SD카드 등에 저장해야 하고, 언제 수신한 데이터인지 확인하려면 RTC 시계 등을 이용해 시간 정보를 유지할 수 있어야 한다. 또한 수십만 개씩 기록된 로그에서 오류가 난 로그는 제거하고 원하는 값만 찾아서 시각화하는 것 또한 상당히 번거로운 일이다. 매 주행마다 SD카드를 분리하여 데이터를 뽑아내기도 현실적으로 어려움이 많다.

이러한 문제점을 해결하고자 이번에 차량 주행 데이터 분석 및 원격 모니터링 시스템을 개발하였고, 기술부문 기술아이디어에 제출하여 금상을 받았다. 죽어라 만들었는데 우리 팀이 올해 한 번 쓰고 말면 아까우니 하드웨어 설계도와 제작 방법, 소스코드 등을 모두 [공개](https://github.com/luftaquila/monolith)해 두었다. 자세한 내용은 마지막 글인 [모노리스 DIY 데이터로거](https://luftaquila.io/blog/e-formula/monolith-telemetry-datalogger/)를 참고하면 된다. 널리 유용하게 사용되기를 바란다.

{% include_relative index.md %}

</details>
