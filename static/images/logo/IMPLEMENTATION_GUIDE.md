# Logo Implementation Guide

This guide provides detailed instructions for implementing the Student Management System (SMS) logos across various parts of the application.

## Base Layout Implementation

Add the following code to your base template (`base.html` or similar):

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Favicon implementation -->
    <link rel="icon" href="{% static 'images/logo/favicon.ico' %}" sizes="any">
    <link rel="apple-touch-icon" href="{% static 'images/logo/apple-touch-icon.png' %}">
    <link rel="manifest" href="{% static 'site.webmanifest' %}">
    <!-- Other head elements -->
</head>
<body>
    <header>
        <nav class="navbar">
            <a class="navbar-brand" href="{% url 'home' %}">
                <img src="{% static 'images/logo/logo.svg' %}" alt="Student Management System" height="40">
            </a>
            <!-- Other navigation elements -->
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer class="bg-dark text-white">
        <div class="container">
            <img src="{% static 'images/logo/logo-dark.svg' %}" alt="Student Management System" height="30">
            <p>© {% now "Y" %} Student Management System. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

## Responsive Logo Implementation

For a responsive design that adapts to different screen sizes:

```html
<a class="navbar-brand" href="{% url 'home' %}">
    <picture>
        <source media="(max-width: 576px)" srcset="{% static 'images/logo/logo-small.svg' %}">
        <source media="(min-width: 577px)" srcset="{% static 'images/logo/logo.svg' %}">
        <img src="{% static 'images/logo/logo.svg' %}" alt="Student Management System" 
             class="img-fluid" style="max-height: 40px;">
    </picture>
</a>
```

## Dark Mode Implementation

If your application supports dark mode toggling:

```html
<a class="navbar-brand" href="{% url 'home' %}">
    <img src="{% static 'images/logo/logo.svg' %}" alt="Student Management System" 
         class="logo-light" height="40">
    <img src="{% static 'images/logo/logo-dark.svg' %}" alt="Student Management System" 
         class="logo-dark" height="40" style="display: none;">
</a>

<script>
// Example dark mode toggle
document.getElementById('darkModeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    
    // Toggle logo visibility
    const logoLight = document.querySelector('.logo-light');
    const logoDark = document.querySelector('.logo-dark');
    
    if (document.body.classList.contains('dark-mode')) {
        logoLight.style.display = 'none';
        logoDark.style.display = 'inline-block';
    } else {
        logoLight.style.display = 'inline-block';
        logoDark.style.display = 'none';
    }
});
</script>
```

## Mobile Navigation Implementation

For mobile navigation with the small logo:

```html
<div class="mobile-header d-block d-md-none">
    <div class="container">
        <div class="d-flex justify-content-between align-items-center">
            <a href="{% url 'home' %}">
                <img src="{% static 'images/logo/logo-small.svg' %}" alt="SMS" width="40" height="40">
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarMobile">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>
    </div>
</div>
```

## Email Template Implementation

For email templates, use the PNG version of the logo:

```html
<div style="text-align: center; margin-bottom: 20px;">
    <img src="{{ site_url }}{% static 'images/logo/logo.png' %}" alt="Student Management System" 
         style="max-width: 200px; height: auto;">
</div>
```

In Django, you'll need to include the full URL in emails:

```python
from django.contrib.sites.shortcuts import get_current_site

def send_email(request, user_email):
    current_site = get_current_site(request)
    site_url = f"https://{current_site.domain}"
    # Use site_url in your email template context
```

## Login Page Implementation

For the login page, center the logo with appropriate spacing:

```html
<div class="login-container">
    <div class="text-center mb-4">
        <img src="{% static 'images/logo/logo.svg' %}" alt="Student Management System" 
             class="img-fluid" style="max-width: 250px;">
    </div>
    <!-- Login form follows -->
</div>
```

## Print Stylesheet

For print-friendly pages, ensure the logo displays properly:

```css
@media print {
    .navbar-brand img {
        height: 30px !important;
        print-color-adjust: exact;
        -webkit-print-color-adjust: exact;
    }
}
```

## Best Practices Reminders

1. Never stretch or distort the logo - always maintain its aspect ratio
2. Keep adequate whitespace around the logo
3. Use the appropriate version (light/dark) based on the background color
4. For UI components requiring a square logo, use the small logo variants
5. When implementing dark mode, ensure you toggle between appropriate logo versions 