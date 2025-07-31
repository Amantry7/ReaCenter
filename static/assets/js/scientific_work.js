/**
 * JavaScript для страницы "Научные работы"
 */

document.addEventListener('DOMContentLoaded', function() {
    // Инициализация обработчиков для скачивания PDF
    initDownloadHandlers();
    
    // Инициализация модальных окон для просмотра документов
    initDocumentViewers();
});

/**
 * Инициализирует обработчики для кнопок скачивания
 */
function initDownloadHandlers() {
    const downloadButtons = document.querySelectorAll('.download-btn');
    
    downloadButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const pdfUrl = this.getAttribute('data-pdf');
            
            if (pdfUrl) {
                // Если URL задан, начинаем скачивание
                downloadPDF(pdfUrl, this.getAttribute('data-title') || 'document.pdf');
            } else {
                console.error('URL для скачивания не указан');
            }
        });
    });
}

/**
 * Инициализирует просмотрщики документов
 */
function initDocumentViewers() {
    const viewButtons = document.querySelectorAll('.view-btn');
    const modal = document.getElementById('doc-modal');
    const modalImg = document.getElementById('doc-modal-content');
    const closeBtn = document.querySelector('.doc-modal-close');
    
    if (!modal || !modalImg || !closeBtn) return;
    
    viewButtons.forEach(button => {
        button.addEventListener('click', function() {
            const pdfUrl = this.getAttribute('data-pdf');
            
            if (pdfUrl) {
                modal.style.display = "block";
                modalImg.src = pdfUrl;
            }
        });
    });
    
    closeBtn.addEventListener('click', function() {
        modal.style.display = "none";
    });
    
    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
}

/**
 * Функция для скачивания PDF файла
 * @param {string} url - URL файла для скачивания
 * @param {string} filename - Имя файла при скачивании
 */
function downloadPDF(url, filename) {
    fetch(url)
        .then(response => response.blob())
        .then(blob => {
            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = filename;
            link.click();
            window.URL.revokeObjectURL(link.href);
        })
        .catch(error => {
            console.error('Ошибка при скачивании файла:', error);
            alert('Произошла ошибка при скачивании файла. Пожалуйста, попробуйте позже.');
        });
}
