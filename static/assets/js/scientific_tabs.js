// JavaScript для работы табов на странице научной работы

document.addEventListener('DOMContentLoaded', function() {
    // Получаем все кнопки табов и контент табов
    const tabButtons = document.querySelectorAll('.scientific-tab-btn');
    const tabContents = document.querySelectorAll('.scientific-tab-content');
    
    // Функция для активации выбранного таба
    function activateTab(tabId) {
        // Скрываем все контенты табов
        tabContents.forEach(content => {
            content.classList.remove('active');
        });
        
        // Убираем активный класс у всех кнопок
        tabButtons.forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Активируем выбранный таб и его кнопку
        document.getElementById(tabId).classList.add('active');
        document.querySelector(`[data-tab="${tabId}"]`).classList.add('active');
    }
    
    // Добавляем обработчики событий для кнопок табов
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tabId = this.getAttribute('data-tab');
            activateTab(tabId);
            
            // Сохраняем выбранный таб в localStorage
            localStorage.setItem('activeScientificTab', tabId);
        });
    });
    
    // Проверяем, есть ли сохраненный таб в localStorage
    const savedTab = localStorage.getItem('activeScientificTab');
    if (savedTab && document.getElementById(savedTab)) {
        // Если есть, активируем его
        activateTab(savedTab);
    } else {
        // Иначе активируем первый таб
        const firstTabId = tabButtons[0].getAttribute('data-tab');
        activateTab(firstTabId);
    }
    
    // Проверяем, есть ли хэш в URL (для прямых ссылок на секции)
    if (window.location.hash) {
        const hash = window.location.hash.substring(1);
        if (document.getElementById(hash)) {
            activateTab(hash);
            // Плавная прокрутка к секции
            setTimeout(() => {
                document.getElementById(hash).scrollIntoView({
                    behavior: 'smooth'
                });
            }, 100);
        }
    }
});
