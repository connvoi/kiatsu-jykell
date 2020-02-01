---
layout: default
---
{% for g in site.data.group %}
<div class="container mt-3">
  <h3>
    <strong>{{ g.group_name }}</strong>
  </h3>
  <div class="row mt-3">
    {% for item in site.data.citylist %}
      {% if item.group == g.group %}
          <div class="col-4 col-sm-4">
              <a href="{{site.baseurl}}city/{{ item.nameid }}.html" class="cyan-text"><button class="btn btn-outline-cyan">{{ item.name }}</button></a>
          </div>
      {% endif %}
    {% endfor %}
  </div>
</div>
{% endfor %}