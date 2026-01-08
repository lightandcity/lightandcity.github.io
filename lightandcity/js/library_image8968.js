var LIBRARY_IMAGE = function() {
  var cover_image_index = 0;
  var type = "";
  var $editor_obj, $cover_image, $represent_img, represent_img_val, $library_img_list;
  var editor_id;
  var init = function(_type, _editor_obj, _library_img_obj, _represent_img = '') {
    type = _type;
    $editor_obj = _editor_obj;
    editor_id = $editor_obj.attr("id");
    var $library_img_obj = _library_img_obj;
    var library_img_html = "";
    library_img_html += '<div class="post_write_left _post_write_left">';
    library_img_html += '<div class="margin-bottom-xxl img_tools_title"><div class="holder">' + getLocalizeString('타이틀_대표이미지설정', '', '대표 이미지 설정') + ' <a href="javascript:;" class="btn-dismiss hidden-md hidden-lg hidden-sm" id="library_img_close_btn"><i class="btl bt-times" aria-hidden="true"></i><span class="sr-only">' + getLocalizeString('설명_대표이미지삭제', '', '대표 이미지 삭제') + '</span></a></div></div>';
    if (!TEST_SERVER) {
      library_img_html += '<div class="clearfix library_img_list" id="library_img_list"><div style="text-align:center;padding-top:75px;"><span class="hidden-sm hidden-lg hidden-md opacity-50" style="font-size:16px;">' + getLocalizeString('설명_첨부된이미지가없습니다', '', '첨부된 이미지가 없습니다.') + '</span></div></div>';
    } else {
      library_img_html += '<div class="clearfix library_img_list" id="library_img_list"><div style="text-align:center;padding-top:75px;"><span class="blocked hidden-sm hidden-lg hidden-md opacity-50" style="font-size:16px;">' + getLocalizeString('설명_첨부된이미지가없습니다', '', '첨부된 이미지가 없습니다.') + '</span><p class="hidden-sm hidden-lg hidden-md margin-top-xl inline-blocked holder"><span class="text-brand">' + getLocalizeString("설명_이미지추가", '', "이미지 추가") + '</span><input type=\'file\' name=\'files[]\' class=\'img-file-control\' accept=\'image/jpeg, image/jpg, image/png, image/gif, image/svg+xml\' title="' + getLocalizeString("설명_이미지추가", '', "이미지 추가") + '"></p></div></div>';
    }
    library_img_html += '</div>';
    $library_img_obj.html(library_img_html);
    $library_img_list = $("#library_img_list");
    $represent_img = $("#represent_img");
    $cover_image = $('#cover_image');
    represent_img_val = _represent_img;
    $("#library_img_btn, #library_img_close_btn").off("click.library_img_btn").on("click.library_img_btn", function() {
      $library_img_obj.find("._post_write_left").toggleClass("on_library_img");
    });
  };
  var addLibraryImageLoop = function(delay) {
    LIBRARY_IMAGE.addLibraryImage();
    setInterval(LIBRARY_IMAGE.addLibraryImage, delay);
  };
  var tmp_img_list = [];
  var tmp_imgs = {};
  var addLibraryImage = function() {
    var $body;
    if (IE_VERSION < 10) {
      $body = $(CKEDITOR.instances[editor_id].getData());
    } else {
      $body = $editor_obj;
    }
    var img_list = [];
    var cover_image = $cover_image.val();
    if (cover_image !== "") {
      cover_image_index = 0;
      img_list.push(cover_image);
    } else cover_image_index = -1;
    $body.find("img, iframe, embed").each(function() {
      var $that = $(this);
      var src = $that.attr("src");
      if (typeof src !== 'undefined') {
        if ($that.prop("tagName") === "IMG") {
          src = src.replace(CDN_UPLOAD_URL, UPLOAD_URL);
          src = src.replace(CDN_THUMBNAIL_URL, THUMBNAIL_URL);
          if ($.inArray(src, img_list) == -1 && src.indexOf('base64') == -1) img_list.push(src);
        } else {
          var is_video_type = getVideoId(src);
          var thumb_data = {};
          if (typeof is_video_type != 'undefined') {
            $.each(is_video_type, function(k, v) {
              switch (k) {
                case 'youtube':
                  if (typeof tmp_imgs[v[1]] == 'undefined') {
                    thumb_data = getYoutubeThumbnail(v[1]);
                    tmp_imgs[v[1]] = thumb_data;
                  } else {
                    thumb_data = tmp_imgs[v[1]];
                  }
                  if (thumb_data != "" && typeof thumb_data != 'undefined') img_list.push(thumb_data);
                  break;
                case 'vimeo':
                  var check_param = src.indexOf("?");
                  if (check_param != -1) {
                    src = src.substring(0, check_param);
                  }
                  src = "https:" + src;
                  img_list.push(src);
                  thumb_data = getVimeoThumbnail(src, function(src, thumb_url) {
                    changeImageById(src, thumb_url);
                  });
                  break;
              }
            });
          }
        }
      }
    });
    updateLibrayImage(img_list);
  };

  function updateLibrayImage(img_list) {
    var html = "";
    var is_update = false;
    var img_list_length = img_list.length;
    var tmp_img_list_length = tmp_img_list.length;
    if (img_list_length !== tmp_img_list_length) is_update = true;
    $.each(img_list, function(i, v) {
      if (v !== tmp_img_list[i]) {
        is_update = true;
        return false;
      }
    });
    if (is_update) {
      var represent_img_src = represent_img_val;
      var is_represent_img = false;
      if (img_list_length > 1 || cover_image_index == -1) {
        $.each(img_list, function(index, _img_src) {
          if (represent_img_src === _img_src) {
            is_represent_img = true;
            $represent_img.val(represent_img_src);
          };
        });
        if (!is_represent_img) {
          $represent_img.val("");
          represent_img_src = "";
        }
      }
      $.each(img_list, function(index, _img_src) {
        var img_src = "";
        img_src = _img_src;
        if (img_src.indexOf("http") !== -1 || img_src.indexOf("https") !== -1) {} else {
          if (img_src.substring(0, 8) == "/upload/") {
            img_src = img_src.replace("/upload/", "");
            img_src = CDN_UPLOAD_URL + img_src;
          } else if (img_src.substring(0, 11) == "/thumbnail/") {
            img_src = img_src.replace("/thumbnail/", "");
            img_src = CDN_THUMBNAIL_URL + img_src;
          } else if (img_src.indexOf(CDN_UPLOAD_URL) === -1) {
            img_src = CDN_UPLOAD_URL + img_src;
          }
        }
        if (represent_img_src === "" && index === 0 && img_list_length !== 0) {
          represent_img_src = _img_src;
          $represent_img.val(represent_img_src);
        }
        var add_class = _img_src === represent_img_src ? "on" : "";
        var is_represent_img = add_class === "on";
        if (_img_src.indexOf(".") == -1) img_src = NO_IMAGE_URL;
        html += "<div class='123123 float_l img_tools _library_img " + add_class + "' style='background-image: url(" + img_src + ")' data-id='" + _img_src + "'>";
        html += '<a href="javascript:;" data-url="' + _img_src + '" onclick="LIBRARY_IMAGE.deleteLibraryImage(' + index + ',' + is_represent_img + ')"><i aria-hidden="true" class="btm bt-times"></i></a><div class="primary">' + getLocalizeString('설명_대표', '', '대표') + '</div>';
        html += "</div>";
        if (TEST_SERVER) {
          html += "<div class='float_l img_tools _library_img add_img'>";
          html += "<i aria-hidden='true' class='btm bt-plus'></i>";
          html += "<input type='file' name='files[]' class='img-file-control' accept='image/jpeg, image/jpg, image/png, image/gif, image/svg+xml'>";
          html += "</div>";
        }
      });
      if (!html) html = '<div style="text-align:center;padding-top:75px;"><span class="hidden-sm hidden-lg hidden-md opacity-50" style="font-size:16px;">' + getLocalizeString('설명_첨부된이미지가없습니다', '', '첨부된 이미지가 없습니다.') + '</span></div>';
      $library_img_list.html(html);
      tmp_img_list = img_list;
      $library_img_list.find("._library_img").off("click.library_img").on("click.library_img", function() {
        $library_img_list.find("._library_img").removeClass("on");
        $(this).addClass("on");
        var img_name = $(this).find("a").data("url");
        $represent_img.val(img_name);
      });
    } else {
      if (img_list_length === 0 && represent_img_src !== "") {
        $represent_img.val("");
        represent_img_src = "";
      }
    }
  }
  var deleteLibraryImage = function(delete_index, is_represent) {
    is_update = true;
    var body = '';
    if (delete_index === cover_image_index) {
      deleteCoverImage();
    } else {
      if (IE_VERSION < 10) {
        body = CKEDITOR.instances[editor_id].getData();
      } else {
        body = FroalaEditor('#' + editor_id).html.get(true);
      }
      var delete_tag = "";
      var current_index = cover_image_index === -1 ? 0 : 1;
      $(body).find("img, iframe, embed").each(function(index, tag) {
        if ($(this).prop("tagName") !== "IMG") {
          if ($(this).attr("src").indexOf("youtube") === -1 && $(this).attr("src").indexOf("vimeo") === -1) return true;
        }
        if (delete_index === current_index) {
          delete_tag = tag.outerHTML;
          delete_tag = $.trim(delete_tag);
          return false;
        }
        current_index++;
      });
      body = body.replace(delete_tag, "");
      if (IE_VERSION < 10) {
        CKEDITOR.instances[editor_id].setData(body);
      } else {
        FroalaEditor('#' + editor_id).html.set(body, true);
      }
    }
    if (is_represent) {
      $represent_img.val("");
    }
    addLibraryImage();
  };

  function changeImageById(id, thumb_url) {
    var old_url = $library_img_list.find("div[data-id='" + id + "']").css("background-image");
    if (typeof old_url != 'undefined' && old_url.indexOf(thumb_url) == -1) {
      $library_img_list.find("div[data-id='" + id + "']").css({
        "background-image": "url(" + thumb_url + ")"
      });
      $library_img_list.find("div[data-id='" + id + "']").find("a").data("url", thumb_url);
      if ($library_img_list.find("div[data-id='" + id + "']").hasClass("on")) $represent_img.val(thumb_url);
    }
  }

  function deleteCoverImage() {
    switch (type) {
      case 'post':
        POST.deleteCoverImage();
        break;
      case 'map':
        MAP.deleteCoverImage();
        break;
    }
  }
  return {
    'init': function(_type, _editor_obj, _library_img_obj, _represent_img) {
      init(_type, _editor_obj, _library_img_obj, _represent_img);
    },
    'addLibraryImageLoop': function(delay) {
      addLibraryImageLoop(delay);
    },
    'addLibraryImage': function() {
      addLibraryImage();
    },
    'deleteLibraryImage': function(delete_index, is_represent) {
      deleteLibraryImage(delete_index, is_represent);
    }
  };
}();