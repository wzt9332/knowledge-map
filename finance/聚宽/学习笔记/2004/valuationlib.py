
<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>valuationlib.py (editing)</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="https://cdn.joinquant.com/research/static/base/images/favicon-file.ico?v=e2776a7f45692c839d6eea7d7ff6f3b2">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="https://cdn.joinquant.com/research/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=9b2c8d3489227115310662a343fce11c" type="text/css" />
    <link rel="stylesheet" href="https://cdn.joinquant.com/research/static/components/jquery-typeahead/dist/jquery.typeahead.min.css?v=7afb461de36accb1aa133a1710f5bc56" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="https://cdn.joinquant.com/research/static/components/codemirror/lib/codemirror.css?v=ae81317fa2b3a745892c83985827d41b">
<link rel="stylesheet" href="https://cdn.joinquant.com/research/static/components/codemirror/addon/dialog/dialog.css?v=c89dce10b44d2882a024e7befc2b63f5">

    <link rel="stylesheet" href="https://cdn.joinquant.com/research/static/style/style.min.css?v=47782e517c98a53adb514cbefb4528f2" type="text/css"/>
    

    <link rel="stylesheet" href="/user/60474564012/custom/custom.css" type="text/css" />
    <script src="https://cdn.joinquant.com/research/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="https://cdn.joinquant.com/research/static/components/preact/index.js?v=00a2fac73c670ce39ac53d26640eb542" type="text/javascript"></script>
    <script src="https://cdn.joinquant.com/research/static/components/proptypes/index.js?v=c40890eb04df9811fcc4d47e53a29604" type="text/javascript"></script>
    <script src="https://cdn.joinquant.com/research/static/components/preact-compat/index.js?v=f865e990e65ad27e3a2601d8adb48db1" type="text/javascript"></script>
    <script src="https://cdn.joinquant.com/research/static/components/requirejs/require.js?v=6da8be361b9ee26c5e721e76c6d4afce" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20200510192016",
          
          baseUrl: 'https://cdn.joinquant.com/research/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/user/60474564012/custom',
            nbextensions : '/user/60474564012/nbextensions',
            kernelspecs : '/user/60474564012/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/ui/minified/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/dist/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    </script>

    
    

</head>

<body class="edit_app "
 
data-base-url="/user/60474564012/"
data-file-path="IndexValuationReport/valuationlib.py"

  
 

dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook需要的JavaScript.<br>
      请允许它执行.
  </div>
</noscript>

<div id="header">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="/user/60474564012/tree" title='指示板'>
      
<img src='/hub/logo' alt='Jupyter Notebook'/>

  </a></div>

  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename"></span>
    <span class="last_modified"></span>
</span>


  
  

  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">注销</button>
      
    </span>

  

  

<span>
    <a href='/hub/home'
       class='btn btn-default btn-sm navbar-btn pull-right'
       style='margin-right: 4px; margin-left: 2px;'>
        Control Panel
    </a>
</span>

  
  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p  class="navbar-text indicator_area">
          <span id="current-mode" >当前模式</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">文件</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="#">新建</a></li>
                <li id="save-file"><a href="#">保存</a></li>
                <li id="rename-file"><a href="#">重命名</a></li>
                <li id="download-file"><a href="#">下载</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">编辑</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="#">查找</a></li>
                <li id="menu-replace"><a href="#">查找 &amp; 替换</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">快捷键</li>
                <li id="menu-keymap-default"><a href="#">默认<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="#">Sublime文本<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs"><a href="#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">视图</a>
              <ul id="view-menu" class="dropdown-menu">
              <li id="toggle_header" title="显示/隐藏 标题和logo">
              <a href="#">开/关 文档头</a></li>
              <li id="menu-line-numbers"><a href="#">开/关 行号</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">语言</a>
              <ul id="mode-menu" class="dropdown-menu">
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"></div>
</div>


</div>






    


<script src="https://cdn.joinquant.com/research/static/edit/js/main.min.js?v=69ef7b7a55de6f60611ff3ae94ef5069" type="text/javascript" charset="utf-8"></script>


<script type='text/javascript'>
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>
</body>

</html>