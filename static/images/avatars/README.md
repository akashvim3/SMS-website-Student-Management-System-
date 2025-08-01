# Avatar Images Directory

This directory contains profile images for users in the Student Management System.

## Naming Convention

For student profile pictures, use the format: `student_[id].jpg` or `student_[id].png`
For teacher profile pictures, use the format: `teacher_[id].jpg` or `teacher_[id].png`
For admin profile pictures, use the format: `admin_[id].jpg` or `admin_[id].png`

## Default Avatars

Default avatars for users who haven't uploaded a profile picture are:
- `default_student.png` - Default student avatar
- `default_teacher.png` - Default teacher avatar
- `default_admin.png` - Default admin avatar
- `default_male.png` - Default male avatar
- `default_female.png` - Default female avatar

## Requirements

- Images should be square for best results (1:1 aspect ratio)
- Recommended size: 500x500 pixels
- Maximum file size: 2MB
- Supported formats: .jpg, .jpeg, .png

## File Structure
```
avatars/
├── default_admin.png
├── default_female.png
├── default_male.png
├── default_student.png
├── default_teacher.png
├── student_1001.jpg
├── student_1002.jpg
└── ... etc
```

## Notes

You should place real avatar images in this directory. The Student Management System will resize and crop images as needed based on where they are displayed (e.g., profiles, tables, comments, etc.).