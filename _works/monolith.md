---
title: Monolith
description: 오픈소스 실시간 무선 데이터로거
date: 2024-01-19
image: /assets/images/works/monolith/main.jpg
layout: docs
---
[GitHub](https://github.com/luftaquila/monolith)
&emsp;
[TMA-2 실시간 텔레메트리 모니터](https://monolith.luftaquila.io/live/)
&emsp;
[TMA-3 데이터 분석 도구](https://monolith.luftaquila.io)

모노리스는 대학생 자작자동차대회 출전 차량을 위한 오픈소스 DIY 데이터로깅 플랫폼입니다.

공개된 설계도에 따라 직접 데이터로거를 제작하면 실시간 원격 데이터 모니터링, 웹 기반 데이터 분석 도구 등을 무료로 쉽게 이용할 수 있습니다.

지원하는 로깅 데이터는 다음과 같습니다.

* CAN 2.0(A/B) 버스 트래픽
* 8채널 디지털 입력 신호
* 4채널 아날로그 입력 신호
* 4채널 휠 스피드 센서(디지털 파형 주기 측정)
* 3축 ±4g 가속도 (ADXL345)
* GPS 위치 정보 (NEO-6/7M)
* 전원(LV) 전압 및 자체 CPU 온도
* RTC 실제 시간 정보

원격 데이터 모니터링은 드라이버가 휴대한 스마트폰의 핫스팟 네트워크를 통해 이루어집니다. 데이터로거는 핫스팟을 통해 웹 서버에 데이터를 전송하며, 실시간으로 기술팀 인원의 스마트폰에 생중계됩니다.

또한, 웹 기반 데이터 분석 도구는 주행 이후 데이터로거의 SD카드에 저장된 데이터를 업로드하면 분석하기 쉽도록 그래프로 시각화해 보여줍니다.

이러한 원격 데이터 모니터링과 분석 도구는 모두 미리 구축된 웹 서버와 브라우저에서 구현되므로, 사용에 별도 프로그램 설치가 필요하지 않습니다.

회로도, 필요한 부품 목록, 제작 가이드, 소프트웨어 소스코드는 모두 공개되어 누구나 자유롭게 이용하고 수정할 수 있습니다.

## TMA-1 데이터로거
![](/assets/images/works/monolith/tma-1.jpg)

### TMA-1 설정 도구
![](/assets/images/works/monolith/tma-1_config_tool.png)

## TMA-2 실시간 텔레메트리 모니터
![](/assets/images/works/monolith/tma-2.png)

## TMA-3 데이터 분석 도구
![](/assets/images/works/monolith/tma-3.png)

<style>
div#content img {
    max-height: none!important;
    width: 700px!important;
}
</style>
