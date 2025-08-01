# Icons Directory

This directory contains custom icons used throughout the Student Management System. While the system primarily uses Font Awesome icons, some custom icons are stored here for specific functionality.

## Icon Categories

- **Subject Icons** - Icons representing different academic subjects
- **Department Icons** - Icons for different departments
- **Feature Icons** - Icons representing different features of the system
- **Status Icons** - Icons representing different status indicators
- **Custom Icons** - Special custom icons for the system

## File Naming Convention

Icons should be named using the following pattern:
`category-name-size.format`

Examples:
- `subject-mathematics-24.svg`
- `department-science-32.png`
- `feature-attendance-16.svg`
- `status-active-16.png`

## Recommended Formats

- SVG is preferred for vector icons (scalable without quality loss)
- PNG with transparency for raster icons
- Icons should be available in multiple sizes: 16x16, 24x24, 32x32, 48x48

## Organization

Icons are organized in subdirectories by category:
```
icons/
├── subjects/
│   ├── mathematics.svg
│   ├── science.svg
│   └── ...
├── departments/
│   ├── science.svg
│   ├── arts.svg
│   └── ...
├── features/
│   ├── attendance.svg
│   ├── grades.svg
│   └── ...
├── status/
│   ├── active.svg
│   ├── pending.svg
│   └── ...
└── custom/
    ├── logo-small.svg
    ├── favicon.ico
    └── ...
```

## Usage in Code

To use these icons in templates:
```html
<img src="{% static 'images/icons/subjects/mathematics.svg' %}" alt="Mathematics">
```

## Notes

- Keep icons consistent in style and color scheme
- Ensure icons are optimized for web use
- Prefer SVG format when possible for better scaling across devices
- Consider accessibility when choosing colors and designs 