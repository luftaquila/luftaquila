---
title: E-포뮬러 전기시스템 제작기
description: 3. 시스템 제원 - 부품 스펙 및 핀맵
category: e-formula
assets: /assets/posts/e-formula/2022-04-05-specifications-pinout
image: /assets/posts/e-formula/2022-04-05-specifications-pinout/main.png
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

### PARTS
#### 1. BMS

|Spec|Value|
|:--:|:---:|
|Current|~170mA|
|FAULT|`#8 Discharge Enable` HIGH OK, LOW FAIL|
|Connector|독자규격 / 제공됨|

##### Pinout

|#|DESCRIPTION|
|:-:|:-------:|
|2|Ready Power|
|7|Discharge Enable|
|10|Fan Enable|
|12|GND|
|18|CAN1_H|
|19|CAN1_L||
|3|Charge Power|
|6|Charger Safety|
|8|Charge Enable|
|23|Multi Purpose Output 1|
|24|Multi Purpose Output 4|
|13|Multi Purpose Input 1|
|14|Multi Purpose Input 2|
|9|Multi Purpose Input 3|

<br>
<hr>

#### 2. IMD

|Spec|Value|
|:--:|:---:|
|Current|~150mA|
|FAULT|`#8 OK_HS` HIGH OK, LOW FAIL|

##### Connectors

|수량|모델명|상대물 모델명|
|:-:|:-------:|:-------:|
|1x|2-1445088-8|1445022-8|
|2x|2-1445088-2|1445022-2|

##### Pinout

|#|DESCRIPTION|
|:-:|:-------:|
|1|Kl.31 GND|
|2|Kl.15 Supply Voltage|
|3|Kl.31 GND|
|4|kl.31 GND(Separaged line)|
|8|OK_HS Status Output|

<br>
<hr>

#### 3. Inverter

|Spec|Value|
|:--:|:---:|
|Current|~2.5A|

##### Connectors

|수량|모델명|상대물 모델명|
|:-:|:-------:|:-------:|
|1x J1|776164-1||
|1x J2|770680-1||

##### Pinout

|#(J1)|DESCRIPTION|
|:-:|:-------:|
|||

<br>

|#(J2)|DESCRIPTION|
|:-:|:-------:|
|||

<br>
<hr>

#### 4. ENERGY METER

|Spec|Value|
|:--:|:---:|
|Current|~ 200mA(예상)|

##### Connectors

|수량|모델명|상대물 모델명|
|:-:|:-------:|:-------:|
|1x|T4145415051-011||
|1x|0039012026||

##### Pinout

|#(T4145415051-011)|DESCRIPTION|
|:-:|:-------:|
|1|LV Power|
|2|GND|

<br>

|#(0039012026)|DESCRIPTION|
|:-:|:-------:|
|1|HV+|
