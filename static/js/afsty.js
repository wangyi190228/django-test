$(document).ready(function(){
    $(".tabs").tabs();
    $("#albtn1").on("click", function () {
        $.get( "/annual/", function( data ) {
            $( ".result" ).html( data );
          });
    });
});
