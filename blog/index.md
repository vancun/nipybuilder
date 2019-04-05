---
layout: default
title: Blog
---
<h1>{{ page.title }}</h1>
<ul class="posts">

  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url | relative_url }}" title="{{ post.title }}">{{ post.title }}</a></li>
  {% endfor %}
    
</ul>