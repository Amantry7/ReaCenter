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
    slidesPerView: 'auto', // Автоматический размер для поддержки разных форматов (Shorts и обычные)
    centeredSlides: true, // Центрировать активный слайд
    spaceBetween: 30, // Отступ между слайдами

    breakpoints: {
        1079: { // Для экранов шириной 1079px и меньше
            slidesPerView: 'auto', // Автоматический размер
            centeredSlides: true,
            spaceBetween: 20, // Уменьшить отступы
        },
        1080: { // Для экранов шириной 1080px и больше
            slidesPerView: 'auto', // Автоматический размер для смешанных форматов
            centeredSlides: true,
            spaceBetween: 30,
        }
    }
});

const swiper3 = new Swiper('.swiper-container3', {
    direction: 'horizontal',
    loop: true,
    slidesPerView: 1, // Показывать только 1 слайд на мобильных
    centeredSlides: true, // Центрировать активный слайд
    spaceBetween: 20, // Отступ между слайдами
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    watchOverflow: true, // Следить за переполнением
    observer: true, // Обновлять слайдер при изменении элементов
    observeParents: true, // Обновлять слайдер при изменении родительских элементов

    breakpoints: {
        320: { // Для маленьких мобильных экранов
            slidesPerView: 1,
            spaceBetween: 20,
            centeredSlides: true,
        },
        480: { // Для средних мобильных экранов
            slidesPerView: 1,
            spaceBetween: 20,
            centeredSlides: true,
        },
        768: { // Для планшетов
            slidesPerView: 2,
            spaceBetween: 20,
            centeredSlides: true,
        },
        1080: { // Для экранов шириной 1080px и больше
            slidesPerView: 3, // Показывать 3 слайда
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

const aboutUsDocSwiper = new Swiper('.swiper-container-docs', {
    direction: 'horizontal',
    loop: true,
    slidesPerView: 3, // Показываем 3 слайда на десктопе
    spaceBetween: 20,

    // Добавляем пагинацию
    pagination: {
        el: '.swiper-pagination-docs',
        clickable: true,
    },

    // Добавляем навигационные стрелки
    navigation: {
        nextEl: '.swiper-button-next-docs',
        prevEl: '.swiper-button-prev-docs',
    },

    // Адаптивные настройки
    breakpoints: {
        // Для мобильных
        320: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        // Для планшетов
        768: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        // Для десктопов
        1024: {
            slidesPerView: 3,
            spaceBetween: 30,
        }
    }
});
