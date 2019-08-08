$(document).ready(function(){
    $("#albtn1").on("click", function () {
        $.get( "/annualdays/", function( data ) {
            $( "#body-content" ).html( data );
          });
    });

    $("#albtn2").on("click", function () {
        $.get( "/annuallist/", function( data ) {
            $( "#body-content" ).html( data );
          });
    });

    $("#albtn3").on("click", function () {
        $.get( "/approvallist/", function( data ) {
            $( "#body-content" ).html( data );
          });
    });

    // $(".tabs").tabs();
});


