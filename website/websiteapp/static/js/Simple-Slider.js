$(function(){

    // Initializing the swiper plugin for the slider.
    // Read more here: http://idangero.us/swiper/api/

    var mySwiper = new Swiper ('.swiper-container', {
        runCallbacksOnInit: true,
        spaceBetween: 100,
        simulateTouch: true,
        followFinger: true,
        loop: true,
        pagination: '.swiper-pagination',
        paginationClickable: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        grabCursor: true,
        spee: 100000,
        effect: 'cube',
        cubeEffect: {
            slideShadows: false
             }
    });




})
