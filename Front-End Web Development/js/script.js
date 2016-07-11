// Carousel prevent auto-slide
$(function() {

  $('.carousel').carousel({
    interval: false,
  });
});


// Carousel 1 Number Indicators
var total = $('.item.one').length;
var currentIndex = $('div.active.one').index() + 1;
$('#slidetext1').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel1').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.one').index() + 1;
  var total = $('.item.one').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext1').html(text);
});


// Carousel 2 Number Indicators
var total = $('.item.two').length;
var currentIndex = $('div.active.two').index() + 1;
$('#slidetext2').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel2').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.two').index() + 1;
  var total = $('.item.two').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext2').html(text);
});



// Carousel 3 Number Indicators
var total = $('.item.three').length;
var currentIndex = $('div.active.three').index() + 1;
$('#slidetext3').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel3').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.three').index() + 1;
  var total = $('.item.three').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext3').html(text);
});


// Carousel 4 Number Indicators
var total = $('.item.four').length;
var currentIndex = $('div.active.four').index() + 1;
$('#slidetext4').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel4').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.four').index() + 1;
  var total = $('.item.four').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext4').html(text);
});


// Carousel 5 Number Indicators
var total = $('.item.five').length;
var currentIndex = $('div.active.five').index() + 1;
$('#slidetext5').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel5').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.five').index() + 1;
  var total = $('.item.five').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext5').html(text);
});


// Carousel 6 Number Indicators
var total = $('.item.six').length;
var currentIndex = $('div.active.six').index() + 1;
$('#slidetext6').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel6').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.six').index() + 1;
  var total = $('.item.six').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext6').html(text);
});


// Carousel 7 Number Indicators
var total = $('.item.seven').length;
var currentIndex = $('div.active.seven').index() + 1;
$('#slidetext7').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel7').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.seven').index() + 1;
  var total = $('.item.seven').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext7').html(text);
});


// Carousel 8 Number Indicators
var total = $('.item.eight').length;
var currentIndex = $('div.active.eight').index() + 1;
$('#slidetext8').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel8').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.eight').index() + 1;
  var total = $('.item.eight').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext8').html(text);
});


// Carousel 9 Number Indicators
var total = $('.item.nine').length;
var currentIndex = $('div.active.nine').index() + 1;
$('#slidetext9').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel9').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.nine').index() + 1;
  var total = $('.item.nine').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext9').html(text);
});


// Carousel 10 Number Indicators
var total = $('.item.ten').length;
var currentIndex = $('div.active.ten').index() + 1;
$('#slidetext10').html(currentIndex + '-'  + total);

// This triggers after each slide change
$('.carousel10').on('slid.bs.carousel', function () {
  currentIndex = $('div.active.ten').index() + 1;
  var total = $('.item.ten').length;
  // Now display this wherever you want
  var text = currentIndex + '-' + total;
  $('#slidetext10').html(text);
});


// Affix the Previous / Next buttons to appeare after x pixels on Project Page.
var isVisible = false;
$(window).scroll(function(){
     var shouldBeVisible = $(window).scrollTop()>100;
     if (shouldBeVisible && !isVisible) {
          isVisible = true;
          $('#previous').show();
          $('#next').show();
     } else if (isVisible && !shouldBeVisible) {
          isVisible = false;
          $('#previous').hide();
          $('#next').hide();
    }
});


//----------------------------------------------------------------------

// ListView popover image JS
var questionMark1 = document.getElementById("questionMarkImage1");
var questionMark2 = document.getElementById("questionMarkImage2");
var questionMark3 = document.getElementById("questionMarkImage3");
var questionMark4 = document.getElementById("questionMarkImage4");
var questionMark5 = document.getElementById("questionMarkImage5");
var questionMark6 = document.getElementById("questionMarkImage6");
var questionMark7 = document.getElementById("questionMarkImage7");
var questionMark8 = document.getElementById("questionMarkImage8");
var questionMark9 = document.getElementById("questionMarkImage9");
var questionMark10 = document.getElementById("questionMarkImage10");


var image1 = document.getElementById("imageProject1");
var image2 = document.getElementById("imageProject2");
var image3 = document.getElementById("imageProject3");
var image4 = document.getElementById("imageProject4");
var image5 = document.getElementById("imageProject5");
var image6 = document.getElementById("imageProject6");
var image7 = document.getElementById("imageProject7");
var image8 = document.getElementById("imageProject8");
var image9 = document.getElementById("imageProject9");
var image10 = document.getElementById("imageProject10");
var image11 = document.getElementById("imageProject11");
var image12 = document.getElementById("imageProject12");
var image13 = document.getElementById("imageProject13");
var image14 = document.getElementById("imageProject14");
var image15 = document.getElementById("imageProject15");
var image16 = document.getElementById("imageProject16");
var image17 = document.getElementById("imageProject17");
var image18 = document.getElementById("imageProject18");
var image19 = document.getElementById("imageProject19");

var textLine = document.getElementById("p1");

// Show / hide
function show(x, y) {
    x.style.visibility = "visible";
    x.style.zIndex = "-1";
}

function hide(x) {
    x.style.visibility = "hidden";
}

var testImage = document.getElementById("testImage1");
testImage.onmouseover = function() {

}

// Scroll down to buttons on project pages
var projPage = document.getElementById("projectPage");
projPage.onscroll = function () {
  if (document.body.scrollTop > 150) {
      document.getElementById("previous").style.visibility = "visible";
      document.getElementById("next").style.visibility = "visible";
  } else {
      document.getElementById("previous").style.visibility = "hidden";
      document.getElementById("next").style.visibility = "hidden";
  }

}





/*TESTING PAGE*/
function prepareEventHandlers() {

//  var lineSpan = document.getElementById("line");
  var lineLink = document.getElementById("p1");
  lineLink.onmouseover = function() {
    var testImage = document.getElementById("testImage1");
    testImage.style.visibility = "visible";
    testImage.style.zIndex = "-1";
    lineLink.style.zIndex = "2";
  }
  lineLink.onmouseout = function() {
    var testImage = document.getElementById("testImage1");
    testImage.style.visibility = "hidden";
  }
}

window.onload = function() {
  //prep anything we need to
  prepareEventHandlers();
}
