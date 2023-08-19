### 목차
<div style="margin-left: 2rem;">
    {% for post in site.categories['e-formula'] reversed %}
    <div><a style='font-weight: bold' href="{{post.url}}">{{post.title}}</a>{% if post.url == page.url %} ← 현재 글{% endif %}</div>
    {% endfor %}
    추가 중입니다.
</div>
<br>
