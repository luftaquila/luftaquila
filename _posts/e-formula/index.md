### 목차
<div style="margin-left: 2rem;">
    {% for post in site.categories['e-formula'] reversed %}
    <div><a style='font-weight: bold' href="{{post.url}}">{{post.title}}</a>{% if post.url == page.url %} ← 현재 글{% endif %}</div>
    {% endfor %}
    <div><a style='font-weight: bold' href="https://github.com/luftaquila/monolith" target='_blank' class='forceinternal'>+) 오픈소스 DIY 데이터로거 모노리스</a></div>
</div>
<br>
