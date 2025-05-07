---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<!-- FILTRO -->
<div style="margin-bottom: 1em;">
  <input type="text" id="pub-search" placeholder="Cerca..." style="padding: 0.5em; width: 60%;">
  <select id="pub-year" style="padding: 0.5em; margin-left: 1em;">
    <option value="">Tutti gli anni</option>
    <option value="2025">2025</option>
    <option value="2024">2024</option>
    <option value="2023">2023</option>
    <option value="2022">2022</option>
    <!-- Aggiungi altri anni se necessario -->
  </select>
</div>


<ul id="pub-list">
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
</ul>
