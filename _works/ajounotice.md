---
title: 아주대학교 공지사항 카톡 봇
description: 크롤링과 세션 유지, 카톡 메시지 전송
date: 2021-11-08
assets: /assets/images/works/ajounotice
image: /assets/images/works/ajounotice/main.jpg
layout: docs
---
[GitHub 저장소](https://github.com/luftaquila/ajounotice){:target="_blank"}{:class='link'}
&emsp;
[서비스 오픈카톡방](https://open.kakao.com/o/g8BxtUId){:target="_blank"}{:class='external'}  
<br>
아주대학교 홈페이지에서 공지사항을 크롤링한 후, 카카오링크 서비스를 이용해 보기 좋게 오픈채팅방에 전달하는 봇입니다.  

Node.js로 작성되었습니다.  
- 로그인된 사용자에게만 보이는 게시물을 불러오기 위해 Selenium으로 로그인 세션이 만료될 때마다 다시 로그인합니다.  
- 공지사항 목록과 게시글 세부 내용(이미지 링크 등)을 불러오는 데는 axios를 사용합니다.  
- 카카오링크 전송에는 [node-kakaolink](https://github.com/archethic/node-kakaolink){:target="_blank"}{:class='external'}를 이용합니다.  
- node-schedule 모듈을 통해 평일 09시부터 20시까지에만 5분에 한 번씩 주기적으로 크롤링을 수행합니다.
- [ajoumeow](https://luftaquila.io/works/ajoumeow/){:target="_blank"}{:class='link'} 서비스의 날씨 크롤러의 데이터를 이용해 아주대학교 날씨를 알립니다.
  <img src='{{ page.assets }}/1.jpg'>
- 아주대학교 학사일정 API를 호출해 오늘 날짜가 포함되는 학사 일정을 모아 알립니다.
  <img src='{{ page.assets }}/2.jpg'>