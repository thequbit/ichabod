
var PageCustomer = {

    name: 'customer',
    id: 'page-customer',
    load : function(show, url) {

        //var url = 'customers/:' + value;
        
        console.log("Loading customer data ...");
        
        $.getJSON(url, function(customer) {
            PageCustomer.customer = customer;
            PageCustomer._showCustomerInfo();
            show('customer');
        });
    },
    unload : function () {
    },
    navigate : function(value) {
        if ( value != undefined && value != '' ) {
            var id = value.split('/')[0];
            PageCustomer._showCustomerInfo(this.customer);
        }
    },
    _showCustomerInfo : function() {
        
        if ( this.customer == undefined || this.customer == {} ) {
            PageCustomer._hideCustomerInfo();
            
            return;
        }
        
        var html = '';
        html += '<h5>Customer Name<input type="text" value="' + this.customer.name + '"></input></h5>';
        html += '<h5>Customer Description<textarea rows="6">' + this.customer.notes + '</textarea></h5>';
        
        html += '</br>';
        html += '<h4>Customer Accounts<a class="right button" href="#/accounts/new" class="button">New Account</a></h4>';
        
        var headers = [
            'Account',
            'Contact',
            'Leads',
            'Opertunities'
            //'Projects'
        ];
        var accountTableData = this.customer.accounts;
        for(var i=0; i<accountTableData.length; i++) {
            var id = accountTableData[i].primary_contact_id;
            var name = accountTableData[i].primary_contact_name;
            delete accountTableData[i].primary_contact_id;
            delete accountTableData[i].primary_contact_email;
            delete accountTableData[i].primary_contact_phone;
            accountTableData[i].primary_contact_name = '<a href="#/contact/:' + id + '">' + name + '</a>';
        }
        console.log(accountTableData);
        html += TableMaker.makeTable('page-customer-customer-accounts', 'accounts', headers, accountTableData);
        
        $('#page-customer-customer-info').html(html);
        $('#page-customer-customer-info').show();
        
        $('#page-customer-customer-accounts').dataTable();
    },
    _hideCustomerInfo : function() {
        $('#page-customer-customer-info').html('');
        $('#page-customer-customer-info').hide();
    }
};

// register page with Pages tool
Pages.registerPage(PageCustomer);
