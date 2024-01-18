---
title: +) 모노리스 DIY 데이터로거
description: "E-포뮬러 제작기: 데이터로깅"
category: e-formula
assets: /assets/posts/e-formula/2024-01-18-monolith-telemetry-datalogger
image: /assets/posts/e-formula/2024-01-18-monolith-telemetry-datalogger/main.jpg
layout: post
---

{% include_relative index.md %}

## 모노리스

[이전 글](https://luftaquila.io/blog/e-formula/datalogging-and-can/#%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A1%9C%EA%B1%B0)에서 데이터로거를 쓸만하게 만드는데 필요한 온갖 삽질에 대한 장황한 열변을 늘어놓았다. 직접 데이터로거 만들면서 하나하나 얻어맞은 것들이라 그러니 조금만 이해해 주기 바란다.

<div class='center'><img src='{{ page.assets }}/monolith.jpg'></div>

그래서 그 모든 기능을 지원하는 오픈소스 DIY 데이터로거를 만들었다.

제작 방법 보고 따라서 만들기만 하면 누구나 실시간 무선 데이터 모니터링 기능을 사용할 수 있다(사용 신청만 하면 서버를 제공해 드리고 있다). SD카드에 저장된 로그를 업로드하면 예쁘게 그래프를 그려주는 웹 기반 데이터 분석 도구도 있다.

기록할 수 있는 데이터의 종류는 다음과 같다.

* CAN 2.0(A/B) 버스 트래픽
* 8채널 디지털 입력 신호
* 4채널 아날로그 입력 신호
* 4채널 휠 스피드 센서(디지털 파형 주기 측정)
* 3축 ±4g 가속도 (ADXL345)
* GPS 위치 정보 (NEO-6/7M)
* 전원(LV) 전압 및 자체 CPU 온도
* RTC 실제 시간 정보

제작에 필요한 모든 부품 목록과 제작 방법, 사용 방법을 [Github](https://github.com/luftaquila/monolith)에 상세하게 작성해 두었다.

자작차 하는데 한 푼이라도 아끼는게 얼마나 중요한지 잘 알고 있다. 사용할 기능에 필요한 일부 부품만 장착해도 작동하도록 기능을 선택적으로 비활성화하는 소프트웨어도 포함되어 있다.

외국 자작차 동네에도 홍보하느라 기본 README를 영어로 작성해 놓았는데, [한국어 README](https://github.com/luftaquila/monolith/blob/main/README_KO.md)도 있으니 유용하게 사용되길 바란다.

## 마치는 글
대회가 끝나고 기억을 더듬어 전해드릴 수 있는 모든 것을 이 시리즈에 기록해 놓았다. 많이 부족하고 훨씬 더 잘 아시는 분들이 많지만, 어쩌다 자작차에 발을 들여 온갖 삽질을 하고 계실 전국의 많은 대학생들에게 조금이나마 도움이 되길 바란다.

데이터로거 관련 문의 뿐만 아니라 자작차 전기시스템에 관련한 모든 질문에 빠짐없이 답변을 드리고 있다. 궁금한 것이 있다면 언제든 사이트 홈페이지에 있는 연락처로 편하게 연락 주시면 된다.

차 만들면서 온갖 억까에 얻어맞고 팀원들이랑 싸워도 보고 하다보면 내가 무슨 부귀영화를 누리겠다고 이 삽질을 하고 있나 하는 생각이 들 때가 참 많다. 그러나 분명 그 고생을 하면서 수많은 생각을 하고, 인간적인 무언가를 얻고, 어디가서도 배울 수 없는 진짜 경험과 값진 지식을 갖게 된다.

모든 힘든 것들과 나쁜 기억은 그냥 작업 끝나고 다같이 맥주 한 잔 하고 대회 뒤풀이 한 번 조지면 다 사라진다. 졸업하고 취업하고 보니 이만큼 끝내주고 행복한 추억이 없다. 모두 행운이 함께하고 몸과 마음과 지갑이 다치지 않는 자작차 활동이 되었으면 좋겠다.

<div class='center'><img src='{{ page.assets }}/DSC_1574.jpg'></div>

<div class='center'><img src='{{ page.assets }}/DSC_1715.jpg'></div>


{% include_relative index.md %}
