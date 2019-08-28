$(document).ready(function () {
    $(".alaplbtn").button().css({
        "background-color":"#98F5FF",
        "margin-left":"950px",
        "margin-top":"-100px",
        "padding":"5px",
    });

    $(".subapp").button().css({
        "width":"80px",
        "margin-left":"40px",
        "background-color":"#98F5FF",
        "padding":"5px",  
    });

    $("#startin").datepicker({
        minDate:0,
        onClose:function(datatext){
            $("#stopin").datepicker("option","minDate",datatext);
        },
    });
    $("#stopin").datepicker({
        minDate:0,
        onClose:function(datatext){
            $("#startin").datepicker("option","maxDate",datatext);
        },
    });

});