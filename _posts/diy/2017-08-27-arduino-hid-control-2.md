---
title: 아두이노로 마우스 & 키보드 입력 제어 (2)
description: HoodLoader2 부트로더 굽기
category: diy
assets: /assets/posts/diy/2017-08-27-arduino-hid-control-2
image: /assets/posts/diy/2017-08-27-arduino-hid-control-2/main.png
layout: post
---
앞선 글 [(1) HID 장치가 뭐길래](https://luftaquila.io/blog/diy/arduino-hid-control-1/){:class="link"}에서 대체 왜 삽질을 해야 하는지 이유를 알아보았으니, 이제 실제로 삽질을 할 차례다.  
먼저 이 글의 내용은 모두 [HoodLoader2 GitHub](https://github.com/NicoHood/HoodLoader2/wiki){:target="_blank"}{:class="external"}의 내용을 옮긴 것임을 밝힌다.

<br>
##### 목차
[(1) HID 장치가 뭐길래](https://luftaquila.io/blog/diy/arduino-hid-control-1/){:class="link"}  
[(2) HoodLoader2](https://luftaquila.io/blog/diy/arduino-hid-control-2/){:class="link"}  
[(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}

<br>
#### 준비물
부트로더를 올리는 데는 아두이노 보드 1개와 <dfn>100nF</dfn> 커패시터, 또는 아두이노 보드 2개가 필요하다.
  
<div class='center'><img src='{{ page.assets }}/1.png'></div>
<dfn>100nF</dfn> 커패시터가 있다면 보드가 한 개만 있어도 된다. 위와 같이 연결한다.

<div class='center'><img src='{{ page.assets }}/2.png'></div>
아니라면, 아두이노 두 대를 준비해 위와 같이 연결한다.
<br>
#### 전투 개시
배선이 끝났으면 코드를 업로드할 차례다. 아두이노에는 아직 전원을 공급하지 않는다.

[<i class='fas fa-download'></i> HoodLoader2.zip]({{ page.assets }}/HoodLoader2.zip)

Hoodloader2 부트로더를 다운로드하고, 압축을 풀어 아두이노 스케치 설치 폴더 아래의 hardwares 폴더 안으로 이동시킨다.

다음으로 avr/examples/Installation_Sketch 폴더에서 `Installation_Sketch.ino` 파일을 연다. 이 파일이 바로 부트로더 업로드 코드이다. 코드 맨 앞에는 이런 부분이 있다.

<div class='center'><img src='{{ page.assets }}/3.png'></div>

부트로더를 바꿀 보드의 MCU에 따라 하이라이트 된 부분을 밑의 숫자로 바꾸면 된다. 예를 들면, 아두이노 우노의 경우 USB MCU가 Atmega16u2이므로 하이라이트 된 부분을 3으로 바꾸면 된다. 유의할 점은 USB MCU의 모델명을 찾아야 한다는 것이다. I/O MCU의 모델명을 찾으면 안 된다.

수정을 마쳤으면 업로드하기 전에 배선이 올바른지 다시 한 번 확인하고, 아두이노를 컴퓨터와 연결하고 업로드한다. 업로드 및 작업 진행 중에 배선을 바꾸면 안 된다. 아두이노가 그냥 에폭시 덩어리로 변하는 광경을 지켜봐야 할 수도 있다.

코드를 업로드하면 부트로더를 쓰는 작업은 자동으로 진행된다. 전원 공급이 시작되고 10초가 지나면 부트로더 굽기가 이루어진다. 진행 상황을 보려면 시리얼 모니터를 115200 보드 레이트로 띄우면 된다. 모든 작업이 끝나면 시리얼 모니터에 `programming finished` 메시지가 뜨면서 빌트인 LED가 0.1초마다 깜빡인다. USB를 뽑으면 된다.

만약 LED가 1초에 한 번씩 느리게 깜빡인다면 업로드에 실패했다는 뜻이다. 실패한 경우 10초마다 재시도하는데, 시작한지 1~2분이 지나도 작업이 완료되지 않으면 일단 USB를 뽑는다. 일부 호환 보드에서 ISP 핀이 180도 돌아간 상태로 배열되어 있는 경우가 있다고 하니, 아래 사진을 참고해서 배선을 바꾸고 다시 시도해 보자. 정상적으로 진행된다면 작업은 1분 미만으로 완료된다.

<div class='center'><img src='{{ page.assets }}/main.png'></div>

설치가 제대로 됐는지 확인하려면 `장치 및 프린터` 에서 아두이노를 찾아 속성을 확인하면 된다.

<div class='center'><img src='{{ page.assets }}/4.png'></div>

사진과 같이 모델명에 HoodLoader2라는 문구가 붙고, 세부 속성의 하드웨어 ID에 REV_0203 또는 0205가 붙으면 잘 된 것이다. 리눅스의 경우는 아래와 같은 방법으로 확인한다.
```bash
# The easiest way to get information about your arduino
# is to run the command below
# and then plug in you arduino afterwards.
# Make sure it is in bootloader mode (double tab reset)
udevadm monitor --subsystem-match=usb --property | grep -E "REVISION|VENDOR|MODEL"

# sample output:
ID_MODEL_FROM_DATABASE=Uno R3 (CDC ACM)
ID_VENDOR_FROM_DATABASE=Arduino SA
ID_MODEL_FROM_DATABASE=Uno R3 (CDC ACM)
ID_VENDOR_FROM_DATABASE=Arduino SA
ID_MODEL=HoodLoader2_Uno
ID_MODEL_ENC=HoodLoader2\x20Uno
ID_MODEL_FROM_DATABASE=Uno R3 (CDC ACM)
ID_MODEL_ID=0043
ID_REVISION=0205
ID_VENDOR=NicoHood
ID_VENDOR_ENC=NicoHood
ID_VENDOR_FROM_DATABASE=Arduino SA
ID_VENDOR_ID=2341

# Use this to check all connected devices
lsusb -d 2341:

# 16u2 in bootloader mode example:
Bus 003 Device 122: ID 2341:0043 Arduino SA Uno R3 (CDC ACM)

# 16u2 running sketch example:
Bus 003 Device 121: ID 2341:484c Arduino SA

# To check if the connected device is a HoodLoader device
# Plug your Arduino in and run:
dmesg | tail

# example output:
[13129.089557] usb 3-10.4.4: new full-speed USB device number 122 using xhci_hcd
[13129.195962] usb 3-10.4.4: New USB device found, idVendor=2341, idProduct=0043
[13129.195971] usb 3-10.4.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[13129.195975] usb 3-10.4.4: Product: HoodLoader2 Uno
[13129.195979] usb 3-10.4.4: Manufacturer: NicoHood
[13129.196258] usb 3-10.4.4: ep 0x82 - rounding interval to 1024 microframes, ep desc says 2040 microframes
[13129.197168] cdc_acm 3-10.4.4:1.0: ttyACM0: USB ACM device

# If you upload programs via AVR-Dude you can see the version number (might need verbose output):
Found programmer: Id = "HL2.0.5"; type = S
```
<br>
#### 뒷수습
윈도우 7 또는 8 사용자의 경우 [Software Installation](https://github.com/NicoHood/HoodLoader2/wiki/Software-Installation){:target="_blank"}{:class="external"}을 참고해 `Teensy driver`를 설치해야 한다. 성공적으로 설치를 마쳤다면 이제야 드디어 조이스틱을 만들 차례다. 삽질의 길은 멀고도 험난하다. 
[(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}
<br>
##### 목차
[(1) HID 장치가 뭐길래](https://luftaquila.io/blog/diy/arduino-hid-control-1/){:class="link"}  
[(2) HoodLoader2](https://luftaquila.io/blog/diy/arduino-hid-control-2/){:class="link"}  
[(3) 조이스틱 제작](https://luftaquila.io/blog/diy/arduino-hid-control-3/){:class="link"}