var SECURITY_PRIVACY = function() {
  var ONE_MINUTE = 60 * 1000;
  var TWO_MINUTES = 2 * 60 * 1000;
  var NEXT_ACTION_TIME_LOCAL_STORAGE_KEY = 'NEXT_ACTION_TIME';
  var event_setting_timer;
  var logout_warning_timer;
  var auto_logout_timer;
  var setAutoLogoutEvent = function(auto_logout_time) {
    if (IS_IE) {
      if (typeof event_setting_timer !== 'undefined') {
        clearTimeout(event_setting_timer);
      }
      if (typeof logout_warning_timer !== 'undefined') {
        clearTimeout(logout_warning_timer);
      }
      if (typeof auto_logout_timer !== 'undefined') {
        clearTimeout(auto_logout_timer);
      }
      window.addEventListener('storage', function(e) {});
    } else {
      deleteTimeout();
    }
    removeFocusListner();
    var next_action_time = new Date();
    next_action_time.setMinutes(next_action_time.getMinutes() + 1);
    LOCAL_STORAGE.setLocalStorage(NEXT_ACTION_TIME_LOCAL_STORAGE_KEY, next_action_time);
    event_setting_timer = setTimeout(function() {
      setActionEvent(auto_logout_time);
    }, ONE_MINUTE);
  };
  var openChangePasswordNotice = function(month_notice) {
    $.cocoaDialog.close();
    $.ajax({
      type: "POST",
      url: ("/ajax/change_password_notice.cm"),
      data: {
        month_notice: month_notice
      },
      dataType: "html",
      async: true,
      cache: false,
      success: function(html) {
        var $html = $(html);
        var change_password_btn = $html.find("._change_password_btn");
        var not_change_password_btn = $html.find("._not_change_password_btn");
        change_password_btn.off("click").on("click", function(e) {
          changePassword();
          e.preventDefault();
          return false;
        });
        not_change_password_btn.off("click").on("click", function(e) {
          notChangePassword();
          e.preventDefault();
          return false;
        });
        $.cocoaDialog.open({
          type: "admin_change_password",
          custom_popup: $html,
          "close_block": true
        });
      }
    });
  };

  function resetAutoLogoutEvent(auto_logout_time) {
    removeActionEvent();
    deleteTimeout(logout_warning_timer);
    deleteTimeout(auto_logout_timer);
    setAutoLogoutEvent(auto_logout_time);
  }

  function setActionEvent(auto_logout_time) {
    var action_time = LOCAL_STORAGE.getLocalStorage(NEXT_ACTION_TIME_LOCAL_STORAGE_KEY);
    if (new Date(action_time).getTime() <= new Date().getTime()) {
      logout_warning_timer = setTimeout(function() {
        removeActionEvent();
        showLogoutWarning(auto_logout_time);
      }, (auto_logout_time * ONE_MINUTE) - TWO_MINUTES);
      $(document).off("mousemove keydown").on("mousemove keydown", function() {
        removeActionEvent();
        deleteTimeout(logout_warning_timer);
        deleteTimeout(auto_logout_timer);
        setAutoLogoutEvent(auto_logout_time);
      });
    } else {
      $(document).off("focus").on("focus", function() {
        setAutoLogoutEvent(auto_logout_time);
      });
    }
  }

  function showLogoutWarning(auto_logout_time) {
    auto_logout_timer = setTimeout(function() {
      removeActionEvent();
      $.cocoaDialog.hide();
      LOCAL_STORAGE.setLocalStorage("IS_AUTO_LOGOUT", "Y");
      location.href = "/logout.cm";
    }, ONE_MINUTE);
    showAutoLogoutAlert(auto_logout_time);
  }

  function showAutoLogoutAlert(auto_logout_time) {
    $.ajax({
      type: "POST",
      url: ("/ajax/auto_logout_alert.cm"),
      data: {
        auto_logout_time: auto_logout_time
      },
      dataType: "html",
      async: false,
      cache: false,
      success: function(html) {
        $.cocoaDialog.open({
          type: "site_alert",
          custom_popup: html,
          "close_block": true
        });
      }
    });
  }

  function deleteTimeout(timer_id) {
    if (!timer_id) {
      clearTimeout();
    } else {
      clearTimeout(timer_id);
    }
  }

  function removeActionEvent() {
    $(document).off("mousemove keydown");
  }

  function removeFocusListner() {
    $(document).off("focus");
  }

  function changePassword() {
    var data = $("#change_password_notice").serializeObject();
    $.ajax({
      type: "POST",
      url: ("/ajax/change_password.cm"),
      data: data,
      dataType: "json",
      async: false,
      cache: false,
      success: function(res) {
        if (res.msg === "SUCCESS") {
          window.location.reload();
        } else {
          var join_form = $("#change_password_notice");
          var object = join_form.find("._" + res.type);
          join_form.find("._item").toggleClass("triangle", false);
          join_form.find("._msg").text("");
          object.toggleClass("triangle", true);
          object.find("input").focus();
          object.find("._msg").text(res.msg);
        }
      }
    });
  }

  function notChangePassword() {
    $.ajax({
      type: "POST",
      url: ("/ajax/not_change_password.cm"),
      dataType: "json",
      async: false,
      cache: false,
      success: function(res) {
        if (res.msg === "SUCCESS") {
          $.cocoaDialog.close();
        }
      }
    });
  }
  return {
    "setAutoLogoutEvent": function(auto_logout_time) {
      setAutoLogoutEvent(auto_logout_time);
    },
    "openChangePasswordNotice": function(month_notice) {
      openChangePasswordNotice(month_notice);
    },
    "resetAutoLogoutEvent": function(auto_logout_time) {
      resetAutoLogoutEvent(auto_logout_time);
    }
  };
}();