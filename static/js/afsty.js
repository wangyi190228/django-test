$(document).ready(function(){

    // $(".tabs").tabs();

    $(".alli1").css("background-color","#6495ED");

    var test = window.location.href;
    if(test.indexOf("#asb")>=0)
    {
        $(".alli1").css("background-color","#98F5FF");
        $(".alli2").css("background-color","#6495ED");
        $(".alli3").css("background-color","#98F5FF");
        $.get( "/annuallist/", function( data ) {
            $( "#body-content" ).html( data );
          });
        
    }

    $("#albtn1").on("click", function () {
        $(".alli1").css("background-color","#6495ED");
        $(".alli2").css("background-color","#98F5FF");
        $(".alli3").css("background-color","#98F5FF");
        $.get( "/annualdays/", function( data ) {
            $( "#body-content" ).html( data );
          });
    });

    $("#albtn2").on("click", function () {
        $(".alli1").css("background-color","#98F5FF");
        $(".alli2").css("background-color","#6495ED");
        $(".alli3").css("background-color","#98F5FF");
        $.get( "/annuallist/", function( data ) {
            $( "#body-content" ).html( data );
          });
    });

    $("#albtn3").on("click", function () {
        $(".alli1").css("background-color","#98F5FF");
        $(".alli2").css("background-color","#98F5FF");
        $(".alli3").css("background-color","#6495ED");
        $.get( "/approvallist/", function( data ) {
            $( "#body-content" ).html( data );
          });
    });

});


