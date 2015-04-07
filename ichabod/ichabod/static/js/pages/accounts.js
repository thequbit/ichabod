
var PageAccounts = {

    name: 'accounts',
    id: 'page-accounts', 
    load : function(doneCallback) {
        
        // do async things here, and then call doneCallback() to display page.
        
        doneCallback('accounts');
    },
    unload : function () {
    },
    navigate : function() {
    }

};

// register page with Pages tool
Pages.registerPage(PageAccounts);