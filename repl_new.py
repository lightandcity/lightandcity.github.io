import os
import shutil

# ===== 설정부 =====
ROOT_DIR = r"C:\Users\Kwon\Desktop\real_github\lightandcity.github.io"
TARGET_EXTENSIONS = (".html", ".js", ".css")

OLD_BLOCK = """
         회사소개
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
       <ul>
        <li class="depth-02" data-code="m20221213a16ffb6038a7b" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="34" href="34.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           소장 인사
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m20221213bc11137d86560" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="35" href="18.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           소개 자료
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
       </ul>
      </li>
      <li class="depth-01" data-code="m202212081efd34ea40b2c" style="">
       <a class="" data-has_child="Y" data-is_folder_menu="Y" data-url="18" href="javascript:void(0)" onclick="">
        <span class="plain_name" data-hover="">
         사업분야
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
       <ul>
        <li class="depth-02" data-code="m20221209690efd15e7457" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="23" href="51.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           일조·채광·조망 분석
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m2022120939401292beeda" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="24" href="52.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           인허가·심의 대응 환경검토
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m202212092369e6a80aa00" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="25" href="53.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           법원감정·분쟁 기술자문
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
       </ul>
      </li>
      <li class="depth-01" data-code="m20221208233f5e8286bd6" style="">
       <a class="" data-has_child="Y" data-is_folder_menu="Y" data-url="19" href="javascript:void(0)" onclick="">
        <span class="plain_name" data-hover="">
         업무상세
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
       <ul>
        <li class="depth-02" data-code="m20230323185825dbb4178" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="40" href="40.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           업무절차
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m20230323d6f698cbf5bb0" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="41" href="41.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           업무실적
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>        
        <li class="depth-02" data-code="m20230323d6f698cbf5bb0" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="61" href="61.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           의뢰사례
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
       </ul>
      </li>
      <li class="depth-01" data-code="m202303160c80d2783d540" style="">
       <a class="" data-has_child="N" data-is_folder_menu="N" data-url="38" href="38.html" onclick="">
        <span class="plain_name" data-hover="">
         상담문의
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
      </li>
     </div>
    </ul>
    <div class="im-mobile-slide-footer">
    </div>
   </div>
   <button class="navbar-toggle close slide-close" onclick="MOBILE_SLIDE_MENU.slideNavToggle();" type="button">
    <i aria-hidden="true" class="btm bt-times">
    </i>
    <span class="sr-only">
     닫기
    </span>
   </button>
   <style>
    .new_header_site .mobile_slide_menu_container.slide_open .mobile_slide_menu,
		.new_header_site .mobile_slide_menu_container .mobile_slide_menu,
		.admin.new_header_mode .mobile_slide_menu_container.slide_open .mobile_slide_menu,
		.admin.new_header_mode .mobile_slide_menu_container .mobile_slide_menu {
			background: #fff !important;
		}
		.new_header_site .mobile_slide_menu_container .mobile_slide_menu .viewport-nav.mobile li li ul,
		.admin.new_header_mode .mobile_slide_menu_container .mobile_slide_menu .viewport-nav.mobile li li ul {
			background: transparent;
		}
		.mobile_slide_menu_container .mobile_slide_menu .profile-area {
			background: #2b2b2b;
			margin-bottom:0 ;
		}
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info,
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .btn-group,
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info.guest button {
			color: #fff;
		}
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info.guest button {
				border-color:rgb(255,255,255) ;border-color:rgba(255,255,255,0.2) ;		}
		.mobile_slide_menu_container .viewport-nav.mobile li li a.has_child.open > span,
		.mobile_slide_menu_container .viewport-nav.mobile li li a.has_child.open:after,
		.mobile_slide_menu_container .viewport-nav.mobile li li a span {
			color: #430000;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li a {
			color: #430000;
			letter-spacing: 0px;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.use_sub_name:hover>a:not(.active)>.plain_name:before {
			color: #430000;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li.use_sub_name:hover>a:not(.active)>.plain_name {
			color: transparent;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li.use_sub_name:hover>a:not(.active)>.plain_name:before {
			position: absolute;
			color: #430000;
			left: auto;
			right: auto;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li a.active-real {
			background: #f5f5f5;
			color: #ffffff;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li a.active-real span,
		.mobile_slide_menu_container .viewport-nav.mobile li a.has_child.open.active-real span {
			color: #430000;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01 {
			border-top: 1px solid #f3f3f3;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01:last-child {
			border-bottom: 1px solid #f3f3f3;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01 ul{
			display : none; 		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01 > a {
			font-size: 14px;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li a {
			font-size: 13px !important;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li:last-child a,
		.mobile_slide_menu_container .viewport-nav.mobile li li li:last-child a,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapse,
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapse,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapsing[aria-expanded=false],
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapsing[aria-expanded=false] {
			margin-bottom : 0;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li > ul,
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapse.in,
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapse.in,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapsing[aria-expanded=true],
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapsing[aria-expanded=true] {
			margin-bottom: 14px;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li li:first-child a {
			margin-top: 0;
		}
				.viewport-nav.mobile li a.has_child > .toggle-btn:after {
							font-size: 13.3px;
					}
		.viewport-nav.mobile li li a.has_child > .toggle-btn:after {
							font-size: 12.35px;
					}
		.navbar-nav .profile-more.open .dropdown-menu li > a {
			background: transparent;
			color: #212121;
			padding: 8px 16px;
		}
				.mobile_slide_menu_container .mobile_slide_menu .profile-area {
			display: none;
		}
						.im-globe {
			display: none;
		}
				.im-globe .globe_icon {
			display: inline-block;
		}
		.im-globe .globe_square,
		.im-globe .globe_circle {
			display: none !important;
		}
				.im-mobile-slide-footer {
			background: #fff;
			color: #430000;
		}
		.im-mobile-slide-footer .btn {
			color: #430000;
		}
   </style>
  </div>
  <header id="doz_header_wrap">
   <div data-newheader="Y" id="doz_header">
    <div class="new_fixed_header _new_fixed_header">
     <div class="" id="inline_header_fixed" style="min-height: 30px;">
      <div class="inline-section-wrap fixed_transform" data-type="section-wrap" id="s20221209a57149455238d">
       <div class="section_bg _section_bg fixed_transform _interactive_bg">
       </div>
       <div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#430000;  position: absolute;left: 0;top: 0;right: 0; bottom: 0;">
       </div>
       <div class="inline-inside _inline-inside" data-type="inside">
        <div class="inline-section" data-type="section" section-code="s20221209a57149455238d">
         <div class="inline-col-group inline-col-group-left" data-col-group="left" data-type="col-group" style="width:225px;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w2022120910446350271af">
            <div class="_widget_data" data-widget-type="inline_logo">
             <div class="widget inline_widget logo text_inline" id="logo_w2022120910446350271af">
              <div class="img_box _img_box" style="position: relative;">
               <a class="_fade_link" href="21.html">
                <span class="sr-only">
                 주식회사 빛과도시
                </span>
                <img alt="주식회사 빛과도시" class="normal_logo _front_img" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
                <img alt="주식회사 빛과도시" class="scroll_logo fixed_transform" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
               </a>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
         <div class="inline-col-group inline-col-group-right" data-col-group="right" data-type="col-group" style="width: 1025px; visibility: visible;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w20221209f6e56a9081615">
            <div class="_widget_data" data-widget-type="inline_menu">
             <ul class="nav navbar-nav _inline_menu_container" style="visibility: visible;">
              <div class="viewport-nav desktop _main_menu">
               <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                 <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                  회사소개
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                  <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소장 인사
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                  <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소개 자료
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                 <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                  사업분야
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                  <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    일조·채광·조망 분석
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                  <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    인허가·심의 대응 환경검토
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                  <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    법원감정·분쟁 기술자문
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                 <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                  업무상세
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                  <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무절차
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무실적
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                 <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                  상담문의
                 </span>
                </a>
               </li>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px; display: none;">
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop main_clone_menu">
                <li class="dropdown _more_menu">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" data-toggle="dropdown">
                  <i aria-hidden="true" class="icon-options vertical-middle">
                  </i>
                 </a>
                 <ul class="dropdown-menu more_list _more_list">
                 </ul>
                </li>
               </div>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop _main_clone_menu main_clone_menu">
                <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                  <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                   회사소개
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                   <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소장 인사
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                   <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소개 자료
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                  <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                   사업분야
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                   <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     일조·채광·조망 분석
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                   <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     인허가·심의 대응 환경검토
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                   <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     법원감정·분쟁 기술자문
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                  <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                   업무상세
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                   <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무절차
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                   <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무실적
                    </span>
                   </a>
                  </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                  <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                   상담문의
                  </span>
                 </a>
                </li>
               </div>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop main_clone_menu">
                <li class="dropdown _more_menu">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" data-toggle="dropdown">
                  <i aria-hidden="true" class="icon-options vertical-middle">
                  </i>
                 </a>
                 <ul class="dropdown-menu more_list _more_list">
                 </ul>
                </li>
               </div>
              </div>
             </ul>
            </div>
           </div>
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div class="new_org_header _new_org_header">
     <div class="" id="inline_header_normal" style="min-height: 30px;">
      <div class="inline-section-wrap fixed_transform" data-type="section-wrap" id="s202212090e52d0cf2598b">
       <div class="section_bg _section_bg fixed_transform _interactive_bg">
       </div>
       <div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#430000; -ms-filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#00ffffff,endColorstr=#00ffffff);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#00ffffff,endColorstr=#00ffffff);	zoom: 1; position: absolute;left: 0;top: 0;right: 0; bottom: 0;">
       </div>
       <div class="inline-inside _inline-inside" data-type="inside">
        <div class="inline-section" data-type="section" section-code="s202212090e52d0cf2598b">
         <div class="inline-col-group inline-col-group-left" data-col-group="left" data-type="col-group" style="width:225px;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w2022120966554224b9df2">
            <div class="_widget_data" data-widget-type="inline_logo">
             <div class="widget inline_widget logo text_inline" id="logo_w2022120966554224b9df2">
              <div class="img_box _img_box" style="position: relative;">
               <a class="_fade_link" href="21.html">
                <span class="sr-only">
                 주식회사 빛과도시
                </span>
                <img alt="주식회사 빛과도시" class="normal_logo _front_img" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
                <img alt="주식회사 빛과도시" class="scroll_logo fixed_transform" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
               </a>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
         <div class="inline-col-group inline-col-group-right" data-col-group="right" data-type="col-group" style="width: 1025px; visibility: visible;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w20221209f0e5de754997c">
            <div class="_widget_data" data-widget-type="inline_menu">
             <ul class="nav navbar-nav _inline_menu_container" style="visibility: visible;">
              <div class="viewport-nav desktop _main_menu">
               <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                 <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                  회사소개
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                  <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소장 인사
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                  <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소개 자료
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                 <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                  사업분야
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                  <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    일조·채광·조망 분석
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                  <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    인허가·심의 대응 환경검토
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                  <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    법원감정·분쟁 기술자문
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                 <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                  업무상세
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                  <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무절차
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무실적
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                 <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                  상담문의
                 </span>
                </a>
               </li>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px; display: none;">
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop main_clone_menu">
                <li class="dropdown _more_menu">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" data-toggle="dropdown">
                  <i aria-hidden="true" class="icon-options vertical-middle">
                  </i>
                 </a>
                 <ul class="dropdown-menu more_list _more_list">
                 </ul>
                </li>
               </div>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop _main_clone_menu main_clone_menu">
                <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                  <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                   회사소개
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                   <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소장 인사
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                   <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소개 자료
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                  <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                   사업분야
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                   <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     일조·채광·조망 분석
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                   <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     인허가·심의 대응 환경검토
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                   <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     법원감정·분쟁 기술자문
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                  <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                   업무상세
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                   <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무절차
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                   <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무실적
                    </span>
                   </a>
                  </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                 </ul>
                </li>
                <li class="dropdown _show_m20221208931c197d1ca23" data-code="m20221208931c197d1ca23" id="dropdown_m20221208931c197d1ca23" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="20" href="-.html">
                  <span class="_txt_m20221208931c197d1ca23 plain_name" data-hover="">
                   연구개발
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m202212131bef3b675a3e7" data-code="m202212131bef3b675a3e7" style="">
                   <a class="_txt_m202212131bef3b675a3e7 _fade_link" data-url="29" href="-.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     건축주택연구
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212135511c166dba27" data-code="m202212135511c166dba27" style="">
                   <a class="_txt_m202212135511c166dba27 _fade_link" data-url="30" href="-.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     스마트건설
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212135d3b9c03651b7" data-code="m202212135d3b9c03651b7" style="">
                   <a class="_txt_m202212135d3b9c03651b7" data-url="31" href="javascript:void(0);" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     층간소음
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022121376e679bec36a9" data-code="m2022121376e679bec36a9" style="">
                   <a class="_txt_m2022121376e679bec36a9" data-url="32" href="javascript:void(0);" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     건설안전
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022121326b5fdea252a4" data-code="m2022121326b5fdea252a4" style="">
                   <a class="_txt_m2022121326b5fdea252a4" data-url="33" href="javascript:void(0);" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     분쟁조정연구
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                  <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                   상담문의
                  </span>
                 </a>
                </li>
                <li class="dropdown _show_m20230316e19923af12450" data-code="m20230316e19923af12450" id="dropdown_m20230316e19923af12450" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="39" href="-.html">
                  <span class="_txt_m20230316e19923af12450 plain_name" data-hover="">
                   인재채용
                  </span>
"""
NEW_BLOCK = """
         회사소개
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
       <ul>
        <li class="depth-02" data-code="m20221213a16ffb6038a7b" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="34" href="34.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           소장 인사
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m20221213bc11137d86560" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="35" href="18.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           소개 자료
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
       </ul>
      </li>
      <li class="depth-01" data-code="m202212081efd34ea40b2c" style="">
       <a class="" data-has_child="Y" data-is_folder_menu="Y" data-url="18" href="javascript:void(0)" onclick="">
        <span class="plain_name" data-hover="">
         사업분야
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
       <ul>
        <li class="depth-02" data-code="m20221209690efd15e7457" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="23" href="51.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           일조·채광·조망권 침해검토
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m2022120939401292beeda" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="24" href="52.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           태양광 발전 사업검토
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m202212092369e6a80aa00" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="25" href="53.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           조경식재·미기후 환경검토
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
       </ul>
      </li>
      <li class="depth-01" data-code="m20221208233f5e8286bd6" style="">
       <a class="" data-has_child="Y" data-is_folder_menu="Y" data-url="19" href="javascript:void(0)" onclick="">
        <span class="plain_name" data-hover="">
         업무상세
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
       <ul>
        <li class="depth-02" data-code="m20230323185825dbb4178" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="40" href="40.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           업무절차
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
        <li class="depth-02" data-code="m20230323d6f698cbf5bb0" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="41" href="41.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           업무실적
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>        
        <li class="depth-02" data-code="m20230323d6f698cbf5bb0" style="">
         <a class="" data-has_child="N" data-is_folder_menu="N" data-url="61" href="61.html" onclick="" tabindex="-1">
          <span class="plain_name" data-hover="">
           의뢰사례
          </span>
          <span class="_toggle_btn toggle-btn">
          </span>
         </a>
        </li>
       </ul>
      </li>
      <li class="depth-01" data-code="m202303160c80d2783d540" style="">
       <a class="" data-has_child="N" data-is_folder_menu="N" data-url="38" href="38.html" onclick="">
        <span class="plain_name" data-hover="">
         상담문의
        </span>
        <span class="_toggle_btn toggle-btn">
        </span>
       </a>
      </li>
     </div>
    </ul>
    <div class="im-mobile-slide-footer">
    </div>
   </div>
   <button class="navbar-toggle close slide-close" onclick="MOBILE_SLIDE_MENU.slideNavToggle();" type="button">
    <i aria-hidden="true" class="btm bt-times">
    </i>
    <span class="sr-only">
     닫기
    </span>
   </button>
   <style>
    .new_header_site .mobile_slide_menu_container.slide_open .mobile_slide_menu,
		.new_header_site .mobile_slide_menu_container .mobile_slide_menu,
		.admin.new_header_mode .mobile_slide_menu_container.slide_open .mobile_slide_menu,
		.admin.new_header_mode .mobile_slide_menu_container .mobile_slide_menu {
			background: #fff !important;
		}
		.new_header_site .mobile_slide_menu_container .mobile_slide_menu .viewport-nav.mobile li li ul,
		.admin.new_header_mode .mobile_slide_menu_container .mobile_slide_menu .viewport-nav.mobile li li ul {
			background: transparent;
		}
		.mobile_slide_menu_container .mobile_slide_menu .profile-area {
			background: #2b2b2b;
			margin-bottom:0 ;
		}
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info,
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .btn-group,
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info.guest button {
			color: #fff;
		}
		.mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info.guest button {
				border-color:rgb(255,255,255) ;border-color:rgba(255,255,255,0.2) ;		}
		.mobile_slide_menu_container .viewport-nav.mobile li li a.has_child.open > span,
		.mobile_slide_menu_container .viewport-nav.mobile li li a.has_child.open:after,
		.mobile_slide_menu_container .viewport-nav.mobile li li a span {
			color: #430000;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li a {
			color: #430000;
			letter-spacing: 0px;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.use_sub_name:hover>a:not(.active)>.plain_name:before {
			color: #430000;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li.use_sub_name:hover>a:not(.active)>.plain_name {
			color: transparent;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li.use_sub_name:hover>a:not(.active)>.plain_name:before {
			position: absolute;
			color: #430000;
			left: auto;
			right: auto;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li a.active-real {
			background: #f5f5f5;
			color: #ffffff;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li a.active-real span,
		.mobile_slide_menu_container .viewport-nav.mobile li a.has_child.open.active-real span {
			color: #430000;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01 {
			border-top: 1px solid #f3f3f3;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01:last-child {
			border-bottom: 1px solid #f3f3f3;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01 ul{
			display : none; 		}
		.mobile_slide_menu_container .viewport-nav.mobile li.depth-01 > a {
			font-size: 14px;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li a {
			font-size: 13px !important;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li:last-child a,
		.mobile_slide_menu_container .viewport-nav.mobile li li li:last-child a,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapse,
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapse,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapsing[aria-expanded=false],
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapsing[aria-expanded=false] {
			margin-bottom : 0;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li > ul,
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapse.in,
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapse.in,
		.mobile_slide_menu_container .viewport-nav.mobile li > ul.collapsing[aria-expanded=true],
		.mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapsing[aria-expanded=true] {
			margin-bottom: 14px;
		}
		.mobile_slide_menu_container .viewport-nav.mobile li li li:first-child a {
			margin-top: 0;
		}
				.viewport-nav.mobile li a.has_child > .toggle-btn:after {
							font-size: 13.3px;
					}
		.viewport-nav.mobile li li a.has_child > .toggle-btn:after {
							font-size: 12.35px;
					}
		.navbar-nav .profile-more.open .dropdown-menu li > a {
			background: transparent;
			color: #212121;
			padding: 8px 16px;
		}
				.mobile_slide_menu_container .mobile_slide_menu .profile-area {
			display: none;
		}
						.im-globe {
			display: none;
		}
				.im-globe .globe_icon {
			display: inline-block;
		}
		.im-globe .globe_square,
		.im-globe .globe_circle {
			display: none !important;
		}
				.im-mobile-slide-footer {
			background: #fff;
			color: #430000;
		}
		.im-mobile-slide-footer .btn {
			color: #430000;
		}
   </style>
  </div>
  <header id="doz_header_wrap">
   <div data-newheader="Y" id="doz_header">
    <div class="new_fixed_header _new_fixed_header">
     <div class="" id="inline_header_fixed" style="min-height: 30px;">
      <div class="inline-section-wrap fixed_transform" data-type="section-wrap" id="s20221209a57149455238d">
       <div class="section_bg _section_bg fixed_transform _interactive_bg">
       </div>
       <div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#430000;  position: absolute;left: 0;top: 0;right: 0; bottom: 0;">
       </div>
       <div class="inline-inside _inline-inside" data-type="inside">
        <div class="inline-section" data-type="section" section-code="s20221209a57149455238d">
         <div class="inline-col-group inline-col-group-left" data-col-group="left" data-type="col-group" style="width:225px;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w2022120910446350271af">
            <div class="_widget_data" data-widget-type="inline_logo">
             <div class="widget inline_widget logo text_inline" id="logo_w2022120910446350271af">
              <div class="img_box _img_box" style="position: relative;">
               <a class="_fade_link" href="21.html">
                <span class="sr-only">
                 주식회사 빛과도시
                </span>
                <img alt="주식회사 빛과도시" class="normal_logo _front_img" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
                <img alt="주식회사 빛과도시" class="scroll_logo fixed_transform" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
               </a>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
         <div class="inline-col-group inline-col-group-right" data-col-group="right" data-type="col-group" style="width: 1025px; visibility: visible;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w20221209f6e56a9081615">
            <div class="_widget_data" data-widget-type="inline_menu">
             <ul class="nav navbar-nav _inline_menu_container" style="visibility: visible;">
              <div class="viewport-nav desktop _main_menu">
               <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                 <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                  회사소개
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                  <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소장 인사
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                  <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소개 자료
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                 <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                  사업분야
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                  <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    일조·채광·조망권 침해검토
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                  <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    태양광 발전 사업검토
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                  <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    조경식재·미기후 환경검토
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                 <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                  업무상세
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                  <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무절차
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무실적
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                 <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                  상담문의
                 </span>
                </a>
               </li>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px; display: none;">
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop main_clone_menu">
                <li class="dropdown _more_menu">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" data-toggle="dropdown">
                  <i aria-hidden="true" class="icon-options vertical-middle">
                  </i>
                 </a>
                 <ul class="dropdown-menu more_list _more_list">
                 </ul>
                </li>
               </div>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop _main_clone_menu main_clone_menu">
                <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                  <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                   회사소개
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                   <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소장 인사
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                   <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소개 자료
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                  <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                   사업분야
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                   <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     일조·채광·조망권 침해검토
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                   <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     태양광 발전 사업검토
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                   <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     조경식재·미기후 환경검토
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                  <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                   업무상세
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                   <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무절차
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                   <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무실적
                    </span>
                   </a>
                  </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                  <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                   상담문의
                  </span>
                 </a>
                </li>
               </div>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop main_clone_menu">
                <li class="dropdown _more_menu">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" data-toggle="dropdown">
                  <i aria-hidden="true" class="icon-options vertical-middle">
                  </i>
                 </a>
                 <ul class="dropdown-menu more_list _more_list">
                 </ul>
                </li>
               </div>
              </div>
             </ul>
            </div>
           </div>
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div class="new_org_header _new_org_header">
     <div class="" id="inline_header_normal" style="min-height: 30px;">
      <div class="inline-section-wrap fixed_transform" data-type="section-wrap" id="s202212090e52d0cf2598b">
       <div class="section_bg _section_bg fixed_transform _interactive_bg">
       </div>
       <div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#430000; -ms-filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#00ffffff,endColorstr=#00ffffff);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#00ffffff,endColorstr=#00ffffff);	zoom: 1; position: absolute;left: 0;top: 0;right: 0; bottom: 0;">
       </div>
       <div class="inline-inside _inline-inside" data-type="inside">
        <div class="inline-section" data-type="section" section-code="s202212090e52d0cf2598b">
         <div class="inline-col-group inline-col-group-left" data-col-group="left" data-type="col-group" style="width:225px;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w2022120966554224b9df2">
            <div class="_widget_data" data-widget-type="inline_logo">
             <div class="widget inline_widget logo text_inline" id="logo_w2022120966554224b9df2">
              <div class="img_box _img_box" style="position: relative;">
               <a class="_fade_link" href="21.html">
                <span class="sr-only">
                 주식회사 빛과도시
                </span>
                <img alt="주식회사 빛과도시" class="normal_logo _front_img" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
                <img alt="주식회사 빛과도시" class="scroll_logo fixed_transform" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
               </a>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
         <div class="inline-col-group inline-col-group-right" data-col-group="right" data-type="col-group" style="width: 1025px; visibility: visible;">
          <div class="inline-col" data-type="grid">
           <div class="inline-widget" data-type="widget" id="w20221209f0e5de754997c">
            <div class="_widget_data" data-widget-type="inline_menu">
             <ul class="nav navbar-nav _inline_menu_container" style="visibility: visible;">
              <div class="viewport-nav desktop _main_menu">
               <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                 <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                  회사소개
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                  <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소장 인사
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                  <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    소개 자료
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                 <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                  사업분야
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                  <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    일조·채광·조망권 침해검토
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                  <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    태양광 발전 사업검토
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                  <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    조경식재·미기후 환경검토
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                 <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                  업무상세
                 </span>
                </a>
                <ul class="dropdown-menu" role="menu">
                 <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                  <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무절차
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    업무실적
                   </span>
                  </a>
                 </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                </ul>
               </li>
               <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                 <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                  상담문의
                 </span>
                </a>
               </li>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px; display: none;">
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop main_clone_menu">
                <li class="dropdown _more_menu">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" data-toggle="dropdown">
                  <i aria-hidden="true" class="icon-options vertical-middle">
                  </i>
                 </a>
                 <ul class="dropdown-menu more_list _more_list">
                 </ul>
                </li>
               </div>
              </div>
              <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;">
               <div class="viewport-nav desktop _main_clone_menu main_clone_menu">
                <li class="dropdown _show_m20221201f9696fab3c649" data-code="m20221201f9696fab3c649" id="dropdown_m20221201f9696fab3c649" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="17" href="javascript:void(0)">
                  <span class="_txt_m20221201f9696fab3c649 plain_name" data-hover="">
                   회사소개
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221213a16ffb6038a7b" data-code="m20221213a16ffb6038a7b" style="">
                   <a class="_txt_m20221213a16ffb6038a7b _fade_link" data-url="34" href="34.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소장 인사
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212133e4cc5cf9cc2b" data-code="m202212133e4cc5cf9cc2b" style="">
                   <a class="_txt_m202212133e4cc5cf9cc2b _fade_link" data-url="37" href="18.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     소개 자료
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202212081efd34ea40b2c" data-code="m202212081efd34ea40b2c" id="dropdown_m202212081efd34ea40b2c" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="18" href="javascript:void(0)">
                  <span class="_txt_m202212081efd34ea40b2c plain_name" data-hover="">
                   사업분야
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20221209690efd15e7457" data-code="m20221209690efd15e7457" style="">
                   <a class="_txt_m20221209690efd15e7457 _fade_link" data-url="23" href="51.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     일조·채광·조망권 침해검토
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022120939401292beeda" data-code="m2022120939401292beeda" style="">
                   <a class="_txt_m2022120939401292beeda _fade_link" data-url="24" href="52.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     태양광 발전 사업검토
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212092369e6a80aa00" data-code="m202212092369e6a80aa00" style="">
                   <a class="_txt_m202212092369e6a80aa00 _fade_link" data-url="25" href="53.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     조경식재·미기후 환경검토
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m20221208233f5e8286bd6" data-code="m20221208233f5e8286bd6" id="dropdown_m20221208233f5e8286bd6" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="19" href="javascript:void(0)">
                  <span class="_txt_m20221208233f5e8286bd6 plain_name" data-hover="">
                   업무상세
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m20230323185825dbb4178" data-code="m20230323185825dbb4178" style="">
                   <a class="_txt_m20230323185825dbb4178 _fade_link" data-url="40" href="40.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무절차
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                   <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="41" href="41.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     업무실적
                    </span>
                   </a>
                  </li>
                 <li class="dropdown-submenu _show_m20230323d6f698cbf5bb0" data-code="m20230323d6f698cbf5bb0" style="">
                  <a class="_txt_m20230323d6f698cbf5bb0 _fade_link" data-url="61" href="61.html" tabindex="-1">
                   <span class="plain_name" data-hover="">
                    의뢰사례
                   </span>
                  </a>
                 </li>
                 </ul>
                </li>
                <li class="dropdown _show_m20221208931c197d1ca23" data-code="m20221208931c197d1ca23" id="dropdown_m20221208931c197d1ca23" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="20" href="-.html">
                  <span class="_txt_m20221208931c197d1ca23 plain_name" data-hover="">
                   연구개발
                  </span>
                 </a>
                 <ul class="dropdown-menu" role="menu">
                  <li class="dropdown-submenu _show_m202212131bef3b675a3e7" data-code="m202212131bef3b675a3e7" style="">
                   <a class="_txt_m202212131bef3b675a3e7 _fade_link" data-url="29" href="-.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     건축주택연구
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212135511c166dba27" data-code="m202212135511c166dba27" style="">
                   <a class="_txt_m202212135511c166dba27 _fade_link" data-url="30" href="-.html" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     스마트건설
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m202212135d3b9c03651b7" data-code="m202212135d3b9c03651b7" style="">
                   <a class="_txt_m202212135d3b9c03651b7" data-url="31" href="javascript:void(0);" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     층간소음
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022121376e679bec36a9" data-code="m2022121376e679bec36a9" style="">
                   <a class="_txt_m2022121376e679bec36a9" data-url="32" href="javascript:void(0);" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     건설안전
                    </span>
                   </a>
                  </li>
                  <li class="dropdown-submenu _show_m2022121326b5fdea252a4" data-code="m2022121326b5fdea252a4" style="">
                   <a class="_txt_m2022121326b5fdea252a4" data-url="33" href="javascript:void(0);" tabindex="-1">
                    <span class="plain_name" data-hover="">
                     분쟁조정연구
                    </span>
                   </a>
                  </li>
                 </ul>
                </li>
                <li class="dropdown _show_m202303160c80d2783d540" data-code="m202303160c80d2783d540" id="dropdown_m202303160c80d2783d540" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="38" href="38.html">
                  <span class="_txt_m202303160c80d2783d540 plain_name" data-hover="">
                   상담문의
                  </span>
                 </a>
                </li>
                <li class="dropdown _show_m20230316e19923af12450" data-code="m20230316e19923af12450" id="dropdown_m20230316e19923af12450" style="">
                 <a aria-expanded="false" class="fixed_transform dropdown-toggle disabled _header_dropdown _fade_link" data-toggle="dropdown" data-url="39" href="-.html">
                  <span class="_txt_m20230316e19923af12450 plain_name" data-hover="">
                   인재채용
                  </span>
"""

BACKUP = True
# =================


def replace_block_in_file(file_path, old_block, new_block, backup=True):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if old_block not in content:
        return

    if backup:
        shutil.copy(file_path, file_path + ".bak")

    content = content.replace(old_block, new_block)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[REPLACED] {file_path}")


def replace_block_in_folder(root_dir, old_block, new_block, backup=True):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(TARGET_EXTENSIONS):
                file_path = os.path.join(root, file)
                replace_block_in_file(
                    file_path,
                    old_block,
                    new_block,
                    backup
                )


if __name__ == "__main__":
    replace_block_in_folder(
        ROOT_DIR,
        OLD_BLOCK,
        NEW_BLOCK,
        BACKUP
    )
    print("✅ 블록 치환 완료")
