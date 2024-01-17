---
title: 차량 원격 모니터링 시스템
description: E-Formula 데이터로거
date: 2023-09-11
image: /assets/images/works/telemetry/main.png
layout: docs
---

### 서비스 링크
[실시간 원격 계측](https://a-fa.luftaquila.io/telemetry){:target="blank"}{:class='link'}
&emsp;
[로그 변환 및 데이터 분석기](https://a-fa.luftaquila.io/telemetry/review){:target="blank"}{:class='link'}
&emsp;
[GitHub 저장소](https://github.com/luftaquila/a-fa-telemetry){:target="_blank"}{:class='link'}

## 소개

KSAE 대학생 자작자동차대회 출전 차량의 주행 데이터를 수집하기 위한 데이터로깅 시스템입니다.

오픈소스 데이터로거 프로젝트 [모노리스](https://github.com/luftaquila/monolith){:target="blank"}{:class='external'}의 초기 버전입니다.

![](/assets/images/works/telemetry/poster.jpg)

### 하드웨어
임베디드 하드웨어는 STM32F4 MCU로 구현되었으며, CAN 버스 트래픽, 디지털/아날로그 신호, 디지털 펄스 신호 주기, 3축 가속도, GPS 등 다양한 데이터를 수집하여 SD카드에 저장합니다.

또한 수집한 데이터를 즉시 드라이버 스마트폰의 Wi-Fi 핫스팟 네트워크로 전송하여 기술팀이 주행 중 차량 상태를 실시간으로 모니터링할 수 있도록 합니다.

![](/assets/posts/e-formula/2023-08-29-lv-introduction/lv.jpg)

### 중계 서버
서버는 소켓 통신을 통해 데이터를 수신하며, 이를 여러 명의 기술팀 인원이 동시에 자신의 스마트폰으로 주행 데이터를 확인할 수 있도록 중계합니다.

![](/assets/images/works/telemetry/telemetry.png)

### 로그 해석 및 데이터 분석기
안정적인 전송을 위해 오류 검출 기능을 포함한 16 Byte 규격의 로그 프로토콜을 정의하였으며, 이를 json 또는 csv로 변환하는 웹 기반 해석기를 지원합니다. 또한 같은 웹 어플리케이션에서 해석한 로그를 바로 분석할 수 있도록 그래프를 통한 데이터 시각화 도구를 제공합니다.

![](/assets/images/works/telemetry/data.png)

<br>
<hr>
<br>

2023 KSAE 대학생 자작자동차대회 기술아이디어 부문 금상, 2022 아주대학교 아주 훌륭한 SW융합인의 도전 최우수상 수상작입니다.

<div class='center'>
    <img src='/assets/images/works/telemetry/trophy.jpg' style='width: 48%'>
    <img src='/assets/images/works/telemetry/panel.jpg' style='width: 48%'>
</div>

<style>
img {
    max-height: none!important;
}
</style>
