var Pages = {
    _pages : [],
    _params: {
        'page-title-element': 'h3',
        'site-div-id': '',
        'site-loading-div-id': '',
    },
    _currentPage : '',
    _homePage : '',
    _loadingPageId : '',
    _showPage : function(pageName) {
        console.log("Pages._showPage(), pageName = '" + pageName + "'");
        Pages._hideLoadingPage();
        document.getElementById(Pages._getPage(pageName).id).style.display = "inline";
        if ( document.getElementById('pages-nav-' + Pages._currentPage) != null ) {
            document.getElementById('pages-nav-' + Pages._currentPage).className = 
                document.getElementById('pages-nav-' + Pages._currentPage).className.replace(' pages-nav-highlight','');
        }
        Pages._currentPage = pageName;
        if ( document.getElementById('pages-nav-' + Pages._currentPage) !== null ) {
            document.getElementById('pages-nav-' + Pages._currentPage).className += ' pages-nav-highlight';
        }
    },
    _showLoadingPage : function() {
        console.log("Pages._showLoadingPage()");
        if ( document.getElementById(Pages._loadingPageId) != null ) {
            document.getElementById(Pages._loadingPageId).style.display = "inline";
        }
    },
    _hideLoadingPage : function() {
        console.log("Pages._hideLoadingPage()");
        if ( document.getElementById(Pages._loadingPageId) != null ) {
            document.getElementById(Pages._loadingPageId).style.display = "none";
        }
    },
    _hidePages : function() {
        console.log("Pages._hidePages()");
        for(var i=0; i<Pages._pages.length; i++) {
            document.getElementById(Pages._pages[i].id).style.display = "none";
        }
    },
    _navigate : function(url) {
        console.log("Pages._navigate(), url = '" + url + "'");
        var pageName = '';
        var value = undefined;
        if ( url == undefined || url == '' ) {
            pageName = Pages._homePage;
        } else {
            pageName = url.split('/')[1];
            if ( url.split('/').length > 1 ) {
                value = url.split('/').splice(2,url.split('/').length).join('/');
            }
        }
        Pages.loadPage(pageName);
        location.hash = "#" + url;
        console.log("Pages._navigate(), url: " + url);
        console.log("Pages._navigate(), pageName: " + pageName);
        if ( typeof Pages._getPage(pageName).navigate !== 'undefined' ) {
            Pages._getPage(pageName).navigate(value);
        }
    },
    _getPage : function(pageName) {
        for(var i=0; i<Pages._pages.length; i++) {
            if(Pages._pages[i].name == pageName) {
                return Pages._pages[i];
            }
        }
    },
    init : function(params) {
        for( p in params ) {
            this._params[p] = params[p];
        }
        var navPage = location.hash.slice(1);
        if ( navPage == '' ) {
            if (Pages._homePage == undefined || Pages._homePage == '' ) {
                navPage = "/" + Pages._pages[0].pageName;
            } else {
                navPage = "/" + Pages._homePage;
            }
        }
        Pages._navigate(navPage);
        if ( document.getElementById(this._params['site-div-id']) != null ) {
            document.getElementById(this._params['site-div-id']).style.display = 'inline';
        }
        if ( document.getElementById(this._params['site-loading-div-id']) != null ) {
            document.getElementById(this._params['site-loading-div-id']).style.display = 'none';
        }
        
    },
    registerHomePage : function(pageDef) {
        console.log("Pages.registerHomePage()");
        Pages._homePage = pageDef.name;
        Pages.registerPage(pageDef);
    },
    registerPage : function(pageDef) {
        console.log("Pages.registerPage(), pageName = '" + pageDef.name + "'");
        Pages._pages.push(pageDef);
    },
    registerLoadingPage : function(id) {
        console.log("Pages.registerLoadingPage()");
        Pages._loadingPageId = id;
    },
    loadPage : function(pageName) {
        console.log("Pages.loadPage(), pageName = '" + pageName + "'");
        Pages._hidePages();
        Pages._showLoadingPage();
        var page = undefined;
        if ( typeof pageName !== 'undefined' && pageName != '' ) {
            console.log("Pages.loadPage(), Valid name.  Loading '" + pageName + "'");
            page = Pages._getPage(pageName);
        } else {
            page = Pages._getPage(Pages._homePage);
            pageName = Pages._homePage;
        }
        console.log("Pages.loadPage(), page.name: " + page.name);
        var camelPageName = page.name.charAt(0).toUpperCase() + page.name.slice(1);
        
        var html = '<' + this._params['page-title-element'] + '>' + camelPageName + '</' + this._params['page-title-element'] + '>'
        if ( document.getElementById(page.id).querySelector('.page-header') != null ) {
            document.getElementById(page.id).querySelector('.page-header').innerHTML = html;
        }
        
        if ( typeof page.load !== 'undefined' ) {
            console.log("Pages.loadPage(), calling page.loadFunction()");
            page.load( Pages._showPage );
        }
    }
    
};

window.onhashchange = function() {
    console.log('hash changed, new url: ' + location.hash);
    Pages._navigate(location.hash.slice(1));
}

