/**
 * Student Management System - Theme Customization
 * This file contains theme-specific customizations and UI-related functionality
 */

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme preferences
    initThemePreferences();
    
    // Initialize scrollbars
    initScrollbars();
    
    // Theme toggle buttons
    initThemeToggle();
    
    // Animate page elements
    initAnimations();
    
    // Initialize responsive behaviors
    initResponsiveBehaviors();
});

/**
 * Initialize theme preferences from localStorage
 */
function initThemePreferences() {
    // Check if user has a saved theme preference
    const savedTheme = localStorage.getItem('theme');
    const savedSidebar = localStorage.getItem('sidebar');
    
    // Apply theme if saved
    if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.checked = savedTheme === 'dark';
        }
    }
    
    // Apply sidebar state if saved
    if (savedSidebar === 'collapsed') {
        document.body.classList.add('sidebar-toggled');
        document.querySelector('.sidebar')?.classList.add('toggled');
    }
}

/**
 * Initialize custom scrollbars
 */
function initScrollbars() {
    // Apply custom scrollbars to sidebar
    const sidebar = document.querySelector('.sidebar');
    if (sidebar && typeof SimpleBar !== 'undefined') {
        new SimpleBar(sidebar);
    }
    
    // Apply to other elements if needed
    const scrollElements = document.querySelectorAll('.custom-scrollbar');
    if (scrollElements.length && typeof SimpleBar !== 'undefined') {
        scrollElements.forEach(element => {
            new SimpleBar(element);
        });
    }
}

/**
 * Initialize theme toggle functionality
 */
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('change', function() {
            const newTheme = this.checked ? 'dark' : 'light';
            document.body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            // Update sidebar colors based on theme
            updateSidebarTheme(newTheme);
        });
    }
    
    // Theme buttons if present
    const themeButtons = document.querySelectorAll('.theme-button');
    themeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const newTheme = this.getAttribute('data-theme');
            document.body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            // Update sidebar colors based on theme
            updateSidebarTheme(newTheme);
            
            // Update toggle if exists
            const themeToggle = document.getElementById('theme-toggle');
            if (themeToggle) {
                themeToggle.checked = newTheme === 'dark';
            }
        });
    });
}

/**
 * Update sidebar colors based on theme
 */
function updateSidebarTheme(theme) {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;
    
    if (theme === 'dark') {
        sidebar.classList.add('sidebar-dark');
        sidebar.classList.remove('sidebar-light');
    } else {
        sidebar.classList.add('sidebar-light');
        sidebar.classList.remove('sidebar-dark');
    }
}

/**
 * Initialize animations for UI elements
 */
function initAnimations() {
    // Animate cards on page load
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.05}s`;
        card.classList.add('fade-in');
    });
    
    // Animate stats counters
    animateStatCounters();
    
    // Animate progress bars
    animateProgressBars();
}

/**
 * Animate statistics counters for dashboard
 */
function animateStatCounters() {
    const counters = document.querySelectorAll('.counter-value');
    
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 1500; // milliseconds
        const step = Math.ceil(target / (duration / 16)); // 60fps approx
        
        let current = 0;
        const updateCounter = () => {
            current += step;
            if (current < target) {
                counter.textContent = current;
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    });
}

/**
 * Animate progress bars
 */
function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    progressBars.forEach(bar => {
        const value = bar.getAttribute('aria-valuenow');
        bar.style.width = '0%';
        
        setTimeout(() => {
            bar.style.transition = 'width 1s ease-in-out';
            bar.style.width = `${value}%`;
        }, 100);
    });
}

/**
 * Initialize responsive behaviors
 */
function initResponsiveBehaviors() {
    // Handle sidebar behavior on smaller screens
    const handleResize = () => {
        if (window.innerWidth < 768) {
            document.body.classList.add('sidebar-toggled');
            document.querySelector('.sidebar')?.classList.add('toggled');
        } else {
            // Only restore if user hasn't manually collapsed
            if (localStorage.getItem('sidebar') !== 'collapsed') {
                document.body.classList.remove('sidebar-toggled');
                document.querySelector('.sidebar')?.classList.remove('toggled');
            }
        }
    };
    
    // Run on load
    handleResize();
    
    // Add window resize listener
    window.addEventListener('resize', handleResize);
    
    // Store sidebar state
    const sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            const isToggled = document.querySelector('.sidebar')?.classList.contains('toggled');
            localStorage.setItem('sidebar', isToggled ? 'expanded' : 'collapsed');
        });
    }
}

/**
 * Card layout and organization functions
 */
const layoutHelpers = {
    // Adjust card heights to match in a row
    equalizeCardHeights: function() {
        const cardRows = document.querySelectorAll('.row');
        cardRows.forEach(row => {
            const cards = row.querySelectorAll('.card');
            if (cards.length > 1) {
                let maxHeight = 0;
                
                // Reset heights
                cards.forEach(card => {
                    card.style.height = 'auto';
                    maxHeight = Math.max(maxHeight, card.offsetHeight);
                });
                
                // Apply max height
                cards.forEach(card => {
                    card.style.height = `${maxHeight}px`;
                });
            }
        });
    },
    
    // Save current card layout
    saveLayout: function() {
        const dashboard = document.querySelector('.dashboard-grid');
        if (!dashboard) return;
        
        const cards = dashboard.querySelectorAll('.card');
        const layout = [];
        
        cards.forEach(card => {
            const id = card.id;
            const parent = card.parentNode;
            const index = Array.from(parent.children).indexOf(card);
            
            layout.push({
                id,
                parent: parent.id,
                index
            });
        });
        
        localStorage.setItem('dashboardLayout', JSON.stringify(layout));
    },
    
    // Restore saved layout
    restoreLayout: function() {
        const savedLayout = localStorage.getItem('dashboardLayout');
        if (!savedLayout) return;
        
        const layout = JSON.parse(savedLayout);
        
        layout.forEach(item => {
            const card = document.getElementById(item.id);
            const parent = document.getElementById(item.parent);
            
            if (card && parent) {
                if (item.index === 0) {
                    parent.prepend(card);
                } else {
                    const children = parent.children;
                    if (item.index >= children.length) {
                        parent.appendChild(card);
                    } else {
                        parent.insertBefore(card, children[item.index]);
                    }
                }
            }
        });
    }
};

// Custom events for theme changes
const customEvents = {
    themeChanged: new CustomEvent('themeChanged', {
        detail: { theme: document.body.getAttribute('data-theme') }
    })
};

// Dispatch event when theme changes
function dispatchThemeChangedEvent(theme) {
    customEvents.themeChanged.detail.theme = theme;
    document.dispatchEvent(customEvents.themeChanged);
} 