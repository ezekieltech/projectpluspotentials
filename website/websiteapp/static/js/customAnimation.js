function animateCSS(element, animationName, callback) {
    const node = document.querySelector(element)
    node.classList.add('animated', animationName)

    function handleAnimationEnd() {
        node.classList.remove('animated', animationName)
        node.removeEventListener('animationend', handleAnimationEnd)


        if (typeof callback === 'function') callback()
    }

    node.addEventListener('animationend', handleAnimationEnd)
}

function reset($elem) {
    $elem.before($elem.clone(true));
    var $newElem = $elem.prev();
    $elem.remove();
    return $newElem;
} // end reset()

//add animation to main text box on home page
$(".main-title-box").addClass("fadeInUp animated")

//animateCSS ('.main-title-bx', 'fadeInUp',function(){
    //$(".main-title-box").addClass("fadeOut animated")
//});


 /* or
animateCSS('.main-title-box', 'fadeInUp', function() {
  // Do something after animation
  $(".main-title-box").addEventListener('animationend', function () {
      var $this = $(this);
      $this.removeClass();
      $this = reset($this);
      $this.addClass("fadeInDown animated");
  });
})
const element =  document.querySelector('.main-title-box')
element.classList.add('animated', 'fadeInUp')


// reset the transition by...
element.addEventListener("animationend", function(e) {
  e.preventDefault;

  // -> removing the class
  element.classList.remove("fadeInUp");

  // -> triggering reflow /* The actual magic */
  // without this it wouldn't work. Try uncommenting the line and the transition won't be retriggered.
  // Oops! This won't work in strict mode. Thanks Felis Phasma!
  // element.offsetWidth = element.offsetWidth;
  // Do this instead:
  //void element.offsetWidth;

  // -> and re-adding the class
  //element.classList.add("fadeOut");
//}, false);

/***********************************
Add Active Class to Current Element in Navigation
***********************************
// Get the container element
var btnContainer = document.getElementById("testin");

console.log("got here");

// Get all buttons with class="nav-link" inside the container
var btns = btnContainer.getElementsByClassName("nav-item-top");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}*/

$( '#testin a' ).on( 'click', function () {
    console.log('got here');
	$( '#testing' ).find( 'li.active' ).removeClass( 'active' );
	$( this ).parent( 'li' ).addClass( 'active' );
});


/*testing shuffle and filter on product page
var Shuffle = window.Shuffle;
var jQuery = window.jQuery;

var myShuffle = new Shuffle(document.querySelector('.my-shuffle'), {
itemSelector: '.image-item',
sizer: '.my-sizer-element',
buffer: 1,
});

jQuery('input[name="shuffle-filter"]').on('change', function (evt) {
var input = evt.currentTarget;
if (input.checked) {
myShuffle.filter(input.value);
}
}); */
