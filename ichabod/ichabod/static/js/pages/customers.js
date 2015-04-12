
var PageCustomers = {

    name: 'customers',
    id: 'page-customers',
    _currentId: undefined,
    load : function( show, url ) {
        
        //var url = 'customers/';
        
        // get the customers from the server, then process them for display
        $.getJSON(url, function(data) {
        
            PageCustomers.customers = data.customers;
        
            PageCustomers._renderCustomers();
            
            show('customers');
            
        });
    },
    unload : function() {
    },
    navigate : function(value) {
        if ( value != undefined && value != '' ) {
            var id = value.split('/')[0];
            if ( id == 'new' ) {
                $('#page-customers-new-customer-dialog').foundation('reveal','open');
                location.hash = '#/customers/';
            } else {
                
            }
        
        }
    },
    _renderCustomers: function() {
        var html = '';
            
        headers = [
            'Customer',
            'Accounts',
            'Value',
        ];
        var customerTableData = [];
        for(var i=0; i<this.customers.length; i++) {
            var totalValue = 0;
            for(var j=0; j<this.customers[i].accounts.length; j++) {
                for(var k=0; k<this.customers[i].accounts[j].jobs.length; k++) {
                    for(var l=0; l<this.customers[i].accounts[j].jobs[k].projects.length; k++) {
                        totalValue += this.customers[i].accounts[j].jobs[k].projects[l].value;
                    }
                }
            }
            totalValue = '$' + totalValue;
            customerTableData.push({
                id: this.customers[i].id,
                name: this.customers[i].name,
                accountsCount: this.customers[i].accounts.length,
                projectCount: totalValue
            })
        }
        
        html += TableMaker.makeTable('page-customers-customer-list', 'customer', headers, customerTableData);
        
        $('#page-customers-customer-list-container').html(html);

        $('#page-customers-customer-list').dataTable();
        
        // new customer dialog
        /*
        var html = '';
        html += '<h3>New Customer</h3>';
        html += '<label>Customer Name<input type="text" placeholder="Customer name" id="page-customers-new-customer-name"></input></label>';
        html += '<label>Notes<textarea rows="6" placeholder="Customer notes" id="page-customers-new-customer-notes"></textarea></label>';
        html += '<a class="right small button" onclick="PageCustomers._newCustomer();">Save</a>';
        html += '<a class="close-reveal-modal" aria-label="Close">&#215;</a>';
        */
        
        var html2 = '';
        html2 += _h(3,'New Customer');
        html2 += _label('Customer Name' + _textinput('page-customers-new-customer-name', 'Customer Name', ''));
        html2 += _label('Notes' + _textarea('page-customers-new-customer-notes', 'Customer Notes', 6, ''));
        html2 += '<a class="right small button" onclick="PageCustomers._newCustomer();">Save</a>';
        html2 += '<a class="close-reveal-modal" aria-label="Close">&#215;</a>';
        
        $('#page-customers-new-customer-dialog').html(html2);
        
        
    },
    _newCustomer: function() {
        
        $('#page-customers-new-customer-dialog').foundation('reveal','close');
        
        // TODO: push new customer to server
        
        var id = Math.floor(Math.random() * 90000) + 10000;
        
        this.customers.push({
            id: id,
            name: $('#page-customers-new-customer-name').val(),
            notes: $('#page-customers-new-customer-notes').val(),
            labels: [],
            accounts: []
        });
        
        // TODO: nav after async is done
        location.hash = '#/customer/:' + id + '/';
    }
};

// register page with Pages tool
Pages.registerPage(PageCustomers);

