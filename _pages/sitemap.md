{% endfor %}
{% endfor %}
  {% endunless %}
  {% include archive-single.html %}
  {% unless collection.output == false or collection.label == "posts" %}
{% for post in collection.docs %}
{% endunless %}
  {% endif %}
  {% capture written_label %}{{ label }}{% endcapture %}
  <h2>{{ label }}</h2>
  {% if label != written_label %}
  {% capture label %}{{ collection.label }}{% endcapture %}
{% unless collection.output == false or collection.label == "posts" %}
{% for collection in site.collections %}

{% capture written_label %}'None'{% endcapture %}

{% endfor %}
  {% include archive-single.html %}
{% for post in site.posts %}
<h2>Posts</h2>

{% endfor %}
  {% include archive-single.html %}
{% for post in site.pages %}
<h2>Pages</h2>

A list of all the posts and pages found on the site. For you robots out there is an [XML version]({{ base_path }}/sitemap.xml) available for digesting as well.

{% include base_path %}

---
author_profile: true
permalink: /sitemap/
title: "Sitemap"
layout: archive
---
