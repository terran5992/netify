$( document ).ready(function() {

    
    
    value = $('.src_value').text();
    $('.src_value').text(0);
    



    var $span = $('.src_value');
    $span.numberAnimate();
    $span.numberAnimate('set', value);


    // MESSAGE TIMEOUT FUNCTION 

    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.message').fadeOut('slow');
    }, 2000); // <-- time in milliseconds, 1000 =  1 sec





});