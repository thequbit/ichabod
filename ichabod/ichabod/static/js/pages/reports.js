
var PageReports = {

    name: 'reports',
    id: 'page-reports', 
    load : function(doneCallback) {
        
        // do async things here, and then call doneCallback() to display page.
        
        doneCallback(this.name);
    },
    unload : function () {
    },
    navigate : function() {
    }

};

// register page with Pages tool
Pages.registerPage(PageReports);