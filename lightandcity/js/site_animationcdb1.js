const SITE_ANIMATION = (() => {
  const body = document.body;
  const widgets = body.querySelectorAll('div[doz_type="widget"]');
  const aniClass = 'ds_animated';
  const init = (dsAnimation, load) => {
    document.addEventListener('DOMContentLoaded', () => {
      startAnimation(dsAnimation, load);
    });
  };
  const addCustomListener = (eventType, element, widgetKey, callback) => {
    const eventName = `${eventType}.${widgetKey}`;
    element.addEventListener(eventType, callback);
    return {
      eventName,
      eventType,
      element,
      callback
    };
  };
  const startAnimation = (dsAnimation, load) => {
    widgets.forEach(widget => {
      const widgetData = widget.querySelector('._widget_data');
      if (!widgetData) return;
      if (widgetData.classList.contains('_ds_animated_except')) return;
      if (dsAnimation === 'Y') {
        widgetData.classList.add(aniClass);
      } else if (!widgetData.classList.contains('wg_animated')) {
        return;
      }
      const widgetKey = widget.id;
      if (dsAnimation === 'Y' && load === 'Y') {
        scrollAnimation(widget, dsAnimation, "N");
      }
      const onScrollOrResize = () => {
        setTimeout(() => {
          scrollAnimation(widget, dsAnimation, load);
        }, 100);
      };
      addCustomListener('load', window, widgetKey, onScrollOrResize);
      addCustomListener('resize', window, widgetKey, onScrollOrResize);
      addCustomListener('scroll', window, widgetKey, onScrollOrResize);
    });
  };
  const scrollAnimation = (widget, dsAnimation, load) => {
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    const bottomOfWindow = window.scrollY + windowHeight;
    let bottomOfObject = widget.getBoundingClientRect().top + window.scrollY;
    let deviceType = windowWidth < 992 ? 'mobile' : 'pc';
    if (windowWidth <= 1024 && windowWidth >= 767) {
      const offset = widget.getBoundingClientRect().top - document.body.getBoundingClientRect().top;
      bottomOfObject = offset * 0.85;
    }
    let obj = widget.querySelector('._widget_data[data-widget-parent-is-mobile="N"]');
    if (deviceType === 'mobile') {
      obj = widget.querySelector('._widget_data');
    }
    if (!obj) return;
    const wgExceptionType = obj.getAttribute('data-widget-type');
    if (wgExceptionType === "booking") {
      const widgetAnimationDone = obj.getAttribute('data-animation-done');
      if (widgetAnimationDone === 'Y') return;
    }
    const wgAniClass = obj.getAttribute('data-widget-anim');
    const wgAniDuration = obj.getAttribute('data-widget-anim-duration');
    const wgAniDelay = obj.getAttribute('data-widget-anim-delay');
    if (wgExceptionType === 'icon' || wgExceptionType === 'button') {
      obj = deviceType === 'mobile' ? widget.querySelectorAll('.wg_animated') : widget.querySelectorAll('div[data-widget-parent-is-mobile="N"] .wg_animated');
    }
    if (!obj) return;
    const wgData = {
      wgExceptionType,
      wgAniClass,
      wgAniDuration,
      wgAniDelay,
      aniClass,
      dsAnimation
    }
    const attachAnimationEndListener = (element) => {
      if (element.getAttribute('data-animation-done') === 'Y') return;
      if (element.classList.contains('wg_animated')) {
        element.addEventListener('animationend', () => {
          element.classList.remove(wgAniClass);
          element.classList.remove(aniClass);
          element.style.opacity = '1';
          element.setAttribute('data-animation-done', 'Y');
        }, {
          once: true
        });
      }
    };
    if (wgExceptionType === 'icon' || wgExceptionType === 'button') {
      obj.forEach(item => {
        animationFunction(item, wgData, bottomOfWindow, bottomOfObject, deviceType, load);
      });
    } else {
      animationFunction(obj, wgData, bottomOfWindow, bottomOfObject, deviceType, load);
      if (wgExceptionType === 'booking') {
        attachAnimationEndListener(obj);
      }
    }
  };
  const animationFunction = (wgObj, wgData, bottomOfWindow, bottomOfObject, deviceType, load) => {
    if (!wgObj || !wgData) return;
    const {
      wgExceptionType,
      wgAniClass,
      wgAniDuration,
      wgAniDelay,
      aniClass,
      dsAnimation
    } = wgData;
    if (wgObj.classList.contains('wg_animated')) {
      wgObj.classList.remove(aniClass);
      if (bottomOfWindow > bottomOfObject) {
        wgObj.classList.add(wgAniClass);
        wgObj.style.animationDuration = `${wgAniDuration}s`;
        wgObj.style.webkitAnimationDuration = `${wgAniDuration}s`;
        wgObj.style.animationDelay = `${wgAniDelay}s`;
        if (!wgAniClass.includes('fadeIn')) {
          wgObj.style.opacity = '1';
        }
        wgObj.style.visibility = 'visible';
      } else {
        if (deviceType !== 'mobile' && load !== 'Y') {
          wgObj.classList.remove(wgAniClass);
        }
        if (!wgAniClass.includes('fadeIn')) {
          wgObj.style.opacity = '0';
        }
        wgObj.style.visibility = 'hidden';
      }
    } else {
      if (dsAnimation !== 'Y' || body.classList.contains('shop_mypage')) return;
      if (bottomOfWindow > bottomOfObject) {
        wgObj.classList.add(aniClass);
        if (wgExceptionType === 'code') {
          wgObj.classList.remove(aniClass);
        }
      } else {
        if (deviceType !== 'mobile' && load !== 'Y') {
          wgObj.classList.remove(aniClass);
          wgObj.style.opacity = '0';
          if (wgExceptionType === 'code') {
            wgObj.style.opacity = '1';
          }
        }
      }
      wgObj.style.visibility = 'visible';
    }
  }
  return {
    init: (dsAnimation, load) => {
      init(dsAnimation, load);
    }
  };
})();