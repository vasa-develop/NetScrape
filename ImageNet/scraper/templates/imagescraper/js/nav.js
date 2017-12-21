$(window).scroll(function() {
	if($(document).scrollTop() < 200) {
  	$('.navbar-default').removeClass('opaque') ;
  }
  else {
  $('.navbar-default').addClass('opaque');
  }
});
