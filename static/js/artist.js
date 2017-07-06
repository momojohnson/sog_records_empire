$(document).ready(function() {
  $(document).ready(function() {
      $('.slideshow').cycle({
  		fx: 'shuffle' // choose your transition type, ex: fade, scrollUp, shuffle, etc...
  	});
  });
});

$(document).ready(function() {
  $('#slideshow').cycle({
  fx: 'fade',
  pager: '#smallnav',
  pause:   1,
  speed: 1800,
  timeout:  3500
  });
});


  $(function(){
  $('.carousel').carousel({
    interval: 9000
});

});
