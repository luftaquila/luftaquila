---
title: 야옹이선술집 2020
description: 아주대학교 축제 주점 야옹이선술집 주문서 관리 서비스
date: 2021-02-13
image: /assets/images/works/ajoupub/main.png
layout: post
---
<br>
<h3>서비스 링크</h3>
<a class='content-link font-bold' target="_blank" href='/ajoupub?table=031'><i class='fas fa-link'></i> 테이블</a>
&emsp;
<a class='content-link font-bold' target="_blank" href='/ajoupub/staff'><i class='fas fa-link'></i> 스태프</a>
&emsp;
<a class='content-link font-bold' target="_blank" href='/ajoupub/kitchen'><i class='fas fa-link'></i> 주방</a>
&emsp;
<a class='content-link font-bold' target="_blank" href='/ajoupub/statistics'><i class='fas fa-link'></i> 통계</a>
&emsp;
<a class='content-link font-bold' target="_blank" href='https://github.com/luftaquila/ajoupub'><i class='fas fa-link'></i> GitHub 저장소</a>

<hr style='border-color: darkgray; margin-top: 1rem;'>

학교 축제 주점 운영 시 수기로 주문을 관리하고 매출을 계산하는 것을 자동화하기 위해 개발했습니다.  
손님 테이블과 홀서빙 스태프, 주방이 서버와 소켓 통신으로 연결되어 실시간으로 주문을 관리합니다. 

1. 손님이 테이블 메뉴판에 인쇄된 QR코드를 스캔해 주문서 페이지에 접속합니다.

1. 손님이 메뉴를 고르고 주문하면,  
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111717.png'>
  * 모든 스태프에게 주문 알림이 전송됩니다.
  * 해당 테이블이 결제 대기 상태로 하이라이트됩니다.  
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111735.png'>

1. 스태프가 결제를 인증하면,  
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111748.png'>
  * 해당 테이블이 음식 대기 상태로 하이라이트됩니다.  
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111825.png'>
  * 주방에 주문 알림이 전송되고, 자동으로 대기열에 주문 내용이 추가됩니다.
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111837.png'>
  * 손님 주문서 페이지의 메뉴별 예상 소요시간이 자동으로 조정됩니다.
  
  
1. 스태프가 음식을 전달하면,  
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111911.png'>
  * 해당 테이블의 하이라이트 상태가 해제됩니다.
  * 주문 대기열에서 해당 내용이 사라지고 예상 소요시간이 조정됩니다.
  
1. 스태프와 주방 관리자는,
  * 한 눈에 대기열 현황을 파악할 수 있습니다.  
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111951.png'>
  <img src='/assets/images/works/ajoupub/Screenshot_20210213-111955.png'>
  
1. 주방 관리자는,
  * 메뉴별 소요 시간을 수동으로 조정할 수 있습니다.
  * 메뉴별 Sold Out 상태를 켜고 끌 수 있습니다.
