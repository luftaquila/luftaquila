---
title: 차량 코너웨이트 측정 시스템
description: 대학생 자작자동차대회 차량 무게 측정 도구
date: 2023-09-10
image: /assets/images/works/cornerweight/cornerweight.jpg
layout: docs
---

### 서비스 링크
[코너웨이트 측정기](https://a-fa.luftaquila.io/weight){:target="blank"}{:class='link'}
&emsp;
[GitHub 저장소](https://github.com/luftaquila/a-fa-weight){:target="_blank"}{:class='link'}

## 소개
직접 제작하는 자작자동차는 차량의 각 바퀴에서의 무게를 측정하여 앞과 뒤, 좌우에 배분되는 무게 균형을 직접 맞춰 주어야 합니다. 이를 코너웨이트 측정이라고 합니다.

그러나 가난한 대학생 자작자동차 소학회 특성상 전용 장비가 없어 체중계 4개에 각 바퀴를 올려놓는 식으로 코너웨이트를 측정해 왔습니다.

균형을 맞추기 위해서는 차량을 조정하며 무게가 어떻게 변하는지 관찰해야 합니다. 그러나 사람용 체중계는 하중이 가해지고 일정 시간이 지나면 자동으로 꺼집니다. **다시 측정하기 위해서는 300kg에 달하는 차량을 들었다 놓아 체중계를 다시 켠 후, 체중계가 꺼지기 전에 각 바퀴를 돌며 일일히 측정값을 읽어야 합니다.**

이러한 과정이 너무 비효율적이고 부정확하여, 보다 간편하게 코너웨이트를 측정할 수 있도록 코너웨이트 측정기를 제작했습니다. 한 화면에서 모든 바퀴의 무게와 차량의 총 중량을 확인할 수 있으며, 체중계에서 연속적인 무게 변화를 읽어 그래프로 보여줍니다.

![](/assets/images/works/cornerweight/spaghetti.jpg)

### 체중계 해킹
체중계에는 4개의 로드셀이 들어 있습니다. 체중계 회로는 이 센서들로 무게를 측정하고 LCD 디스플레이에 숫자를 표시합니다. 동시에 일정 시간이 지나면 체중계 전원을 차단합니다.


체중계에 들어 있는 기존 회로는 잘라버리고 로드셀만을 사용합니다. HX711 증폭기를 붙여 로드셀의 아날로그 신호를 증폭한 후, 이를 아두이노가 읽어 각 바퀴에서의 무게를 측정합니다.

![](/assets/images/works/cornerweight/wiring.jpg)

아두이노는 측정한 무게를 시리얼 통신으로 출력합니다. 웹 브라우저에서 Web Serial API를 이용하여 이 데이터를 읽어 시각화합니다. 실시간 중량 변화와 함께 각 바퀴의 무게, 차량의 총 중량을 한 화면에서 확인할 수 있도록 개발했습니다.

![](/assets/images/works/cornerweight/cornerweight.jpg)

### 사용 예
![](/assets/images/works/cornerweight/measure.jpg)

![](/assets/images/works/cornerweight/car.jpg)

<style>
img {
    max-height: none!important;
}
</style>
