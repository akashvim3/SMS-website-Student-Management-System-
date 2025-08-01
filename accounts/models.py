from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from PIL import Image

# User types
USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
)

class UserProfile(models.Model):
    """Extended user profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Personal information
    user_type = models.CharField(_('User Type'), max_length=10, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(_('Date of Birth'), null=True, blank=True)
    address = models.TextField(_('Address'), blank=True)
    phone_number = models.CharField(_('Phone Number'), max_length=15, blank=True)
    profile_picture = models.ImageField(_('Profile Picture'), upload_to='profile_pics', default='default_profile.png')
    
    # Academic information (for students)
    student_id = models.CharField(_('Student ID'), max_length=20, blank=True)
    admission_date = models.DateField(_('Admission Date'), null=True, blank=True)
    
    # Academic information (for teachers)
    teacher_id = models.CharField(_('Teacher ID'), max_length=20, blank=True)
    qualification = models.CharField(_('Qualification'), max_length=100, blank=True)
    joining_date = models.DateField(_('Joining Date'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
    
    def __str__(self):
        return f"{self.user.username}'s Profile ({self.user_type})"
    
    def save(self, *args, **kwargs):
        """Resize profile picture on save"""
        super().save(*args, **kwargs)
        
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)
