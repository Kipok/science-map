$(document).ready(function(){
    var timer;
    $('.value-container').mouseenter(function() {
        var config_id = this.id.slice(6);
        timer = setTimeout(function(){
            $('#config-' + config_id).show();
        }, 500);
    }).mouseleave(function() {
        var config_id = this.id.slice(6);
        timer = setTimeout(function () {
            $('#config-' + config_id).hide();
        }, 500);
    });
});