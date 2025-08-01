# Logo Directory

This directory contains the official logo files for the Student Management System in various formats and sizes.

## Available Logo Files

- `logo.svg` - Vector version of the main logo (preferred for web use)
- `logo.png` - PNG version of the main logo with transparency
- `logo-dark.svg` - Vector version of the logo for dark backgrounds
- `logo-dark.png` - PNG version of the logo for dark backgrounds
- `logo-small.svg` - Small vector version of the logo for compact spaces
- `logo-small-dark.svg` - Small vector version of the logo for dark backgrounds
- `logo-small.png` - Small PNG version of the logo for compact spaces
- `favicon.ico` - Favicon file for browser tabs
- `apple-touch-icon.png` - Icon for iOS devices when adding to home screen
- `android-chrome-192x192.png` - Icon for Android devices
- `android-chrome-512x512.png` - Larger icon for Android devices

## Logo Sizes and Formats

- Main logo: 200×60px (SVG is scalable)
- Small logo: 60×60px (SVG is scalable)
- Favicon: 16×16px, 32×32px, 48×48px (multi-size ICO)
- Apple Touch Icon: 180×180px
- Android Chrome Icons: 192×192px and 512×512px

## Usage Guidelines

1. Always use the SVG version when possible for best quality
2. Use the dark version of the logo on dark backgrounds
3. For small spaces (like mobile headers), use the small logo version
4. Do not stretch, distort, or change the colors of the logo
5. Maintain adequate spacing around the logo (at least equal to the height of the graduation cap icon)

## Implementation in Templates

```html
<!-- Default usage in header -->
<a class="navbar-brand" href="{% url 'home' %}">
    <img src="{% static 'images/logo/logo.svg' %}" alt="Student Management System" height="40">
</a>

<!-- For dark backgrounds -->
<footer class="bg-dark">
    <img src="{% static 'images/logo/logo-dark.svg' %}" alt="Student Management System" height="40">
</footer>

<!-- For small spaces -->
<div class="mobile-header">
    <img src="{% static 'images/logo/logo-small.svg' %}" alt="SMS" width="60" height="60">
</div>

<!-- For small spaces on dark backgrounds -->
<div class="mobile-header-dark">
    <img src="{% static 'images/logo/logo-small-dark.svg' %}" alt="SMS" width="60" height="60">
</div>
```

## Favicon Implementation

In the base template's head section:

```html
<link rel="icon" href="{% static 'images/logo/favicon.ico' %}" sizes="any">
<link rel="icon" href="{% static 'images/logo/favicon.svg' %}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{% static 'images/logo/apple-touch-icon.png' %}">
<link rel="manifest" href="{% static 'site.webmanifest' %}">
```

## Responsive Logo Usage

For responsive designs, consider using different logo versions based on screen size:

```html
<picture>
  <source media="(max-width: 576px)" srcset="{% static 'images/logo/logo-small.svg' %}">
  <source media="(min-width: 577px)" srcset="{% static 'images/logo/logo.svg' %}">
  <img src="{% static 'images/logo/logo.svg' %}" alt="Student Management System">
</picture>
```

## Best Practices

- **Consistent Placement**: Place the logo in the same position across all pages
- **Responsive Sizing**: Scale the logo appropriately for different screen sizes
- **Appropriate Spacing**: Maintain adequate whitespace around the logo (minimum clearance should be 10px)
- **Contrast**: Ensure the logo has sufficient contrast against its background
- **File Types**: Use SVG for web interfaces and PNG for email templates or contexts where SVG might not be supported
- **Dark Mode**: Use logo-dark variants when implementing dark mode themes

## Notes

- The SVG logo versions are preferred as they scale well for all screen resolutions
- For print materials, high-resolution PNG versions can be provided upon request
- Do not regenerate or recreate the logo without authorization
- The color scheme uses the primary blue (#4e73df) which matches the application's theme