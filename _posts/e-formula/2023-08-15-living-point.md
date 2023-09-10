---
title: ½. 리빙 포인트
description: KSAE E-Formula 전기시스템 제작기
category: e-formula
assets: /assets/posts/e-formula/2023-08-15-living-point
image: /assets/posts/e-formula/2023-08-15-living-point/main.jpg
layout: post
---

{% include_relative index.md %}

## 대회 끝
처음엔 가벼운 마음으로 시작한 자작차였는데 어느덧 꼬박 2년을 쏟아 부었다. 처음 전기차에 도전하는 팀에서 밑바닥부터 공부해 회로를 설계하고 직접 만들면서 정말 눈물겨운 삽질을 수도 없이 해야 했다. 한 개 고치면 세 개가 새로 튀어나오는 치명적인 설계 결함들로 날밤을 샜던 걸 떠올리니 치가 떨린다. 만능기판 대신 예쁘게 만드려고 뜬 PCB는 결국 뜯어내고 새로 연결한 부품들로 만신창이가 됐다.

<div class='center'><img src='{{ page.assets }}/pcb.jpg' style='width: 90%'></div>

차량의 12V LV 계통, 12V를 맞으면 타버리는 작고 소중한 논리 소자들, 전선이 소시지만한 300V HV 세 개가 한 기판에 어우러져야 한다. 기본적인 PCB 설계나  풋프린트부터 절연까지 고려해야 할 온갖 요소가 정말 산더미인데 놀랍게도 아무도 우리에게 단 하나도 알려주지 않았다.

<div class='center'>
  <video controls>
    <source src="{{ page.assets }}/삽질.mp4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
  </video>
  <br>인생에 참 한번에 마음대로 되는게 하나도 없다.
</div>

그러한 이유로 이후에 새로 입문하고 도전하는 사람들에게 전해주고 싶은, 2년동안 피와 땀과 돈을 흘리며 얻은 리빙 포인트를 먼저 적어보려 한다.

# 리빙 포인트
### 0. 목차

1. 장비와 기술
    1. 장인은 장비를 따진다
    1. 납땜에 관한 팁
    1. 전기 배선에 관한 팁
1. 설계
    1. 자신이 설계한 회로를 절대 믿지 말자
    1. 쓰기 어려운 부품은 고르지도 말고, 고른 건 넉넉하게 구매하자
    1. PCB 주문 전에 꼭 풋프린트를 확인하자
    1. 처음부터 오버스펙 설계하지 말고 다 되면 나중에 개선하자
    1. 신호의 출처와 종류를 정확히 파악하자
        1. Floating과 LOW는 다르다
        1. Push-Pull, Open Drain과 Open Collector 회로
        1. 아날로그 신호
    1. LV 전원과 전압 강하
    1. 셀 내부 저항과 DCL
    1. 작고 반짝이는 건 언제나 옳다
1. 임베디드 프로그래밍에 관한 팁
    1. 메모리를 소중하게 생각하고 사랑하자
    1. Interrupt와 Polling
    1. UART는 느리고 문자열은 무겁다
    1. Brownout 대처
    1. 개발 생산성은 중요하다

### ½. 일정
대회 날짜를 목표로 차를 만들면 절대 일정을 맞출 수 없다. 대회 한 달 전 차량 구동을 목표로 작업해야 구동 과정에서 생기는 많은 문제들, 구동하고도 터지는 기상천외한 문제들에 간신히 대응할 수 있다.

그리고 반드시 대회 전에 [인스펙션 시트](https://www.ksae.org/jajak/bbs/?number=62012&mode=view&code=J_notice&keyfield=&keyword=&category=&gubun=)를 하나하나 확인하면서 직접 셀프 검차를 해 보아야 한다. 이 차는 반드시 검차에서 떨어뜨리겠다는 각오로 셀프 검차를 해야 대회장에서 무사히 모든 항목을 통과할 수 있다.

### 1. 장비와 기술
#### 1-1. 장인은 장비를 따진다
회로 설계하고 테스트할 때나 차량에 올리고 나서 문제 분석할 때 적절한 장비가 있으면 인생이 편해진다. 추천하는 장비 목록은 다음과 같다. 대개 알리에서 국내보다 훨씬 싸게 구할 수 있다.

1. 측정 장비<br>
휴대용 오실로스코프가 있으면 여기저기 유용하게 사용할 수 있다. 오실로까지는 어렵더라도 제대로 된 멀티미터는 반드시 필요하다. 요즘 세상에 알리에서 단돈 만 원이면 구할 수 있다. 더 싼 것도 대체로 기능은 제대로 작동한다. 마감과 사용성이 떨어질 뿐이다. 다만 카운트 수가 6000은 넘는 것을 추천한다.

2. 온도조절 인두기<br>
결국 납땜을 하게 될 텐데, 인두기 성능이 좋으면 인생이 편하다. 납땜 퀄리티는 굉장히 중요하다. 비숙련자가 작업하면 냉납이 나거나 쉽게 뜯어진다. 그리고 납 방울이 안 예쁘다(중요). 요즘에는 몇십만원 하는 하코 인두 아니어도 저렴하고 성능 좋은 온도조절 인두기가 많다. 추천하는 인두기는 다음과 같다. 둘 다 하코의 T12 팁을 사용한다. 제일 범용적이라 구하기 쉽고 교체가 편하다.<br>

    1. [T12-956](https://ko.aliexpress.com/item/4000201191923.html): 5만원 정도 하는 스테이션형 인두기다. 전원 올리면 작업 온도까지 올라가는데 몇 초밖에 안 걸린다. 성능 좋고 설정도 다양하다.
    2. [T12 휴대용 인두기](https://ko.aliexpress.com/item/1005005291695011.html): 2만 5천원 하는 인두기다. 펜 타입으로 뒤에 C타입 케이블을 꽂아 사용한다. 전원 공급은 USB PD 규격으로 공급받는다. 휴대형 인두기의 최대 단점이 가열이 느리다는 건데, PD 규격으로 충분한 전력을 공급받을 수 있게 됐다. 수많은 인두기를 써 봤지만, 한동안 1번 인두기 쓰다 팔아치우고 이걸로 정착해서 사용하고 있다.<br><br>
    **대회장에서는 전원 콘센트를 꼽을 수 있는 환경이 많이 부족하다.** 전기시스템 검차 때 뭔가 안 되는 것이 생기면, 10분만에 고칠 수 없으면 차를 빼서 패독에서 수리한 후 다시 줄을 서라고 한다. 우리는 TSAL 전선이 단선이 났었는데, 새로 납땜 한 번 하자고 패독까지 차를 끌고 가면 1시간은 우습게 날아간다. 대회장에서는 시간이 금이다. 5분 차이로 검차를 한번 더 받을 수 있는, 이벤트를 뛸 수 있는 기회가 날아간다. 콘센트 없이 납땜을 할 수 있다는 것은 대회장에서 엄청난 강점이다. 이 인두기는 PD 출력 지원하는 보조배터리만 있으면 빠르게 작업할 수 있다. 휴대폰 충전용 18W PD 보조배터리로도 20초면 가열된다. 강력 추천한다.

3. 기타 물품<br>
정밀한 롱노즈와 니퍼, 와이어 스트리퍼, 크림프 툴(커넥터 터미널 찝는 거), 핀셋, 납 흡입기, 솔더윅, 플럭스, 팁 클리너(철수세미), 품질 좋은 땜납 정도는 갖춰 주어야 작업이 수월하다. 인두 팁은 적당한 면적이 있는 팁(T12-K, T12-BC2)을 개인적으로 좋아한다.

#### 1-2. 납땜에 관한 팁
결국 경험에서 나오는 숙련도가 납땜 퀄리티를 만든다. 그래도 몇 가지 팁을 적어보면 이렇다.

1. 무연납 쓰지 말자<br>
땜납에는 무연납과 유연납의 두 종류가 있다. '연'은 납을 뜻한다. 그러니 무연납은 웃기지만 납이 없는 납이라는 뜻이다. 유럽에는 RoHS라는 전기/전자 제품에 납을 포함한 특정 유해물질의 사용을 제한하는 지침이 있다. 이 지침을 지키기 위해 납 없이 주석 합금으로 이루어진 무연납을 사용하는 것이다. 무연납은 녹는 온도가 훨씬 높고(보통 400도 이상에서 작업한다) 다루기 까다롭다. 여러분이 만든 자동차를 유럽으로 수출할 게 아니라면 유연납을 사용하는 것이 정신건강에 이롭다.

1. 온도가 중요하다<br>
온도가 낮으면 납이 안 녹고, 너무 높으면 납이 죽처럼 변한다. 온도가 낮아도 전선의 내열 온도보다는 훨씬 높기 때문에, 낮은 온도에서 오래 지지고 있으면 전선의 피복만 녹는다. 적정 온도에서 빠르게 필요한 부분만 가열해서 작업하는 것이 핵심이다. 대부분의 유연납은 320~340도에서 잘 녹는다. 이 정도에서 10도 단위로 온도를 조절해 가면서 잘 녹는 범위를 찾으면 된다. 온도조절이 가능한 인두기를 사야 하는 이유이다.

1. 납만 녹인다고 되는 것이 아니다<br>
땜납에 인두기를 갖다 대서 녹이고, 그걸 전선이나 PCB 패드에 올려놓는다고 납땜이 되는 것이 아니다. 납이 모재에 스며드려면 모재 또한 적절하게 가열되어 있어야 한다. 그렇지 않으면 녹았다가 굳은 납이 모재에 전혀 스며들지 않고 그 위에서 따로 놀게 된다. 납을 녹이기 전에 인두기로 전선이나 패드를 약간 가열시키고(1초 미만이면 충분하다), 그 상태에서 땜납을 공급해서 납땜을 하는 것이다.

1. 플럭스를 잘 사용하자<br>
플럭스는 납의 퍼짐성을 개선하는 화학 물질이다. 솔더 페이스트라고도 부르는 찐득한 고체 타입과 액체 타입이 있다. PCB에 사용할 때는 액체가 낫고, 전선에 작업할 때는 고체가 낫다. 여러분이 사용하는 땜납에는 플럭스가 같이 포함되어 있는데, 납을 녹이면 나는 하얀 연기는 이 플럭스가 활성화되면서 나는 연기이다(납땜 시 발생하는 연기에 납은 포함되어 있지 않다. 납의 끓는점은 1700도가 넘는다.). 건강에 좋지는 않다고 한다. 납이 죽처럼 변할 때 이 플럭스를 살짝 바르고 지지거나, 인두기를 플럭스에 아주 살짝 콕 찍고 사용하면 납이 물처럼 되어 방울 모양으로 예쁘게 굳는다. 이렇게 해야 납이 골고루 스며들어 냉납이 나지 않는다. 능숙한 작업자는 땜납에 들어있는 플럭스만으로도 대부분의 작업을 잘 해낸다. 너무 많이 사용하면 PCB를 오염시키지만, 필요할 때 적정량 사용하면 굉장히 도움이 된다.


#### 1-3. 전기 배선에 관한 팁

1. 전선<br>
배선 작업에는 UL1007 규격 전선을 추천한다. 일반 배선에는 22AWG를, 고전류 라인에는 18AWG를 쓰면 웬만한 경우는 다 커버한다. 다른 전선을 까딱 잘못 사면 피복이 너무 두꺼워서 터미널 찝어서 커넥터에 끼울 때 안 들어갈 수 있다.<br>
다만 UL1007은 대개 내열 온도가 80도이다. HV 배선에는 규정을 만족하지 못해 사용할 수 없다. 배터리박스 내부나 TSMP에 사용하는 얇은 HV 배선에는 UL AWM STYLE 11028 규격 전선이 적당하다.

2. 커넥터 시스템<br>
사용하는 커넥터의 종류를 미리 통일해놓지 않으면 이것저것 중구난방으로 사용하다 정말 중요한 순간에 커넥터가 호환이 안 되어서 피 볼 일이 생긴다. 커넥터 및 터미널을 최대한 적은 종류로 구매하는 것이 비용 측면에서도 더 유리하다.<br><br>
필요한 커넥터 종류를 대략 나열해 보면 다음과 같다.<br>

    1. Board to Wire 커넥터<br>
    PCB에서 전선을 뽑기 위해 사용하는 커넥터이다. 우리는 보편적으로 사용되는 Molex 5264/5267 시리즈를 사용했다. 값싸고 작고 사용하기 쉽다.

    2. 고전류 Board to Wire, 방수 없는 Wire to Wire 커넥터<br>
    5264/5267 시리즈는 18AWG 배선을 사용할 수가 없다. PCB에 18AWG 전선을 넣을 때나, 인클로저 내부의 방수가 필요 없는 wire to wire 배선에는 Molex Mini-Fit 시리즈를 사용했다.

    3. 차량 외부 Panel mount 커넥터<br>
    인클로저에서 나오는 차량 외부 배선에는 Amphenol LPT Series의 LPT06SE-14-19S/LPT02SE-14-19P 커넥터를 사용했다. 방수 되고 18-22AWG 지원하고 핀 많고 부피 작고 체결 쉬운 커넥터가 흔치 않다. 다른 더 좋은 커넥터 있으면 알려주시기 바란다. 가격은 꽤 비싼 편이라, 플러그와 리셉터클 한 세트가 터미널 값까지 합하면 12000원 넘게 나온다. 이전에는 Molex MX150 시리즈를 사용했는데, 부피는 큰데 체결에 힘이 많이 들고 핀 수가 적어서 교체했다. 값은 비싸지만 원형 커넥터가 더 예쁘다.

    4. 차량 외부 기타 커넥터<br>
    위에서 언급한 LPT 커넥터는 19핀 커넥터인데, 값이 비싸서 고작 2핀 필요한 자리에 사용하기에는 돈이 없었다. 인클로저와 개별 부품(제동등이나 TSMP 등)을 연결할 때는 2~3핀 정도면 충분하니 다른 방수 되는 조금 더 저렴한 커넥터를 사용하는걸 추천한다.

### 2. 설계

#### 2-1. 자신이 설계한 회로를 절대 믿지 말자
우리는 학부생 나부랭이다. 학교 회로 실험과목에서 이미 검증된 회로들만 만들어 보는 것과, 내가 필요한 입력/출력 신호만 가지고 회로를 부품까지 선정하며 설계해야 하는 실무 회로설계는 완전히 다른 문제다.

회로 설계를 기초부터 배운 것도 아닌데 우리는 일단 원하는 동작을 하는 회로 몇 개를 뚝딱 만들어야 한다. 당연히 처음 설계한 회로는 절대 곱게 작동하지 않는다. 개발된지 50년이나 지난 555 타이머도 내가 쓰면 안 되기 일쑤다. **회로의 모든 부품과 작동 원리를 이해하지 못한 상태에서 설계한 회로는 믿어서는 안 된다.**

설계한 회로의 검증은 철저하게 해야 한다. 아날로그 입력 두 개를 받아서 각각 전압이 특정 값 이상인지 확인하고, 두 전압 모두 특정 값 이상인 상태가 일정 시간 이상 유지될 때 디지털 출력을 내야 하는 BSPD를 예로 들어보자.
1. BSPD의 아날로그 입력 두 개(HV 홀 센서와 브레이크 압력 센서)는 각각 LM311 비교기로 들어가 별도로 설정된 기준 전압과 비교된다. 입력된 아날로그 신호가 기준 전압 이상이라면 HIGH가 LM311에서 출력된다. 빵판에 꽂아서 해봤더니 잘 된다. 오케이 다음.
2. 두 LM311의 디지털 출력은 2N3904 트랜지스터 두 개로 구성된 AND게이트로 들어가 두 LM311 출력이 모두 참일 때만 신호를 출력한다. 어 잘 되네?
3. 두 아날로그 입력에서 LM311을 통해 디지털 출력이 나오는지 따로따로는 테스트해 봤는데, 한 빵판에서 두 개 모두를 구현하기는 조금 번거롭다. <i>그냥 둘 다 조건을 만족하면 AND게이트에서 5V 디지털 출력이 나올 것이라 친다.</i>
4. 별도의 5V 파워 서플라이로 555 타이머 회로를 작동시킨다.
4. 타이머의 출력 핀도 5V를 출력할 테니, 여기에 MOSFET 하나를 붙여 스위칭을 해서 12V BSPD 디지털 출력을 만든다.
5. <b><u>다 됐겠지?</u></b> 설계한 회로로 PCB를 만든다.
6. 7일 걸려 PCB가 온다. 몇 만원치 부품들을 전부 올려 납땜하고 테스트해 본다.
7. 어림도 없지. 작동 안 한다.

회로가 처리해야 하는 일련의 동작들을 여러 부분으로 나누어 각각 테스트하고서 됐겠지? 하며 만족하면 절대 안 된다. 다 합쳐보면 제대로 작동하지 않는다. **될 거라 치고**는 경계해야 한다. 반드시...

555 타이머는 출력단 전압에서 1V 정도의 전압 강하가 일어난다. 5V를 전원으로 공급했다면 1V가 깎인 4V가 출력된다는 뜻이다. 타이머 뒷단의 MOSFET은 5V로는 작동하지만 4V는 문턱 전압에 아슬아슬하게 걸려 작동을 보장하기 어렵다. 타이머 출력은 5V가 나오겠지? 라는 안일한 마인드로 실제 타이머 출력 신호 대신 파워서플라이를 사용해 MOSFET을 테스트한다면 나중에 눈물을 흘리게 될 것이다.

회로 검증은 반드시 입력 신호, 출력 신호, 그리고 중간에 우리가 설계한 회로 전체. 이렇게 해야 한다. 중간에 우리가 만든 회로에서 무슨 일이 일어나는지는 모르겠고, 입력을 줬을 때 출력이 완벽하게 나오지 않는다면 다시 해야 한다. 우리가 설계한 회로는 PCB로 만들기 전에 반드시 회로 전체를 빵판에 구현해서 테스트해봐야 한다.
<br>

#### 2-2. 쓰기 어려운 부품은 고르지도 말고, 고른 건 넉넉하게 구매하자
여기서 쓰기 어렵다 함은 다음을 의미한다.
* 눈에 잘 보이지도 않는 쥐꼬리만한 SMD IC 등 납땜하기 어려운 부품들
* 비싼데 구하기도 힘들고 체결했다 분리하기 어려우며 툭하면 터미널이 뽑히는 커넥터들
* 기타 테스트하는데 많은 수고가 드는 일체의 부품들

우리는 BSPD 회로에 BD77501과 74LVC1G08GV이라는, 길이가 고작 3mm인 눈꼽만한 IC들을 포함시켰다. 문제는 회로라는 게 처음 설계가 절대로 완벽하게 작동하지 않는다는 것이다. 테스트하다 보면 회로에 5V 걸어야 하는데 실수로 12V 걸어서 연기가 퐁퐁 샘솟는 일이 하루가 멀다하고 생긴다.

죽은 부품을 교체하고 다시 테스트해야 하는데 부품이 카톡 알림 아이콘만 하다. 제거하고 다시 땜질하는데 20분이 걸린다. 몇 번 반복하면 PCB의 도금이 벗겨저 나가 납이 안 먹는다. PCB라면 차라리 낫다. 만능기판이라면 0.7mm 간격 다리에 에나멜선을 하나씩 달아줘야 한다.
<div class='center'><img src='{{ page.assets }}/main.jpg' style='width: 60%'><br>죽여줘...</div>

그러나 AND 게이트는 사실 이런거 안 써도 트랜지스터 두 개랑 저항 몇 개만 있으면 구현할 수 있다.

<div class='center'><img src='{{ page.assets }}/and_gate.png'></div>

납땜 어려운 부품 쓰지 말고 무조건 쉬운 부품으로 사용하자.

LM311 비교기, 2N3904/2N2222 범용 트랜지스터, AMS1117 레귤레이터, 12V 릴레이, LED 이런 것들은 개당 몇 백원, 몇 십원밖에 안 한다. 회로에 2개 들어가니까 여유롭게 5배수로 10개 사야지~ 하지 말고 그냥 최소 10배수로 구매하길 권장한다. 이런 부품은 100개씩 사도 만 원 정도밖에 안 한다. 테스트하면서 부품 죽고 다리 잘리고 교체하고 PCB를 통째로 새로 떠야 할 일이 허다하다. 부족해서 배송비 내고 새로 시켜서 기다리는 것보다 많이 사는게 천만 배 낫다.

#### 2-3. PCB 주문 전에 꼭 풋프린트를 확인하자
우리가 원하는 모든 회로를 PCB에 직접 설계해 올리기 어려울 때가 있다. RTDS를 위한 앰프 모듈 등이 그렇다. 이런 것들은 회로를 직접 설계하는 대신 모듈째로 헤더핀을 달아서 PCB에 올리곤 한다. 이 때, 꼭 실제 모듈 사이즈와 핀 위치, 번호를 실제로 확인한 후에 부품 풋프린트를 만들기 바란다. 실측하지 않고 그냥 인터넷에 굴러다니는걸 가져다 쓰면 꼭 실제와 달라 부품 간에 간섭이 일어나거나 제대로 작동하지 않고, 5만 원짜리 PCB를 새로 떠야 하는 불상사가 생긴다.

#### 2-4. 처음부터 오버스펙 설계하지 말고 다 되면 나중에 개선하자
**회로 소형화, 노이즈 저항성 강화, 진동에 잘 버티는 커넥터 등 개선 사항들은 일단 회로가 작동이 되면 그 이후에 고민할 일이다.** 최초 설계때부터 이런 걸로 골머리앓지 말고 일단 작동하는 회로를 만들자.

우리는 처음에 진동으로 PCB 커넥터가 분리되는 것을 막겠다고 실제 상용차에 들어가는 Molex DuraClik™ 커넥터 시리즈를 사용했다. 이것들은 손가락만한 커넥터 하나에 2000원씩 하면서 끼울 땐 더럽게 안 끼워지고, 뺄 땐 더 안 빠지다가 부러진다. 그 와중에 터미널이 커넥터에서 뽑히고 전선이 터미널에서 빠져버린다. 이러면 되살릴 수도 없는데 비싸다 보니 수량이 넉넉치도 않다. 인접한 두 터미널이 합선이 나는 기상천외한 문제도 있었다.

PCB 대신 만능기판에 회로 만들어서 잘 굴리는 다른 학교들도 있는데 초심자 주제에 욕심이 과했다. 공장에서 찍어내서 수십만 킬로미터씩 달려야 하는 양산차들에는 필요하겠지만, 1년만에 만들어서 며칠 굴릴 차를 처음 개발할 때에는 마음을 좀 비울 필요가 있다.
<br>

#### 2-5. 신호의 출처와 종류를 정확히 파악하자
##### 1. Floating과 LOW는 다르다!!!

디지털 신호는 HIGH와 LOW의 두 가지 상태를 가진다. 그러나 엄밀히 말하면, High-Z라는 상태가 하나 더 있다. 전선이 연결되지 않은 하이 임피던스, 즉 floating 상태이다.

**회로가 연결되어 있는데 전압이 0V라서 LOW인 것과, 회로가 연결되어 있지 않아서 멀티미터에서 0V가 찍히는 floating 상태는 서로 같지 않다.** 어쨌든 둘 다 0V니까 같은 것 아니냐고 할 수 있지만, 디지털 회로는 LOW와 High-Z 상태에서 서로 다르게 동작할 수 있다. LM311은 비교기 입력핀을 GND에 연결해서 0V를 입력했을 때는 제대로 동작하지만, 아예 연결하지 않아 floating 상태로 두었을 때는 정상 동작하지 않는다.

사실 당연한 개념이다. 프로그래밍에 조금 경험이 있는 사람이라면 null과 정수를 비교할 수 없다는 사실을 잘 알 것이다. 0과 null은 다르다. 마찬가지로 LOW와 floating은 다르다.

<div class='center'><img src='{{ page.assets }}/zero_vs_null.jpg' style='width: 60%'></div>

로직 IC 칩들을 사용할 때 출력이 원하는 대로 나오지 않는다면 전선이 제대로 연결되어 있는지 확인해 볼 필요가 있다.

##### 2. Push-Pull, Open Drain과 Open Collector 회로

아두이노나 STM32같은 마이크로컨트롤러는 디지털 출력을 지원한다. 디지털 HIGH를 출력하면 해당 핀에서 실제로 V<sub>cc</sub> 전압이 측정되고, 반대로 LOW를 출력하면 해당 핀이 GND와 도통 상태가 된다. 이러한 디지털 출력을 Push-Pull 구조라고 한다.

<div class='center'><img src='{{ page.assets }}/push_pull.png' style='width: 50%'></div>

복잡하게 생각할 것 없고, 디지털 출력 핀의 안쪽에 트랜지스터 두 개가 달려 있다. 두 트랜지스터는 각각 HIGH와 LOW에 연결되어 있다. 어떤 신호를 출력할 것인지에 따라 두 트랜지스터 중 하나가 활성화되며 출력 단자를 HIGH 또는 LOW와 연결시켜 놓는다. 그렇기 때문에 HIGH는 확실히 HIGH이고, LOW는 정말 LOW이다.

이 Push-Pull 방식은 디지털 핀이 실제로 전압을 출력하기 때문에 사용하기 편하다는 장점이 있으나, 출력 전압을 바꿀 수 없다는 단점이 있다.

반면 Open Drain/Collector 회로는 HIGH에 연결된 트랜지스터가 없고 LOW에만 트랜지스터가 있다. 다음 회로는 트랜지스터의 컬렉터가 출력 핀으로 나가는 Open Collector 회로이다.

<div class='center'><img src='{{ page.assets }}/open_collector.png' style='width: 50%'></div>

따라서 이 회로는 논리 HIGH 신호를 출력할 수가 없다. 오직 LOW일 때 디지털 핀을 GND로 끌어내릴 수만 있는 것이다. LOW 상태가 아니라면 디지털 핀은 그냥 아무것도 연결되어 있지 않은 floating 상태가 된다. <b>floating 상태를 멀티미터로 측정하면 0V가 나오지만 이것은 실제 LOW와는 다른 것이다.</b>

<div class='center'><img src='{{ page.assets }}/open_collector_1.png' style='width: 50%'></div>

그래서 위 그림과 같이 디지털 핀의 외부에 별도로 풀업 회로를 구성해 주어야 한다. 이렇게 되면 디지털 출력이 LOW가 아닐 때 디지털 핀은 풀업 저항으로 연결된 외부 전원 전압을 출력하게 된다.

이 회로의 장점은 디지털 핀의 출력 전압을 내 마음대로 설정할 수 있다는 것이다. 그저 내가 원하는 전압에 풀업시키면 디지털 핀은 해당 전압을 출력한다. 단점은 외부에 풀업 회로를 별도로 구성해 주어야 하고, 풀업 저항에서 전류가 샌다는 점이다. 물론 자동차 정도 규모의 시스템에서는 크게 중요하지 않다.

방금의 Open Collector 회로에서 BJT 트랜지스터 대신 NMOS를 사용하고 Drain 핀을 출력 핀으로 쓰면 Open Drain 회로가 된다. Open Collector와 Open Drain은 근본적으로 같다. 논리 소자로 트랜지스터와 MOSFET 중 무엇을 사용하느냐에 따라 달라질 뿐이다.

MOSFET은 대개 BJT 트랜지스터보다 더 큰 전류를 흘려보낼 수 있다. 그래서 Open Collector보다는 Open Drain 회로를 더 자주 보게 된다. 우리 팀이 사용하는 BMS와 모터 컨트롤러도 디지털 출력을 Open Drain으로 낸다.

따라서 우리는 차단 회로를 설계할 때 BMS나 IMD 같은 외부 장비가 디지털 출력을 어떤 방식으로 내는지 확인할 필요가 있다. 이 내용에 관한 더 자세한 설명은 [오픈 컬렉터 (open collector) 및 오픈 드레인 (open drain) 출력](https://m.blog.naver.com/eslectures/80137762936){:target="_blank"}{:class='external'}을 참고하면 좋을 듯 하다.

##### 3. 아날로그 신호

아날로그와 디지털 신호를 모두 사용하는 많은 장비는 디지털 그라운드(DGND)와 아날로그 그라운드(AGND)를 분리한다. 이는 디지털 영역에서 발생하는 노이즈가 아날로그로 넘어가서 오류가 나는 것을 방지하기 위함이다. 디지털 출력 신호가 LOW로 전환될 때, DGND에는 디지털 회로의 유도 성분으로 인한 기전력이 유도된다. 이를 ground bounce라고 하며, 실제 접지면과 DGND 사이의 일시적인 전압 차이를 만든다.

한편, 우리가 만들어야 하는 BSPD 또한 홀 센서와 브레이크 압력 센서로부터 아날로그 입력을 받아 디지털 출력을 만들어야 한다. 그러나 사실 우리 수준에서 PCB의 trace 길이와 두께까지 고려하면서 AGND와 DGND를 적절하게 분리하는 설계를 하는 것은 어려운 일이다.  그래서 우리 팀은 그냥 아날로그 회로에서도 그라운드를 분리하지 않고 차체 공통 접지면을 사용했고 지금까지 별다른 문제는 없었다.

그러나, 이미 AGND가 분리되어 있는 장비들에서는 이를 고려해야 한다. 우리의 PM100DX 모터 컨트톨러는 아날로그 센서를 위한 AGND와 5V 전원을 별도로 제공하고 있었다. 심지어 데이터시트에 *Analog ground(AGND) should NOT be connected to chassis ground* 라고 적혀 있었다.

그런데 우리는 22년에 일정을 맞추지 못해 대회날까지 차 한 번을 못 굴려봤고, 이걸 대회 현장에서야 처음 알게 됐다. **대충 이 신호는 이렇게 나오겠지**는 위험한 생각이다. 꼭 이 신호는 어떻게 처리해주어야 정상 작동할 수 있는지를 미리 생각하고 설계하도록 하자.

#### 2-6. LV 전원과 전압 강하
항상 LV 전원은 12V라고 언급해 왔지만, 배터리를 전원으로 쓰는 이상 LV 전압은 계속 바뀔 수밖에 없다. 리튬인산철 4s 배터리는 12~14.6V 전압대를, 리튬이온 4s 배터리는 12.8~16.8V 정도의 전압대를 사용하게 된다. 우리는 이 전압을 12V로 정확히 맞추어 줘야 한다는 잘못된 생각에 사로잡혀 8~40V to 12V 15A 컨버터를 사용했다. 이 컨버터를 배터리 바로 뒷단에 물려 차량의 모든 LV 회로가 정확히 12V를 공급받을 수 있게 하고자 한 것이다.

그러나 차량용 제품들은 모두 가변적인 LV 전압 특성에 따라 훨씬 넓은 전압대에서 사용할 수 있도록 설계되어 있다. 실제로 우리 BMS는 8~30V, IMD는 10~36V, 모터 컨트롤러는 9~18V의 전원 전압을 허용한다. 따라서 우리는 제작한 PCB에서도 <b>인클로저로 공급되는 전압을 12V로 정확히 맞출 것이 아니라, LV 배터리 전압을 그대로 공급받아 인클로저 내에서 필요한 전압을 직접 만들어 사용해야 한다.</b>

이것이 필수적인 이유는 <b>차량 내 배선에서 전압 강하가 발생</b>하기 때문이다. 배선에 초전도체를 사용하지 않는 이상 구리 전선은 저항을 가지고 있다. 배선에 전류가 흐르면, 배선은 저항으로 작용하여 전압 강하를 만들어낸다. <dfn>V = IR</dfn> 에 따라서 배선에서 발생하는 전압 강하는 배선의 단면적(AWG)와 길이, 흐르는 전류에 영향을 받는다.

한편, 차량기술규정에 따라 주 비상정지 스위치, 보조 비상정지 스위치, BOTS, HVD 인터락은 AIR를 작동시키는 전류를 직접 전달해야 한다. 필연적으로 AIR는 LV 전원에서 차량 전체에 퍼져있는 차단 회로 구성요소를 모두 거친 후에 전원을 공급받게 된다. 보조 비상정지 스위치는 차량의 좌우 및 운전석, BOTS는 브레이크 페달에 달려있기 때문에 배선은 아무리 짧아도 3m 이상이 될 수밖에 없다.

앞서 언급한 것처럼 배선의 전압 강하는 흐르는 전류에도 영향을 받는다. 우리 차량은 대략 LV 활성화 시 1A, HV 활성화 시 2A, 모터 구동 시 4A 정도를 소모한다. [전압 강하 계산기](https://www.rapidtables.com/calc/wire/voltage-drop-calculator.html)로 간단하게 계산해 보면 12V 전원, 18AWG 배선 5m, 전류 5A에서 약 1V의 전압 강하가 발생한다. 즉 LV 배터리 전압을 12V로 맞춰 주면 부하는 11V만 받을 수 있다는 뜻이다.

불행하게도 전압 강하에는 또 다른 유형이 있다. 바로 전원 내부 저항에 의한 전압 강하이다. 현실의 전압원들은 이상적인 전압원과 다르게 내부 저항을 가지고 있다. 따라서 실제 회로는 회로도와 다르게 전원과 부하 저항에 추가로, 전원 내부저항과 배선 저항이 추가로 포함되어 있다. 이로 인해 부하 전류가 증가하면 전원 내부저항에 걸리는 전압 강하 또한 증가하여 전원 전압은 더욱 낮아지게 된다. 실제로 우리 차량에서 HV를 활성화했을 때 AIR가 받는 전압은 9V에 불과했다. 작동 전압을 겨우 맞추는 수준이다.

또한 모터 컨트롤러도 12V 대신 10V 정도만을 공급받았는데, 낮은 전압으로 컨트롤러의 3상 스위칭 IGBT의 MOSFET이 포화 상태에 도달하지 못해 스위칭이 일어나지 않는 문제가 있었다. 컨트롤러에서 "Hardware Gate/Desaturation Fault"가 발생해 컨트롤러가 고장난 줄로만 알고 절망했는데, 단지 전원 전압이 모자랄 뿐이었다.

그러니 <b>LV 전원은 항상 12V보다 높은 전압을 모든 부하에 공급해줄 수 있을 만큼 충분히 큰 전압을 유지해야 한다</b>. 그러니 우리도 회로를 설계할 때 모든 부품이 충분한 작동 전압 범위를 확보하도록 하고, 정확한 레퍼런스 전압이 필요한 곳에서만 LDO 선형 레귤레이터나 [소형 DC-DC 컨버터](https://smartstore.naver.com/misoparts/products/5356716694)를 사용해 전압을 맞추도록 해야 한다.

#### 2-7. 셀 내부 저항과 DCL
우리가 사용하는 Orion BMS 2에는 DCL이라는 지표가 있다. Discharge Current Limit으로, 배터리 팩이 방전할 수 있는 최대 전류이다. 이 정보는 CAN 버스를 통해 모터 컨트롤러로 전달되어 모터의 출력 상한선을 실시간으로 제한한다.

우리는 모터를 가동하면 이 DCL이 서서히 감소하면서 출력이 저하되다가, 결국 0A에 도달해 BMS가 Over Current Fault를 내고 차단 회로를 작동시키는 현상에 8개월 넘게 고통받았다. BMS가 제공하는 정보는 단 하나, DCL reduced due to cell resistance 였다. 셀의 내부 저항값이 너무 높아 DCL을 줄이겠다는 뜻이다.

겨우 한 번 굴려보면서 제대로 방전시킨 배터리에서 내부 저항이 너무 높다니, 처음에는 세그먼트를 잘못 만든 줄 알았다. 세그먼트 스폿 용접 중 몇 번의 실수가 있었기에 이것이 문제가 됐다고 생각한 것이다. 그러나 큰 돈을 들여 의심가는 세그먼트를 새로 교체한 후에도 같은 문제가 계속 발생했다.

여러 번의 시행착오 끝에 발견한 한 가지 개연성은 이 DCL 감소 현상이 낮은 SOC(충전량)에서만 발생한다는 것이다. 배터리는 차량에 탑재하고 주행할 때만 유의미한 방전을 할 수 있는데, 주행할 기회가 별로 없다 보니 충전할 일이 없어 주로 40% 미만의 충전량을 유지했다.

여기서 BMS의 데이터시트에 언급된 한 문장이 눈에 띄었다. BMS는 모든 셀 전압을 감시하며 단 하나의 셀이라도 설정된 셀 최소 전압보다 낮게 떨어질 위험이 있다면 DCL을 감소시킨다는 것이다. 이 문장을 기반으로 세운 가설은 다음과 같다.

1. BMS는 방전을 시작하는 즉시 각 셀의 실제 내부 저항을 측정할 수 있다. BMS는 각 셀의 Open Voltage와 Live Voltage, 현재 방전 중인 전류를 알고 있다. 각 셀의 <dfn>V<sub>open</sub> - V<sub>live</sub></dfn> 는 내부 저항에서 일어나는 전압 강하의 크기다. 현재의 전압 강하와 방전 중인 전류를 알고 있으니, <dfn>V = IR</dfn> 에 따라 셀의 내부 저항을 바로 계산해낼 수 있게 된다. (자세한 내용은 [리튬이온 배터리의 수명과 내부저항](https://luftaquila.io/blog/diy/measuring-battery-charge-cycle/)을 읽어보길 추천한다)
2. BMS는 어떠한 셀이라도 그 전압이 사전에 설정된 셀 최소 전압보다 떨어지는 상황을 이악물고 막으려 한다.
3. 방전 전류가 커지면 셀의 내부 저항에서 일어나는 전압 강하 또한 커진다. 이 현상을 셀 외부에서 관찰하면, 셀의 전압이 감소하는 효과를 낸다.
4. 방전 전류로 인해 셀 전압이 감소하면, 셀 최소 전압보다 낮게 떨어질 위험이 있다. BMS는 모든 셀의 실제 내부 저항을 알고 있기 때문에 이러한 상황이 일어나게 되는 최소 방전 전류를 계산할 수 있다.
5. 셀을 최소 전압보다 높게 유지하려면 위에서 계산한 최소 방전 전류 이상은 방전할 수 없다. 이 값으로 DCL을 건다.

따라서, 셀 전압이 최소 전압과 비슷해지는 낮은 충전량에서 모터를 구동하면 DCL이 감소하는 현상이 나타나는 것이다. 이 가설에 따라 몇 가지 실험을 했고, 높은 충전량에서는 어떤 상황을 만들어도 DCL이 감소하지 않았다.

그러니 DCL이 감소하는 문제를 피하고 싶다면 셀의 최소 전압을 실제 셀 데이터시트에 명시된 Minimum cell voltage 값으로 설정해야 한다. 우리는 셀 수명을 높이고자 3.2V로 설정했었는데, 셀의 데이터시트 최소 전압은 2.5V였다. 배터리 용량 한 줌이 아까운 내구에서는 배터리를 끝까지 끌어다 써야 한다.

#### 2-8. 작고 반짝이는 건 언제나 옳다
처음에 회로를 설계할 때는 작동에 너무 몰두한 나머지 이후의 회로 디버깅을 전혀 고려하지 않은 설계를 하게 된다. 그렇지만 회로에서 꽤 의미있는 지점에 전압이 걸리면 켜지는 LED를 한가득 추가하는 것을 빼먹지 않기를 추천한다.

<div class='center'><img src='{{ page.assets }}/led.jpg'></div>

그렇지 않으면 사소한 거 하나만 깜빡해도 회로 뚜껑을 따서 좁디좁은 접점에 멀티미터 프로브를 갖다대고 전압을 읽어야 한다. 프로브가 미끄러져 옆의 접점이랑 합선이 나고 회로가 고장나면 그야말로 금상첨화다. 우스갯소리가 아니라 이런 적이 한두 번이 아니다.

<div class='center'><img src='{{ page.assets }}/led_pcb.png' style='width: 70%'></div>

다 준비하고 LV 올리고 HV 올렸는데 TSAL에 빨간 불이 안 들어온다. 등골이 쎄하다. 아무리 생각해봐도 다 멀쩡한데 HV가 안 켜진다. 옆에서 파워트레인 파트장이 얘기한다. HVD는? 아!

보조 킬 스위치 하나 안 풀거나 HVD 자체를 안 꽂아놓고 HV 안 켜진다고 고심한 것이 정말 셀 수 없이 많다. 그럴 때마다 멀티미터로 기판 찍어보고 있으면 정말 화가 난다. LED를 여기저기 박아 놓으면 훨씬 편하고 빠르게 문제를 파악할 수 있다. PCB 설계할 때 잠깐 조금 더 고생하면 인생이 편해진다.

<div class='center'><img src='{{ page.assets }}/led_2.jpg'></div>


### 3. 임베디드 프로그래밍에 관한 팁
물론 팀마다 구현에 차이가 있겠지만, E-Formula 차량을 구동시키는데 아두이노같은 마이크로프로세서(MCU)는 필요가 없다. 차량기술규정은 차단 회로나 VI와 같은 안전과 직결되는 회로에서 소프트웨어 제어를 허용하지 않고 있다.

그러나 데이터로깅과 같은 부가적인 목적으로 MCU를 사용하곤 하는데, 코드를 작성할 때 도움이 될만한 팁 몇 개를 적어보고자 한다.

#### 3-1. 메모리를 소중하게 생각하고 사랑하자

운영체제가 존재하지 않고 메모리 주소가 모두 실제 physical address인 임베디드 펌웨어에서 `malloc()`은 사용할 필요가 사실상 없다. `malloc()`은 없는 메모리를 만들어내는 것이 아니라 운영체제한테 이만큼 할당해 달라고 요청하는 것이다. 운영체제도 없고 모든 메모리가 우리에게 활짝 열려 있으니 그냥 사용하면 된다.

컴퓨터는 정직하다. 어디선가 중성미자 우주선이 날아와 내 MCU를 한 대 쳐서 메모리 비트 하나가 뒤집히는게 아니라면 런타임 에러는 대부분 메모리 문제다. STM32F4의 내장 메모리는 작고 귀여운 192KiB SRAM이 전부다. 아두이노 우노의 SRAM은 심지어 2KiB이다. NUL 캐릭터를 잠시 소홀히 여겼다거나 포인터를 좀 안일하게 사용하면 MCU가 멈춰설 것이다. 항상 메모리를 소중히 여기고 의심하자. 임베디드 프로그래밍은 자원이 차고 넘치는데다 메모리 가상화가 제공되는 데스크탑 프로그램 작성과는 다른 점이 많다.

아두이노나 C++, 파이썬처럼 저수준 메모리 관리가 필수가 아닌 언어를 사용하는 사람들은 상대적으로 신경쓸 필요가 덜하다.

#### 3-2. Interrupt와 Polling
ADC 변환, 통신(UART, I2C, SPI 등), GPIO 제어와 같은 모든 주변 장치(peripheral) 작업은 명령 즉시 완료되지 않는다. 작업이 완료되는 데까지는 반드시 시간이 소요된다. 따라서, CPU는 주변 장치가 명령한 작업을 완료했는지 확인할 필요가 있다. CPU가 이를 확인하는 방식은 크게 인터럽트와 폴링으로 나눌 수 있다.

* Interrupt
    1. CPU가 주변 장치한테 일을 시킨다. 명령만 내리고 CPU는 다음 코드를 계속 실행한다.
    2. 주변 장치는 할 일을 마친 후 CPU에 인터럽트를 날린다.
    3. CPU는 실행하던 코드를 잠시 중단하고 인터럽트를 처리한다. 인터럽트 루틴이 끝나면 기존 코드를 이어서 실행한다.

컴퓨터 엔지니어의 기본 소양은 가용 가능한 자원이 노는 꼴을 두고 보지 못하는 것이다. 인터럽트 방식은 CPU가 노는 시간 없이 계속 일하도록 갈굴 수 있다.

하지만, 인터럽트 방식은 순차적으로 처리해야 하는 통신 시퀸스를 구현하기가 다소 어렵다. 예를 들어 1602 LCD의 경우 초기화 시 수 ms 간격으로 여러 가지 초기화 메시지를 I2C 버스에 보내야 하는데, 이걸 다 송신 인터럽트로 구현하려면 코드가 비직관적으로 변하고 예상치 못한 상황에 대응하기가 어려워진다.

* Polling
    1. CPU가 주변 장치한테 일을 시킨다. 일 시키고 계속 그 주변 장치를 지켜본다.
    2. 주변 장치는 할 일을 마치면 레지스터에 특정 비트를 set한다.
    3. CPU는 그걸 확인하고 나서야 다음 코드를 계속 실행한다. 만약 일정 시간동안 기다려도 비트가 set되지 않으면 Timeout 에러를 내든지 한다.

앞선 인터럽트 방식과 반대로 한 context 안에서 순차 처리가 쉽다. peripheral 최초 초기화 시에 많이 사용한다. 하지만 주변 장치가 작업을 완료할 때까지 CPU가 논다.

만약 운전자는 브레이크를 밟았는데 MCU가 LCD에 화면 그리는 거 기다리면서 제동 안 하고 멍때리고 있으면 어떻게 될까? 물론 브레이크는 그런 식으로 작동하지 않지만 아무튼 썩 탐탁한 상황은 아니다.

##### +) 인터럽트 루틴에서는 간단한 작업만 해야 한다. 반드시.
CPU가 main context를 수행하다가 인터럽트가 터진다. 그럼 CPU는 context를 백업한 후에 인터럽트 루틴을 수행한다. 그런데 인터럽트 루틴을 실행하는 중에 또 인터럽트가 터지면 어떻게 될까?

인터럽트를 처리하는 하드웨어는 플랫폼마다 다소 다른데, STM32는 NVIC(Nested Vectored Interrupt Controller)를 사용한다. 말 그대로 중첩이 가능하며 인터럽트 벡터로 처리되는 시스템이다. 현재 실행중인 인터럽트 루틴보다 우선순위가 더 높은 인터럽트가 터지면 해당 ISR로 점프한다. 즉, 위와 같은 상황도 잘 핸들링할 수 있다.

그러나 인터럽트 루틴을 실행하는데 걸리는 시간보다 인터럽트가 발생하는 주기가 더 짧으면 인터럽트는 계속 쌓일 수밖에 없다. 이것이 ISR에서 간단한 일만 해야 하는 이유이다. 예를 들어 보자. UART 수신 인터럽트는 시리얼 통신 스트림에서 지정된 길이의 문자열이 도착하면 발생한다. 문자열이 도착할 때마다 메모리에 복사하고 strtok()으로 지금까지 수신한 문자열을 나눈 뒤 원하는 문자열이 있나 찾아보고 있으면 무선 통신 모듈에 시리얼로 해당 문자열을 전송하고... 모든 걸 ISR에서 수행하다 중간에 인터럽트가 또 터지면 인터럽트 흐름이 나락으로 떨어진다.

인터럽트 루틴에서는 정말 필수적인 시간 체크, 비트 clear, flag set과 같은 동작만 해야 한다. 이후에 수반되는 복잡하고 오래 걸리는 작업은 메인 컨텍스트에서 해야 한다. 나는 그냥 전역으로 수신 버퍼와 플래그를 하나씩 선언해 놓고, 인터럽트 루틴에서 버퍼에 복사한 후 수신 플래그를 set만 하도록 구현해 놓았다. 그럼 이제 main 함수의 무한 루프에서 수신 플래그를 확인하고 필요한 작업을 수행한 다음 플래그를 clear하는 방식이다.

#### 3-3. UART는 느리고 문자열은 무겁다
성능이 중요한 응용 프로그램을 만드는 게 아니라면 UART 시리얼 통신의 속도에 대해 진지하게 생각해볼 일이 없다. UART는 50년은 된 기술로, 상대적으로 느리고 먼 거리(10m~)까지 전달할 수 있는 신뢰성 높은 통신 방식이다. 통신의 세계에서 통신 가능 거리가 길어진다는 말은 일반적으로 느리다는 뜻이다.

115200bps UART는 1초에 115200개의 비트를 전송한다. UART로 1바이트를 전송하는 데에는 데이터 8비트와 start, end bit 하나씩 총 10비트가 필요하다. 따라서 115200bps로는 11520B/s의 통신 속도가 나온다. 11.25KiB/s이다. 일반적인 UART에서 가장 빠른 921600bps를 사용해도 초당 90KiB가 한계다.

한편, ASCII 문자열은 글자 1개에 1바이트가 필요하다. 문자열로 저장되는 다음과 같은 로그가 있다고 하자.

```
2023-05-12-10:00:00 INFO GPS GPRMC $GPRMC,114455.532,A,3735.0079,N,12701.6446,E,0.000000,121.61,110706,,*0A
```

107개 문자로 구성되어 있는 107 Byte 크기의 문자열이다. 115200bps로 전송하는데 9.3ms가 소요된다. 9.3ms는 240MHz로 작동하는 ESP32에게 약 220만, 168MHz로 작동하는 STM32F4에게 약 156만 개 클럭이 필요한 영겁과도 같은 시간이다. 하다못해 16MHz로 작동하는 아두이노 나노에게도 15만 개 클럭이 지나가는 엄청난 시간이다.

이런 UART 통신을 polling 방식으로 쓰면 말 그대로 CPU는 9.3ms동안 '논다'. 정확한 비유는 아니지만 STM32F4의 1클럭과 사람의 1초가 같다고 하면 무려 18일을 논다.

내 STM32는 초당 170개씩 발생하는 로그를 Wi-Fi로 서버에 보내기 위해 ESP32에 전송해야 했다. 처음에는 ASCII 문자열 로그를 115200bps UART로 전송했다. 로그가 개당 평균 80바이트라고 하면, 1초에 13600 Byte가 생긴다. 115200bps로는 애초에 전송이 불가능하다. 이러한 것들을 계산해보지 않고 만들었더니 코드는 제대로 짰는데 모든게 꼬여서 엉망진창이 됐다. 시스템 성능이 충분해야 코드가 제대로 돌아간다.

그래서 통신 방식을 400kHz I2C로 바꾸고, 로그 프로토콜을 정의해 개당 16Byte로 고정했다. 4바이트는 타임스탬프, 4바이트는 로그 정보와 체크섬, 8바이트는 데이터 이런 식이다. 그 결과 보수적으로 계산해도 초당 2200개의 로그를 전송할 수 있게 되었고, 이후로 아무런 문제도 생기지 않았다.

#### 3-4. Brownout 대처

앞서 설계 부분에서 배선 저항과 전원 내부저항에 의한 LV 전압 강하에 대한 이야기를 했다. 여기에 추가적으로, 전류가 증가하는 순간 전원 전압은 순간적으로 크게 떨어진다. 이 전원 전압 강하는 DC-DC 컨버터를 통해 MCU 전원을 공급하는 5V나 3.3V 레일 전압도 순간적으로 크게 떨어뜨린다.

<div class='center'>
    <img src='{{ page.assets }}/voltage_drop_12.jpg' style='max-width: 45%'>
    <img src='{{ page.assets }}/voltage_drop_3.3.jpg' style='max-width: 45%'>
    <br> <span style='font-size: .8rem'>HV 활성화 순간 LV와 3.3V 레일의 전압 강하</span>
</div>

위 사진에서 순간적으로 LV는 4.5V까지, 3.3V 레일은 1.98V까지 떨어진다. 이 전압 강하는 대략 ~4ms 동안 진행되는 것으로 관찰됐다. 전원 라인이 MCU가 제대로 동작하지 않는 수준으로 내려가는 [brownout](https://blog.naver.com/cubloc/220065808152) 현상으로 인해 MCU가 리셋되는 증상이 있었다.

이러한 현상은 LV 전원에 커패시터를 추가해 완화할 수 있다. 평소에 LV 배터리가 커패시터를 충전시켜 두었다가, 전원 전압이 떨어질 때 커패시터가 방전하며 전압 강하를 보상해 주는 식이다. 이 커패시터의 용량 계산은 [How to calculate capacitor to fix a brownout](https://electronics.stackexchange.com/questions/500039/how-to-calculate-capacitor-to-fix-a-brownout)을 참고했다.

<div class='center'>
    <img src='{{ page.assets }}/brownout_capacitor_before.jpg' style='max-width: 45%'>
    <img src='{{ page.assets }}/brownout_capacitor_after.jpg' style='max-width: 45%'>
    <br> <span style='font-size: .8rem'>1000uF 전원 커패시터 추가 전/후</span>
</div>

오실로스코프가 싸구려라 전압 강하가 시작하는 순간의 파형은 잡지 못했지만(트리거 작동 직전의 파형을 볼 수가 없다), 전압 강하의 폭이 감소한 것을 관찰할 수 있다. 커패시터 추가 후 HV 활성화 시 STM32가 리셋되는 현상이 사라졌다.

#### 3-5. 개발 생산성은 중요하다
아두이노는 대부분 별도의 USB 통신용 MCU가 보드에 박혀 있어 프로그램 업로드 시 메인 MCU를 리셋하고 업로드 모드로 진입시켜 준다. 그러나 ESP32나 STM32에는 기본적으로 그러한 기능이 없다. Boot mode selection 핀을 이용해 직접 부팅 방법을 지정해 주어야 프로그램을 새로 플래시 메모리에 업로드할 수 있다. 굉장히 번거롭고 불편하다.

STM32 개발 환경인 STM32CubeIDE나 ESP32 개발 환경인 ESP-IDF는 모두 OpenOCD를 통한 프로그램 업로드 기능이 있다. 표준 JTAG 디버거나 ST-Link가 하나 있다면 개발하는 컴퓨터에서 단축키만 눌러도 프로그램을 업로드할 수 있게 된다. 디버깅 기능도 제공하기 때문에 타겟 보드에서 breakpoint, memory view, expression evaluation 등을 모두 사용할 수 있다. 이런 거 없으면 아두이노에서처럼 시리얼로 printf 찍어가면서 확인하는 수밖에 없다. ST-Link는 5천 원이면 [호환 제품](https://smartstore.naver.com/misoparts/products/5263743411)을 구할 수 있다.

{% include_relative index.md %}