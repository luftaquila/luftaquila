---
title: 이어폰 분배기 DIY
description: 3D 모델링 초심자의 실수
category: diy
assets: /assets/posts/diy/2017-12-26-earphone-splitter-diy
image: /assets/posts/diy/2017-12-26-earphone-splitter-diy/main.png
layout: post
---
흔히들 이어폰 분배기나 허브라고 부르는 물건을 만들기도 했다. 최근에 3D 모델링을 부족하게나마 독학했으니 배운 걸 써먹어 볼 겸 3D프린터로 케이스를 뽑아 깔끔하게 만들어보기로 했다.

이어폰 단자 Male 한 개, Female 두 개를 핀 맞춰서 연결만 잘 해 주면 되는 굉장히 단순한 구조다. 외형을 그럴싸하게 만드는 게 중요하다는 말이다. 이어폰 단자는 안 쓰는 핸드폰과 이어폰들에서 뜯어서 조달했다.

<div class='center'><img src='{{page.assets}}/1.png'></div>

그리하여 탄생한 인생 첫 3D 모델링이다. 케이스 만들어서 드릴로 구멍 뚫고 부품 넣어 연결하고 뚜껑 닫으면 되겠지라고 안일한 생각을 했다. 망하면서 배우는 법이다.

<div class='center'>
  <img src='{{ page.assets }}/2.png' style='width: 45%'>
  <img src='{{ page.assets }}/3.png' style='width: 45%'>
</div>

망했다. 이걸로 3D 모델링이 그냥 물건을 예쁘게 뽑아내는 게 아니라는 걸 알게 됐다. 3D 모델링은 기계가 어디까지 해낼 수 있는지를 상상 속의 모델링과 저울질하는 현실과의 타협이다. 3D 프린터의 특성을 전혀 고려하지 않았다.  
3D프린터의 노즐 직경은 0.4mm인데, 외벽 두께를 아무 생각 없이 1mm로 설정했다. 결과적으로 노즐이 두 번 움직여 0.8mm를 쌓은 후, 나머지 0.2mm를 쌓기 위해 지그재그로 드드드드 하고 움직이며 출력물을 망쳐 버렸다. 외벽이 빨래판도 아니고 우둘투둘하다. 그래서 외벽 두께를 0.4mm의 배수인 1.2mm로 수정했다.

<div class='center'><img src='{{page.assets}}/4.png'></div>

출력물의 퀄리티는 훨씬 나아졌다. 하지만 생각치도 못한 곳에서 문제가 생겼다. 드릴로 구멍을 뚫으면 뿅 하고 예쁘게 뚫릴 줄 알았건만 윗부분이 거의 부러지다시피 했다. 뚜껑을 덮는 방식 또한 출력물이 얇으니 똑바르게 출력되지 않아 포기하기로 했다.

<div class='center'><img src='{{page.assets}}/5.png'></div>

그래서 한 번 더 수정을 거쳤다. 외벽 두께는 당연히 1.2mm로 설정했고, 얇게 뽑으면 생기는 문제 때문에 정확히 반으로 나누어 두 개를 뽑아 합치기로 했다. 반만 출력하니 구멍에 서포트를 세울 필요도 없다.

<div class='center'>
  <img src='{{ page.assets }}/6.png' style='width: 45%'>
  <img src='{{ page.assets }}/7.png' style='width: 45%'>
</div>

왼쪽이 이 모델링으로 출력한 출력물이다. 오른쪽 사진은 이걸 뽑기 위해 시도한 시행착오들이다. 3D프린터가 어떻게 쓰는 물건인지 슬슬 감이 오기 시작했다.

<div class='center'>
  <img src='{{ page.assets }}/8.png' style='width: 30%'>
  <img src='{{ page.assets }}/9.png' style='width: 30%'>
  <img src='{{ page.assets }}/10.png' style='width: 30%'>
</div>

이제 케이스가 준비되었으니 부품을 배치한다. 공간이 좁아 납땜이 쉽지 않았다. 어쨌거나 배선을 마치고 순간접착제를 이용해 부품을 고정시킨 다음, 뚜껑을 닫았다. 출력물 마감이 깔끔하지 않아 사포로 조금 갈아 주었다.

<div class='center'><img src='{{page.assets}}/main.png'></div>
완성한 모습이다. 양 쪽 모두 문제없이 출력이 잘 나온다.

