// Image Lightbox for Scientific Work Page

document.addEventListener('DOMContentLoaded', function() {
    // Create the lightbox elements
    createLightbox();
    
    // Add click event listeners to all scientific material images
    initializeImageClicks();
});

// Create the lightbox elements and append to the body
function createLightbox() {
    // Create the lightbox container
    const lightbox = document.createElement('div');
    lightbox.id = 'scientific-lightbox';
    lightbox.className = 'scientific-lightbox';
    lightbox.style.display = 'none';
    
    // Create the lightbox content
    const lightboxContent = document.createElement('div');
    lightboxContent.className = 'scientific-lightbox-content';
    
    // Create the close button
    const closeButton = document.createElement('span');
    closeButton.className = 'scientific-lightbox-close';
    closeButton.innerHTML = '&times;';
    closeButton.onclick = closeLightbox;
    closeButton.setAttribute('title', 'Закрыть');
    
    // Create the image element
    const lightboxImage = document.createElement('img');
    lightboxImage.className = 'scientific-lightbox-image';
    
    // Create image title element
    const imageTitle = document.createElement('div');
    imageTitle.className = 'scientific-lightbox-title';
    
    // Assemble the lightbox
    lightboxContent.appendChild(closeButton);
    lightboxContent.appendChild(lightboxImage);
    lightboxContent.appendChild(imageTitle);
    lightbox.appendChild(lightboxContent);
    
    // Add the lightbox to the document body
    document.body.appendChild(lightbox);
    
    // Close lightbox when clicking outside the image
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });
    
    // Add keyboard support (Escape to close)
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.style.display === 'flex') {
            closeLightbox();
        }
    });
}

// Initialize click events on all scientific material images
function initializeImageClicks() {
    const images = document.querySelectorAll('.scientific-material-image img');
    
    images.forEach(img => {
        // Add cursor pointer to indicate it's clickable
        img.style.cursor = 'pointer';
        
        // Add click event
        img.addEventListener('click', function() {
            openLightbox(this.src, this.alt);
        });
    });
}

// Open the lightbox with the selected image
function openLightbox(imageSrc, imageAlt) {
    const lightbox = document.getElementById('scientific-lightbox');
    const lightboxImage = document.querySelector('.scientific-lightbox-image');
    const lightboxTitle = document.querySelector('.scientific-lightbox-title');
    
    // Set the image source and alt text
    lightboxImage.src = imageSrc;
    lightboxImage.alt = imageAlt || '';
    
    // Find the parent card to get more context about the image
    let parentCard = null;
    const allImages = document.querySelectorAll('.scientific-material-image img');
    for (let img of allImages) {
        if (img.src === imageSrc) {
            parentCard = img.closest('.scientific-material-card');
            break;
        }
    }
    
    // Set the title from the card if available
    if (parentCard) {
        const cardTitle = parentCard.querySelector('h3');
        const cardDescription = parentCard.querySelector('p');
        
        if (cardTitle) {
            lightboxTitle.textContent = cardTitle.textContent;
        } else {
            lightboxTitle.textContent = imageAlt || '';
        }
    } else {
        lightboxTitle.textContent = imageAlt || '';
    }
    
    // Add loading animation
    lightboxImage.style.opacity = '0';
    
    // Show the lightbox with a fade-in effect
    lightbox.style.display = 'flex';
    setTimeout(() => {
        lightbox.style.opacity = '1';
    }, 10);
    
    // When image is loaded, fade it in
    lightboxImage.onload = function() {
        lightboxImage.style.opacity = '1';
    };
    
    // Prevent scrolling of the body when lightbox is open
    document.body.style.overflow = 'hidden';
}

// Close the lightbox
function closeLightbox() {
    const lightbox = document.getElementById('scientific-lightbox');
    
    // Fade out effect
    lightbox.style.opacity = '0';
    setTimeout(() => {
        lightbox.style.display = 'none';
    }, 300);
    
    // Re-enable scrolling
    document.body.style.overflow = '';
}
