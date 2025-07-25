// Animation handling for ReaCenter website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize scroll animations
    initScrollAnimations();
    
    // Add hover effects to cards
    addHoverEffects();
    
    // Add pulse effect to buttons
    addPulseToButtons();
    
    // Add ripple effect to buttons
    addRippleEffect();
    
    // Add 3D hover effect
    add3DHoverEffect();
    
    // Add neon glow effect
    addNeonGlowEffect();
    
    // Add zoom-in animation to images
    addZoomInEffect();
    
    // Add gradient background to selected elements
    addGradientBackground();
    
    // Add swing animation to icons
    addSwingEffect();
});

// Handle scroll animations
function initScrollAnimations() {
    // Get all elements that should animate on scroll
    const fadeElements = document.querySelectorAll('.fade-in-scroll');
    const staggerItems = document.querySelectorAll('.stagger-item');
    
    // Set up the Intersection Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // If element is in view
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Unobserve after animation is triggered
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1 // Trigger when 10% of the element is visible
    });
    
    // Observe all fade elements
    fadeElements.forEach(element => {
        observer.observe(element);
    });
    
    // Handle staggered animations
    staggerItems.forEach((item, index) => {
        // Add delay based on index
        item.style.animationDelay = `${index * 0.1}s`;
        observer.observe(item);
    });
}

// Add hover effects to cards
function addHoverEffects() {
    const cards = document.querySelectorAll('.service_card, .disease_card');
    
    cards.forEach(card => {
        card.classList.add('hover-grow');
    });
}

// Add pulse effect to buttons
function addPulseToButtons() {
    // Отключено по запросу пользователя
    // const ctaButtons = document.querySelectorAll('.button');
    // 
    // ctaButtons.forEach(button => {
    //     button.classList.add('pulse');
    // });
}

// Add ripple effect to buttons
function addRippleEffect() {
    const buttons = document.querySelectorAll('.button, .next_btn, .bordered_btn');
    
    buttons.forEach(button => {
        button.classList.add('ripple');
    });
}

// Add 3D hover effect to cards
function add3DHoverEffect() {
    const cards = document.querySelectorAll('.disease_card');
    
    cards.forEach(card => {
        card.classList.add('hover-3d');
    });
}

// Add neon glow effect to important elements
function addNeonGlowEffect() {
    // Отключено по запросу пользователя
    // const elements = document.querySelectorAll('.bottom_head_section_list_item h1, .what_we_head h1');
    // 
    // elements.forEach(element => {
    //     element.classList.add('neon-glow');
    // });
}

// Add zoom-in animation to images
function addZoomInEffect() {
    const images = document.querySelectorAll('.service_card_image img');
    
    images.forEach(image => {
        image.classList.add('zoom-in');
    });
}

// Add gradient background to selected elements
function addGradientBackground() {
    const elements = document.querySelectorAll('.what_we_news');
    
    elements.forEach(element => {
        element.classList.add('gradient-bg');
    });
}

// Add swing animation to icons
function addSwingEffect() {
    const icons = document.querySelectorAll('.bottom_head_section_list_item img');
    
    icons.forEach(icon => {
        icon.classList.add('swing');
        
        // Add event listener to trigger animation on hover
        icon.addEventListener('mouseenter', function() {
            // Remove and re-add class to restart animation
            this.classList.remove('swing');
            setTimeout(() => {
                this.classList.add('swing');
            }, 10);
        });
    });
}

// Add blink effect to selected elements
function addBlinkEffect() {
    const elements = document.querySelectorAll('.section_title');
    
    elements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.classList.add('blink');
            
            // Remove class after animation completes
            setTimeout(() => {
                this.classList.remove('blink');
            }, 2000);
        });
    });
}

// Add shake effect on click
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('button')) {
        e.target.classList.add('shake');
        
        // Remove class after animation completes
        setTimeout(() => {
            e.target.classList.remove('shake');
        }, 800);
    }
});
