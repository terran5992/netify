$( document ).ready(function() {

    
    
    var all = document.getElementsByClassName("src_value");

    sum = 0;
    $(all).each(function() {
        sum += parseFloat($(this).val());
    });

    var n = sum.toString();

    document.getElementsByClassName("net_worth").innerHTML = 0 ;

    var $span = $('.net_worth');
    $span.numberAnimate();
    $span.numberAnimate('set', n);

    // Loops over the sources and animates the value

    // STUCK HERE , HAVENT BEEN ABLE TO SELECT THE SOURCE AND ANIMATE THE VALUE

    $( ".source_value" ).each(function( index ) {
        value = ($(this).text()).toString();
        $(this).text(0);
        $(this).numberAnimate();
        $(this).numberAnimate('set', value);
        // console.log( index + ": " + $( this ).text() );
    });






    // MESSAGE TIMEOUT FUNCTION 

    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.message').fadeOut('slow');
    }, 2000); // <-- time in milliseconds, 1000 =  1 sec





});