var SITE_SEARCH = function() {
  var init = function() {
    const $numericInput = $('input[type=text][data-inputmode=numeric]');
    const $numericInputMin = $numericInput.filter('[data-numeric-type=min]');
    const $numericInputMax = $numericInput.filter('[data-numeric-type=max]');
    $numericInput.on('input', function(e) {
      const refineValue = e.target.value.replace(/[^\d.]/g, '').replace(/^\./, '').replace(/\.{2,}/g, '.').replace(/(\d*\.\d*)\.(\d*)/, '$1$2');
      e.target.value = refineValue.replace(/(\d+\.?\d{0,2}).*/, '$1');
    });
    $numericInput.on('blur', function(e) {
      const refineValue = e.target.value.replace(/\.$/, '');
      const numericValue = parseFloat(refineValue);
      e.target.value = Number.isNaN(numericValue) ? '' : numericValue;
    });
    $numericInput.on('keydown', function(e) {
      if (e.key === 'Enter') {
        e.target.blur();
        $('#s_form').submit();
      }
    });
    $numericInputMin.on('blur', function(e) {
      const minValue = parseFloat(e.target.value);
      const maxValue = parseFloat($numericInputMax.val());
      if (Number.isNaN(minValue) || Number.isNaN(maxValue)) {
        return;
      }
      e.target.value = Math.min(Math.max(0, minValue), maxValue);
    });
    $numericInputMax.on('blur', function(e) {
      const minValue = parseFloat($numericInputMin.val());
      const maxValue = parseFloat(e.target.value);
      if (Number.isNaN(minValue) || Number.isNaN(maxValue)) {
        return;
      }
      e.target.value = Math.max(minValue, maxValue);
    });
  }
  var openSearch = function(data) {
    $.cocoaDialog.close();
    var $s_form = $('#s_form');
    var keyword = '';
    var type = '';
    if ($s_form.length > 0) {
      keyword = $s_form.find('input[name=keyword]').val().trim();
      type = $s_form.find('input[name=type]').val();
    }
    $.ajax({
      type: 'POST',
      data: {
        'keyword': keyword,
        'type': type,
        'data': data
      },
      url: ('/dialog/search.cm'),
      dataType: 'html',
      async: true,
      cache: false,
      success: function(html) {
        var $html = $(html);
        $.cocoaDialog.open({
          type: 'widget_search',
          custom_popup: $html
        });
        $html.find('input[name=keyword]').off("focus").on("focus", function(e) {
          if (this.createTextRange) {
            var range = this.createTextRange();
            range.move('character', this.value.length);
            range.select();
          } else if (this.selectionStart || this.selectionStart == '0') this.selectionStart = this.value.length;
        });
      }
    });
  };
  $.urlParam = function(name) {
    var results = new RegExp('[\?&amp;]' + name + '=([^&amp;#]*)').exec(window.location.href);
    return results[1] || 0;
  }
  var search = function() {
    var $s_form = $('#s_form');
    var $_keyword = $s_form.find('input[name=keyword]');
    $_keyword.val($_keyword.val().trim());
    var $_category_code = $s_form.find('select[name=category_code]');
    if ($_category_code.length) {
      const val = $_category_code.val();
      if (val === '') {
        $_category_code.prop('disabled', true);
      }
    }
    var $_min_price = $s_form.find('input[name=min_price]');
    if ($_min_price.length) {
      const val = $_min_price.val().trim();
      if (val === '') {
        $_min_price.prop('disabled', true);
      } else {
        $_min_price.val(val);
      }
    }
    var $_max_price = $s_form.find('input[name=max_price]');
    if ($_max_price.length) {
      const val = $_max_price.val().trim();
      if (val === '') {
        $_max_price.prop('disabled', true);
      } else {
        $_max_price.val(val);
      }
    }
    $s_form.submit();
    $_category_code.prop('disabled', false);
    $_min_price.prop('disabled', false);
    $_max_price.prop('disabled', false);
  };
  var inlineSearch = function(code) {
    var $s_form = $('#inline_s_form_' + code);
    var $_keyword = $s_form.find('input[name=keyword]');
    $_keyword.val($_keyword.val().trim());
    $s_form.submit();
  };
  var searchDialog = function() {
    var $sd_form = $('#sd_form');
    var $_keyword = $sd_form.find('input[name=keyword]');
    $_keyword.val($_keyword.val().trim());
    $sd_form.submit();
  };
  var changeType = function(type) {
    var $s_form = $('#s_form');
    var $type = $s_form.find('._type');
    $type.val(type);
    $s_form.submit();
  };
  var changeSort = function(type) {
    var $s_form = $('#s_form');
    var $sort = $s_form.find('._sort');
    $sort.val(type);
    $s_form.submit();
  };
  var popularSearch = function(code, keyword) {
    var $s_form = $('#inline_s_form_' + code);
    var $_keyword = $s_form.find('input[name=keyword]');
    $_keyword.val(keyword);
    $s_form.submit();
    setTimeout(() => {
      $_keyword.val('')
    }, 0);
  }
  return {
    'init': function() {
      init();
    },
    'inlineSearch': function(code) {
      inlineSearch(code);
    },
    'openSearch': function(data) {
      openSearch(data);
    },
    'search': function() {
      search();
    },
    'searchDialog': function() {
      searchDialog();
    },
    'changeType': function(type) {
      changeType(type);
    },
    'changeSort': function(type) {
      changeSort(type);
    },
    'popularSearch': function(code, keyword) {
      popularSearch(code, keyword);
    }
  }
}();