
var TableMaker = {

    makeTable : function(tableId, urlPrefix, headers, data) {
        
        var html = '';
        html += '<table id="' + tableId + '"><thead><tr>';
        for(var i=0; i< headers.length; i++) {
            html += '<th>' + headers[i] + '</th>';
        }
        html += '</thead>';
        
        html += '<tdody>';
        
        for(var i=0; i<data.length; i++) {
            html += '<tr>';
            
            var index = undefined;
            var j = 0;
            for( var key in data[i] ) {
                if ( j ==  0 ) {
                    index = data[i][key];
                } else if (j == 1) {
                    html += '<td><a href="#/' + urlPrefix + '/' + index + '">' + data[i][key] + '</a></td>';
                }
                else if ( j > headers.length ) {
                    // nop
                }
                else {
                    var val = data[i][key];
                    if ( typeof val == 'string' || val instanceof String ) {
                        if ( val.charAt(0) == '$' ) {
                            val = "$" + parseInt(val.substr(1)).formatMoney(2, '.', ',');
                        }
                        else if ( val.indexOf('@') !== -1 ) {
                            val = '<a href="mailto:' + val + '">' + val + '</a>';
                        }
                    }
                    html += '<td>' + val + '</td>';
                }
                j += 1;
            }
            html += '</tr>';
        }
        
        html += '</tdody>';
        html += '</table>';

        //console.log(html);

        return html;
        
    }

};