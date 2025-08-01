# Student Management System

A comprehensive Django-based Student Management System designed to streamline academic administration, student records management, and attendance tracking for educational institutions.

## Features

### 🔐 User Management
- **Multi-role Authentication**: Support for Admin, Teacher, and Student roles
- **User Profiles**: Extended user profiles with personal and academic information
- **Profile Pictures**: Image upload and automatic resizing functionality
- **Role-based Access Control**: Different permissions and views based on user type

### 📚 Academic Management
- **Course Management**: Create and manage academic courses with codes and descriptions
- **Class/Section Management**: Organize students into classes and sections
- **Subject Management**: Manage subjects with credit systems and teacher assignments
- **Assignment System**: Create and track assignments with due dates and scoring

### ���� Attendance System
- **Daily Attendance**: Record student attendance for each class and subject
- **Multiple Status Types**: Present, Absent, Late, and Excused attendance statuses
- **Attendance Reports**: Monthly summaries with percentage calculations
- **Teacher-specific Records**: Teachers can manage attendance for their assigned subjects

### 👥 User Types

#### Admin
- Full system access and management
- User account creation and management
- System configuration and oversight

#### Teacher
- Manage assigned classes and subjects
- Record and track student attendance
- Create and manage assignments
- View student academic records

#### Student
- View personal academic information
- Access attendance records and summaries
- View assignments and academic progress

## Technology Stack

- **Backend**: Django 5.1.1
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: HTML, CSS, JavaScript with Bootstrap 4
- **Forms**: Django Crispy Forms with Bootstrap 4 styling
- **Image Processing**: Pillow (PIL)
- **UI Components**: Widget Tweaks for enhanced form rendering

## Project Structure

```
student_management_system/
├── accounts/              # User management and authentication
├── academics/             # Course, class, and subject management
├── attendance/            # Attendance tracking and reporting
├── core/                  # Core application views and utilities
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates
├── exports/               # Generated reports and exports
├── student_management_system/  # Main project configuration
├── manage.py              # Django management script
└── db.sqlite3            # SQLite database file
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Student management system"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==5.1.1
   pip install pillow
   pip install django-crispy-forms
   pip install crispy-bootstrap4
   pip install django-widget-tweaks
   ```

4. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Configuration

### Settings
The main configuration file is located at `student_management_system/settings.py`. Key configurations include:

- **Database**: Currently configured for SQLite (development)
- **Static Files**: Configured for local development
- **Media Files**: Profile pictures and uploads
- **Authentication**: Custom login/logout redirects
- **Internationalization**: English (US) with UTC timezone

### Environment Variables
For production deployment, consider setting:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False for production
- `ALLOWED_HOSTS`: Configure allowed hostnames
- Database credentials (if using PostgreSQL/MySQL)

## Usage

### Getting Started
1. **Admin Setup**: Use the superuser account to access the admin panel
2. **Create User Profiles**: Add teachers and students through the admin interface
3. **Academic Setup**: Create courses, classes, and subjects
4. **Assign Teachers**: Assign teachers to subjects and classes
5. **Enroll Students**: Add students to appropriate classes
6. **Daily Operations**: Teachers can record attendance and manage assignments

### Key Workflows

#### For Administrators
- Manage user accounts and profiles
- Set up academic structure (courses, classes, subjects)
- Generate reports and analytics
- System maintenance and configuration

#### For Teachers
- Record daily attendance for assigned classes
- Create and manage assignments
- View student academic progress
- Generate attendance reports

#### For Students
- View personal academic information
- Check attendance records and summaries
- Access assignment details and deadlines
- Track academic progress

## Database Models

### Core Models
- **UserProfile**: Extended user information with role-based fields
- **Course**: Academic course definitions
- **Class**: Class/section organization
- **Subject**: Subject management with teacher assignments
- **Assignment**: Assignment creation and tracking
- **AttendanceRecord**: Daily attendance sessions
- **StudentAttendance**: Individual student attendance status
- **AttendanceSummary**: Monthly attendance analytics

## Security Features

- CSRF protection enabled
- User authentication and authorization
- Role-based access control
- Secure file upload handling
- SQL injection prevention through Django ORM

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support, bug reports, or feature requests, please create an issue in the repository or contact the development team.

## Future Enhancements

- **Grade Management**: Complete grading system with report cards
- **Parent Portal**: Parent access to student information
- **Mobile App**: Mobile application for easier access
- **Advanced Reporting**: Detailed analytics and reporting features
- **Online Examinations**: Digital examination system
- **Library Management**: Integration with library systems
- **Fee Management**: Student fee tracking and payment systems
- **Notification System**: Email/SMS notifications for important updates

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Django Version**: 5.1.1