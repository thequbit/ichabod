
Number.prototype.formatMoney = function(c, d, t){
    var n = this, 
    c = isNaN(c = Math.abs(c)) ? 2 : c, 
    d = d == undefined ? "." : d, 
    t = t == undefined ? "," : t, 
    s = n < 0 ? "-" : "", 
    i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "", 
    j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};

_h = function(size, text) {
    return '<h' + size + '>' + text + '</h' + size + '>';
}

_label = function(text) {
    return '<label>' + text + '</label>';
}

_a = function(href, text) {
    return '<a href="' + href + '">' + text + '</a>';
}

_textinput = function(id, placeholder, value) {
    var ret = '<input type="text" id="' + id + '" placeholder="' + placeholder + '" value="' + value + '"></input>';
    //console.log('_input(): ret = ' + ret);
    return ret;
}

_textarea = function(id, placeholder, rows, contents) {
    var ret = '<textarea id="' + id + '" placeholder="' + placeholder + '" rows="' + rows + '">' + contents + '</textarea>';
    //console.log('_textarea(): ret = ' + ret);
    return ret;
}