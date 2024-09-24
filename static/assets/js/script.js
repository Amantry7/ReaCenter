const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
    },
});
const swiper2 = new Swiper('.swiper-container2', {
    direction: 'horizontal',
    loop: true,
    slidesPerView: 1.5, // Показывать 3.5 слайда по умолчанию
    centeredSlides: true, // Центрировать активный слайд
    spaceBetween: 30, // Отступ между слайдами

    breakpoints: {
        1079: { // Для экранов шириной 1079px и меньше
            slidesPerView: 1.5, // Показывать 1 слайд
            centeredSlides: true, // Отключить центрирование
            spaceBetween: 10, // Уменьшить отступы
        },
        1080: { // Для экранов шириной 1080px и больше
            slidesPerView: 3.5, // Показывать 3.5 слайда
            centeredSlides: true,
            spaceBetween: 30,
        }
    }
});

const swiper3 = new Swiper('.swiper-container3', {
    direction: 'horizontal',
    loop: true,
    slidesPerView: 1.3, // Показывать 3.5 слайда по умолчанию
    centeredSlides: true, // Центрировать активный слайд
    spaceBetween: 30, // Отступ между слайдами

    breakpoints: {
        1079: { // Для экранов шириной 1079px и меньше
            slidesPerView: 1, // Показывать 1 слайд
            centeredSlides: false, // Отключить центрирование
            spaceBetween: 10, // Уменьшить отступы
        },
        1080: { // Для экранов шириной 1080px и больше
            slidesPerView: 3.5, // Показывать 3.5 слайда
            centeredSlides: true,
            spaceBetween: 30,
        }
    }
});

const swiper4 = new Swiper('.swiper-container4', {
    direction: 'horizontal',
    loop: true,
    slidesPerView: 1.3, // Показывать 3.5 слайда по умолчанию
    centeredSlides: true, // Центрировать активный слайд
    spaceBetween: 30, // Отступ между слайдами

    breakpoints: {
        1079: { // Для экранов шириной 1079px и меньше
            slidesPerView: 1.3, // Показывать 1 слайд
            centeredSlides: false, // Отключить центрирование
            spaceBetween: 10, // Уменьшить отступы
        },
        1080: { // Для экранов шириной 1080px и больше
            slidesPerView: 3, // Показывать 3.5 слайда
            centeredSlides: false,
            spaceBetween: 30,
        }
    }
});



