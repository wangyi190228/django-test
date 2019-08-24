$(document).ready(function(){
    var tempflag = true;
    if (tempflag) {
        tempflag = false;
        $(".alli1").button().css({
            "background-color":"#6495ED",
            "padding":"5px",
        });
        $(".alli2,.alli3,.alli4").button().css({
            "background-color":"#98F5FF",
            "padding":"5px",
        });
    }
    if (!tempflag){
        $("#albtn1").on("click", function () {
            $(".alli1").css("background-color","#6495ED");
            $(".alli2,.alli3,.alli4").css("background-color","#98F5FF");
            $.get( "/annualdays/", function( data ) {
                $( "#body-content" ).html( data );
              });
        });
    
        $("#albtn2").on("click", function () {
            $(".alli2").css("background-color","#6495ED");
            $(".alli1,.alli3,.alli4").css("background-color","#98F5FF");
            $.get( "/annuallist/", function( data ) {
                $( "#body-content" ).html( data );
              });
        });
    
        $("#albtn3").on("click", function () {
            $(".alli1,.alli2,.alli4").css("background-color","#98F5FF");
            $(".alli3").css("background-color","#6495ED");
            $.get( "/approvallist/", function( data ) {
                $( "#body-content" ).html( data );
              });
        });
    
        $("#albtn4").on("click", function () {
            $(".alli1,.alli2,.alli3").css("background-color","#98F5FF");
            $(".alli4").css("background-color","#6495ED");
            $.get( "/staffleave/", function( data ) {
                $( "#body-content" ).html( data );
              });
        });
    }
});


