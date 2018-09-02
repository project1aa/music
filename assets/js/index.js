$(window).scroll(function() {

  var myScrollTop = $(window).scrollTop();

  if (myScrollTop > 0) { /* Direction : down */
    $('.navbar-fixed-top').css({"opacity" : "0.90"});
    
  } 
  else { /* Direction : up */
    $('.navbar-fixed-top').css({"opacity" : "1" , "visibility" : "visible"});
  }

});

