var APP = function() {
  var appDefaultTabType = {
    'APP_TAB_WEB_VIEW_BACK': 'webViewBack',
    'APP_TAB_ALARM': 'alarm',
    'APP_TAB_MY': 'my'
  };
  var init = function() {
    setPullToRefresh();
  };
  var updateTabBadgeCnt = function(type, cnt) {
    if (IS_IOS_APP) {
      var data = {
        "method": "updateTabBadgeCnt",
        "type": type,
        "cnt": cnt
      };
      loadMethod(data);
    }
  };
  var changeTabIcon = function(type, icon_path) {
    var data = {
      "method": "changeTabIcon",
      "type": type,
      "icon_path": icon_path
    };
    loadMethod(data);
  };
  var disableTab = function(type, is_disable) {
    var data = {
      "method": "disableTab",
      "type": type,
      "is_disable": is_disable
    };
    loadMethod(data);
  };

  function loadMethod(data) {
    try {
      webkit.messageHandlers.imwebIosCallBack.postMessage(data);
    } catch (err) {}
  }
  var setPullToRefresh = function(is_enable) {
    is_enable = isBlank(is_enable) ? "Y" : is_enable;
    if (IS_APP) {
      if (IS_ANDROID_APP === "Y") {
        window.dozAndroidBridge.setPullToRefresh(is_enable);
      } else {
        var data = {
          "method": "setPullToRefresh",
          "is_enable": is_enable
        };
        loadMethod(data);
      }
    }
  };
  var reFresh = function() {
    location.reload();
  };
  return {
    'init': function() {
      init();
    },
    appDefaultTabType: appDefaultTabType,
    'updateTabBadgeCnt': function(type, cnt) {
      updateTabBadgeCnt(type, cnt);
    },
    'disableTab': function(type, is_disable) {
      disableTab(type, is_disable);
    },
    'changeTabIcon': function(type, icon_path) {
      changeTabIcon(type, icon_path);
    },
    'setPullToRefresh': function(isEnable) {
      setPullToRefresh(isEnable);
    },
    'reFresh': function() {
      reFresh();
    }
  };
}();