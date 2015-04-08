
var PageAccounts = {

    name: 'accounts',
    id: 'page-accounts', 
    load : function(show, url) {
        
        $.getJSON( '/accounts/', function() {
        
            var html = ''

        })
        
        show('accounts');
    },
    unload : function () {
    },
    navigate : function(value) {
    }

};

// register page with Pages tool
Pages.registerPage(PageAccounts);
