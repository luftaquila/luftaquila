---
title: E-포뮬러 전기시스템 제작기
description: 3. 시스템 제원 - 케이블 핀맵
category: e-formula
assets: /assets/posts/e-formula/2022-05-03-specifications-cables
image: /assets/posts/e-formula/2022-05-03-specifications-cables/main.png
layout: post
published: false
---

### 목차
<div style="margin-left: 2rem;">
<ol>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/introduction/">들어가며</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/hv-introduction/">HV 시스템 개요</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/lv-introduction/">LV 시스템 개요</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/specifications-pinout/">시스템 제원 - 부품 스펙 및 핀맵</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/specifications-cables/">시스템 제원 - 케이블 핀맵</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/hv-detail/">HV 시스템 세부사항</a></li>
<li><a class='link' href="https://luftaquila.io/blog/e-formula/lv-detail/">LV 시스템 세부사항</a></li>
</ol>
</div>
<br>

### Cables
#### BATTERY PACK ↔ SHUTDOWN

| Socket | Plug | CABLE | Plug | Socket |
|:-:|:-:|:-:|:-:|:-:|
|||BATTERY PACK ↔ SHUTDOWN|||

<br>

|BATTERY PACK|↔|SHUTDOWN|
|:----------:|:-:|:-------:|
|LV||LV|
|GND||GND|
|AIR+_ACTIVE||AIR+_ACTIVE|
|AIR-_ACTIVE||LV_ACTIVE|
|IMD_FAULT||IMD_FAULT|
|BMS_FAULT||BMS_FAULT|

<br>
<hr>

#### BATTERY PACK ↔ INVERTER

| Socket | Plug | CABLE | Plug | Socket |
|:-:|:-:|:-:|:-:|:-:|
|||BATTERY PACK ↔ INVERTER|||

<br>

|BATTERY PACK|↔|INVERTER|
|:----------:|:-:|:-------:|
|PRECHARGE||PRECHARGE|

<br>
<hr>

#### BATTERY PACK ↔ DASHBOARD

| Socket | Plug | CABLE | Plug | Socket |
|:-:|:-:|:-:|:-:|:-:|
|||BATTERY PACK ↔ DASHBOARD|||

<br>

|BATTERY PACK|↔|DASHBOARD|
|:----------:|:-:|:-------:|
|CAN_H||CAN_H|
|CAN_L||CAN_L|

<br>
<hr>
