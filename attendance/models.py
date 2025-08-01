from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from accounts.models import UserProfile
from academics.models import Class, Subject

class AttendanceRecord(models.Model):
    """Attendance record for a class on a specific date"""
    date = models.DateField(_('Date'), default=timezone.now)
    class_record = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendance_records')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendance_records')
    teacher = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        related_name='attendance_records_taken',
        limit_choices_to={'user_type': 'teacher'}
    )
    remarks = models.TextField(_('Remarks'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Attendance Record')
        verbose_name_plural = _('Attendance Records')
        ordering = ['-date']
        unique_together = ('date', 'class_record', 'subject')
    
    def __str__(self):
        return f"{self.class_record} - {self.subject.name} - {self.date}"


class StudentAttendance(models.Model):
    """Individual student attendance status"""
    STATUS_CHOICES = (
        ('present', _('Present')),
        ('absent', _('Absent')),
        ('late', _('Late')),
        ('excused', _('Excused')),
    )
    
    attendance_record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE, related_name='student_attendance')
    student = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        related_name='attendance_records',
        limit_choices_to={'user_type': 'student'}
    )
    status = models.CharField(_('Status'), max_length=10, choices=STATUS_CHOICES, default='present')
    remarks = models.CharField(_('Remarks'), max_length=100, blank=True)
    
    class Meta:
        verbose_name = _('Student Attendance')
        verbose_name_plural = _('Student Attendances')
        unique_together = ('attendance_record', 'student')
        
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.get_status_display()} ({self.attendance_record.date})"


class AttendanceSummary(models.Model):
    """Monthly attendance summary for reporting"""
    student = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        related_name='attendance_summaries',
        limit_choices_to={'user_type': 'student'}
    )
    class_record = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendance_summaries')
    month = models.PositiveIntegerField(_('Month'))
    year = models.PositiveIntegerField(_('Year'))
    total_days = models.PositiveIntegerField(_('Total Working Days'))
    present_days = models.PositiveIntegerField(_('Days Present'))
    absent_days = models.PositiveIntegerField(_('Days Absent'))
    late_days = models.PositiveIntegerField(_('Days Late'))
    excused_days = models.PositiveIntegerField(_('Days Excused'))
    attendance_percentage = models.DecimalField(_('Attendance Percentage'), max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name = _('Attendance Summary')
        verbose_name_plural = _('Attendance Summaries')
        ordering = ['-year', '-month']
        unique_together = ('student', 'class_record', 'month', 'year')
        
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.month}/{self.year} - {self.attendance_percentage}%"
    
    def save(self, *args, **kwargs):
        """Auto-calculate attendance percentage"""
        if self.total_days > 0:
            self.attendance_percentage = (self.present_days / self.total_days) * 100
        else:
            self.attendance_percentage = 0
        super().save(*args, **kwargs)
