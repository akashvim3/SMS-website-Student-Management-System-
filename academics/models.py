from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from accounts.models import UserProfile

class Course(models.Model):
    """Course model"""
    name = models.CharField(_('Course Name'), max_length=100)
    code = models.CharField(_('Course Code'), max_length=20, unique=True)
    description = models.TextField(_('Description'), blank=True)
    duration = models.PositiveIntegerField(_('Duration (years)'), default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})


class Class(models.Model):
    """Class/Section model"""
    name = models.CharField(_('Class Name'), max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes')
    year = models.PositiveIntegerField(_('Year'))
    section = models.CharField(_('Section'), max_length=10, blank=True)
    class_teacher = models.ForeignKey(
        UserProfile, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='classes_taught',
        limit_choices_to={'user_type': 'teacher'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Classes')
        ordering = ['course', 'year', 'section']
        unique_together = ('course', 'year', 'section')
    
    def __str__(self):
        if self.section:
            return f"{self.course.name} - Year {self.year} - Section {self.section}"
        return f"{self.course.name} - Year {self.year}"
    
    def get_absolute_url(self):
        return reverse('class_detail', kwargs={'pk': self.pk})


class Subject(models.Model):
    """Subject model"""
    name = models.CharField(_('Subject Name'), max_length=100)
    code = models.CharField(_('Subject Code'), max_length=20, unique=True)
    description = models.TextField(_('Description'), blank=True)
    credits = models.PositiveIntegerField(_('Credits'), default=3)
    classes = models.ManyToManyField(Class, related_name='subjects')
    teachers = models.ManyToManyField(
        UserProfile, 
        related_name='subjects_taught',
        limit_choices_to={'user_type': 'teacher'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={'pk': self.pk})


class Assignment(models.Model):
    """Assignment model"""
    title = models.CharField(_('Title'), max_length=100)
    description = models.TextField(_('Description'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignments')
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='assignments')
    due_date = models.DateField(_('Due Date'))
    max_score = models.PositiveIntegerField(_('Maximum Score'), default=100)
    created_by = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        related_name='assignments_created',
        limit_choices_to={'user_type': 'teacher'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Assignment')
        verbose_name_plural = _('Assignments')
        ordering = ['-due_date']
    
    def __str__(self):
        return f"{self.title} - {self.subject.name} ({self.assigned_class})"
