document.addEventListener('DOMContentLoaded', function() {
    // Main header slider
    const mainSwiper = new Swiper('.swiper-main', {
        // Core settings
        loop: true,
        effect: 'fade',
        speed: 1000,
        autoplay: {
            delay: 4000,
            disableOnInteraction: false,
        },
        
        // Navigation
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        
        // Pagination
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            dynamicBullets: true,
        },
    });
    
    // Other swipers can be initialized here
});
