document.addEventListener("DOMContentLoaded", function() {

  /**
    *  Mobile Menu
  **/
  var navicon = document.getElementById('navicon')
  var toggleNav = function (e) {
    var navitem = document.getElementById("main-menu");
    if (navitem.style.display != 'block') {
      //Show menu
      navitem.setAttribute('style', 'display: block; visibility: visible');
      document.getElementById('primary-menu').setAttribute('style', 'width: 100%');
    } else {
      //Hide menu
      navitem.setAttribute('style', 'display: none; visibility: hidden');
      document.getElementById('primary-menu').setAttribute('style', 'width: auto');
    }
  }
  navicon.addEventListener('click', toggleNav)

  /**
    *  Mobile Menu
  **/
  if ( document.getElementById('portfolio') ) {
    $('.site-slider').slick({
      lazyLoad: 'ondemand'
    }).slickLightbox();
  }

});