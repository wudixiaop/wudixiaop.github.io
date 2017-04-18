{% if not (theme.duoshuo and theme.duoshuo.shortname) and not theme.duoshuo_shortname and not theme.disqus_shortname %}

  {% if theme.gentie_productKey %}
    {% set gentie_productKey = theme.gentie_productKey %}
    <div id="cloud-tie-wrapper" class="cloud-tie-wrapper"></div>
    <script>
      var cloudTieConfig = {
        url: document.location.href, 
        sourceId: "",
        productKey: "{{gentie_productKey}}",
        target: "cloud-tie-wrapper"
      };
    </script>
    <script src="https://img1.cache.netease.com/f2e/tie/yun/sdk/loader.js"></script>
  {% endif %}

{% endif %}