var ZIPCODE_DAUM = function() {
  var $zipcodeContainer, $zipcodeLayer;
  var $postCodeInput;
  var $addressInput;
  var $subAddress;
  var onComplete;
  var onStart;
  var onShow;
  var onClose;
  var type;
  var $openKakaoAddressButton;
  var option = {
    'addr_container': null,
    'addr_pop': null,
    'post_code': null,
    'addr': null,
    'height': '',
    'open_button': null,
    attachShowEventOnInput: true,
    hideWhenClickOutside: true,
  };
  var init = function(data) {
    option = $.extend(option, data);
    $zipcodeContainer = option.addr_container;
    $zipcodeLayer = option.addr_pop;
    $postCodeInput = option.post_code;
    $addressInput = option.addr;
    $openKakaoAddressButton = option.open_button;
    $subAddress = option.sub_addr;
    onComplete = option.onComplete;
    onShow = option.onShow;
    onStart = option.onStart;
    onClose = option.onClose;
    if (typeof onStart == 'function') {
      onStart();
    }
    if ($openKakaoAddressButton !== undefined && $openKakaoAddressButton !== null) {
      $openKakaoAddressButton.off('click').on('click', function() {
        showFindAddress();
      });
    }
    if ($postCodeInput !== undefined && $postCodeInput !== null) {
      $postCodeInput.off('click').on('click', function() {
        showFindAddress();
      });
    }
    if ($subAddress !== undefined && $subAddress !== null) {
      $subAddress.off('click').on('click', function() {
        showFindAddress();
      });
    }
    if (option.attachShowEventOnInput) {
      $addressInput.off('click').on('click', function() {
        showFindAddress();
      });
    }
  };
  var hideFindAddress = function() {
    $zipcodeContainer.hide();
    $zipcodeContainer.parent('div._widget_data').removeClass('address-open');
    if (typeof onClose == 'function') {
      onClose();
    }
  };
  var showFindAddress = function() {
    new daum.Postcode({
      oncomplete: function(data) {
        var fullAddr = data.address;
        var extraAddr = '';
        if (data.addressType === 'R') {
          if (data.bname !== '') {
            extraAddr += data.bname;
          }
          if (data.buildingName !== '') {
            extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
          }
          fullAddr += (extraAddr !== '' ? ' (' + extraAddr + ')' : '');
        }
        $postCodeInput.val(data.zonecode);
        $addressInput.val(fullAddr);
        hideFindAddress(data);
        onComplete(data, fullAddr);
      },
      width: '100%',
      height: option.height
    }).embed($zipcodeLayer.get(0));
    $zipcodeContainer.show();
    $zipcodeContainer.parent('div._widget_data').addClass('address-open');
    if (typeof onShow == 'function') {
      onShow();
    }
    if (option.hideWhenClickOutside) {
      $(document).find('body').mousedown(function() {
        hideFindAddress();
      });
    }
  };
  return {
    'init': function(data) {
      init(data);
    },
    'showFindAddress': function() {
      showFindAddress();
    },
    'hideFindAddress': function() {
      hideFindAddress();
    }
  }
};