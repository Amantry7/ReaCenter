/**
 * JavaScript для обработки скачивания PDF-файлов
 */

document.addEventListener('DOMContentLoaded', function() {
    // Находим все кнопки скачивания на странице
    const downloadButtons = document.querySelectorAll('.download-btn');
    
    // Для каждой кнопки добавляем обработчик события
    downloadButtons.forEach(button => {
        // Получаем текст кнопки
        const buttonText = button.textContent.trim();
        
        // Получаем родительский элемент с информацией о материале
        const infoBlock = button.closest('.scientific-material-info');
        
        if (infoBlock) {
            // Получаем заголовок материала
            const title = infoBlock.querySelector('h3').textContent.trim();
            
            // Проверяем, есть ли уже установленный атрибут data-pdf
            // Если атрибут уже установлен в HTML, используем его
            // Иначе, формируем путь на основе заголовка
            if (!button.hasAttribute('data-pdf')) {
                // Формируем имя файла на основе заголовка
                const fileName = title.replace(/[^\w\s]/gi, '').replace(/\s+/g, '_') + '.pdf';
                
                // Определяем тип материала на основе родительских классов
                let folderName = 'manuals';
                const cardElement = button.closest('.scientific-material-card');
                
                if (cardElement) {
                    if (cardElement.classList.contains('patent-card')) {
                        folderName = 'patents';
                    } else if (cardElement.classList.contains('permission-card')) {
                        folderName = 'permissions';
                    } else if (cardElement.classList.contains('publication-card')) {
                        folderName = 'publications';
                    } else if (cardElement.classList.contains('journal-card')) {
                        folderName = 'journals';
                    }
                }
                
                // Формируем путь к PDF файлу
                const pdfPath = `/static/assets/documents/scientific/${folderName}/${fileName}`;
                
                // Устанавливаем атрибуты для кнопки
                button.setAttribute('data-pdf', pdfPath);
                button.setAttribute('data-title', fileName);
            }
            
            // Устанавливаем href для совместимости
            button.setAttribute('href', 'javascript:void(0)');
            
            // Добавляем обработчик события клика
            button.addEventListener('click', function() {
                const pdfUrl = this.getAttribute('data-pdf');
                const pdfTitle = this.getAttribute('data-title');
                
                if (pdfUrl) {
                    // Показываем сообщение о скачивании
                    alert(`Скачивание файла "${pdfTitle}" начнется автоматически.\nЕсли скачивание не началось, пожалуйста, проверьте настройки браузера.`);
                    
                    // Создаем ссылку для скачивания
                    const link = document.createElement('a');
                    link.href = pdfUrl;
                    link.download = pdfTitle;
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                } else {
                    alert('Извините, файл недоступен для скачивания.');
                }
            });
        }
    });
    
    // Добавляем модальное окно для просмотра документов
    addDocumentViewerModal();
});

/**
 * Добавляет модальное окно для просмотра документов
 */
function addDocumentViewerModal() {
    // Проверяем, существует ли уже модальное окно
    if (!document.getElementById('doc-modal')) {
        // Создаем элементы модального окна
        const modal = document.createElement('div');
        modal.id = 'doc-modal';
        modal.className = 'doc-modal';
        
        const modalContent = document.createElement('iframe');
        modalContent.id = 'doc-modal-content';
        modalContent.className = 'doc-modal-content';
        
        const closeBtn = document.createElement('span');
        closeBtn.className = 'doc-modal-close';
        closeBtn.innerHTML = '&times;';
        
        // Добавляем элементы в DOM
        modal.appendChild(closeBtn);
        modal.appendChild(modalContent);
        document.body.appendChild(modal);
        
        // Добавляем обработчики событий
        closeBtn.addEventListener('click', function() {
            modal.style.display = 'none';
        });
        
        window.addEventListener('click', function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    }
}
