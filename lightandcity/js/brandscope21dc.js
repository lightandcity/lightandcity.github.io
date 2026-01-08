(function(window, document, script, BrandScope, firstScript) {
  window.BrandScope = window.BrandScope || {
    init: function() {
      (window.BrandScope.q = window.BrandScope.q || []).push(['init'].concat(Array.prototype.slice.call(arguments)))
    },
    identify: function() {
      (window.BrandScope.q = window.BrandScope.q || []).push(['identify'].concat(Array.prototype.slice.call(arguments)))
    },
    track: function() {
      (window.BrandScope.q = window.BrandScope.q || []).push(['track'].concat(Array.prototype.slice.call(arguments)))
    },
    getImwebClientInfo: function() {
      (window.BrandScope.q = window.BrandScope.q || []).push(['getImwebClientInfo'].concat(Array.prototype.slice.call(arguments)))
    },
    sessionResetByLogout: function() {
      (window.BrandScope.q = window.BrandScope.q || []).push(['sessionResetByLogout'].concat(Array.prototype.slice.call(arguments)))
    },
  }
  BrandScope = window.BrandScope
  script = document.createElement('script')
  script.type = 'module'
  script.async = true
  script.src = (typeof TEST_SERVER !== 'undefined' && TEST_SERVER) ? ' : '
  firstScript = document.getElementsByTagName('script')[0]
  firstScript.parentNode.insertBefore(script, firstScript)
})(window, document);
(function initBrandScope() {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBrandScope);
    return;
  }
  const hasShopViewWidget = !!document.querySelector('[data-widget-type="shop_view"]');
  if (hasShopViewWidget) {
    return;
  }
  BrandScope.init({
    props: {
      ownership: 'behavior-tracking-analytics',
    }
  });
})()