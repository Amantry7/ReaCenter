// Scientific Work Page Animations

document.addEventListener('DOMContentLoaded', function() {
    // Add hover effects and subtle animations
    initAnimations();
});

// Initialize all animations
function initAnimations() {
    // Add subtle entrance animations
    addEntranceAnimations();
    
    // Add hover effects to cards
    addCardHoverEffects();
    
    // Add hover effects to buttons
    addButtonHoverEffects();
}

// Add subtle entrance animations with staggered timing
function addEntranceAnimations() {
    // Add animation delays to sections
    const sections = document.querySelectorAll('.scientific-work-section');
    sections.forEach((section, index) => {
        // Make sure all sections are visible
        section.style.opacity = '1';
        // Add a small delay between sections
        section.style.animationDelay = `${0.2 * index}s`;
    });
    
    // Add staggered animation to cards within each grid
    const grids = document.querySelectorAll('.scientific-materials-grid');
    grids.forEach(grid => {
        const cards = grid.querySelectorAll('.scientific-material-card');
        cards.forEach((card, index) => {
            // Make sure all cards are visible
            card.style.opacity = '1';
            // Add a small delay between cards
            card.style.animationDelay = `${0.1 * (index + 1)}s`;
        });
    });
}

// Add hover effects to cards
function addCardHoverEffects() {
    const cards = document.querySelectorAll('.scientific-material-card');
    
    cards.forEach(card => {
        // Make sure card is visible
        card.style.opacity = '1';
        
        // Add hover event listeners
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.15)';
            
            // Find and animate the image
            const img = this.querySelector('.scientific-material-image img');
            if (img) {
                img.style.transform = 'scale(1.05)';
            }
            
            // Find and animate the info section
            const info = this.querySelector('.scientific-material-info');
            if (info) {
                info.style.transform = 'translateY(-5px)';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
            
            // Reset image
            const img = this.querySelector('.scientific-material-image img');
            if (img) {
                img.style.transform = 'scale(1)';
            }
            
            // Reset info section
            const info = this.querySelector('.scientific-material-info');
            if (info) {
                info.style.transform = 'translateY(0)';
            }
        });
    });
}

// Add hover effects to buttons
function addButtonHoverEffects() {
    const buttons = document.querySelectorAll('.download-btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#0056b3';
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
            this.style.transform = 'translateY(0)';
        });
    });
}
