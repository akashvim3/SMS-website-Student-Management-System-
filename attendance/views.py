from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, Sum, Avg
from django.http import JsonResponse

from .models import AttendanceRecord, StudentAttendance, AttendanceSummary
from academics.models import Class, Subject
from accounts.models import UserProfile

# Staff required mixin
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin to require staff status"""
    def test_func(self):
        """Test if user is staff"""
        return self.request.user.is_staff


# Attendance record views
class AttendanceListView(LoginRequiredMixin, ListView):
    """View for listing all attendance records"""
    model = AttendanceRecord
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'attendance_records'
    paginate_by = 10
    
    def get_queryset(self):
        """Filter records based on user type"""
        queryset = AttendanceRecord.objects.all()
        
        # If teacher, show only their records
        if hasattr(self.request.user, 'profile') and self.request.user.profile.user_type == 'teacher':
            queryset = queryset.filter(teacher=self.request.user.profile)
            
        return queryset.order_by('-date')


class AttendanceDetailView(LoginRequiredMixin, DetailView):
    """View for displaying attendance record details"""
    model = AttendanceRecord
    template_name = 'attendance/attendance_detail.html'
    context_object_name = 'attendance_record'
    
    def get_context_data(self, **kwargs):
        """Add student attendance data to context"""
        context = super().get_context_data(**kwargs)
        context['student_attendance'] = StudentAttendance.objects.filter(
            attendance_record=self.object
        ).order_by('student__user__first_name')
        return context


class AttendanceCreateView(StaffRequiredMixin, CreateView):
    """View for creating new attendance records"""
    model = AttendanceRecord
    template_name = 'attendance/attendance_form.html'
    fields = ['date', 'class_record', 'subject', 'remarks']
    success_url = reverse_lazy('attendance_list')
    
    def form_valid(self, form):
        """Set the teacher and create student attendance records"""
        form.instance.teacher = self.request.user.profile
        response = super().form_valid(form)
        
        # Create attendance records for all students in the class
        class_obj = form.instance.class_record
        students = UserProfile.objects.filter(user_type='student')  # Later we'll add logic to link students to classes
        
        for student in students:
            StudentAttendance.objects.create(
                attendance_record=form.instance,
                student=student,
                status='present'  # Default status
            )
        
        messages.success(self.request, _('Attendance record created successfully! Please mark individual student attendance.'))
        return response


class AttendanceUpdateView(StaffRequiredMixin, UpdateView):
    """View for updating attendance records"""
    model = AttendanceRecord
    template_name = 'attendance/attendance_form.html'
    fields = ['date', 'class_record', 'subject', 'remarks']
    
    def form_valid(self, form):
        messages.success(self.request, _('Attendance record updated successfully!'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('attendance_detail', kwargs={'pk': self.object.pk})


class AttendanceDeleteView(StaffRequiredMixin, DeleteView):
    """View for deleting attendance records"""
    model = AttendanceRecord
    template_name = 'attendance/attendance_confirm_delete.html'
    success_url = reverse_lazy('attendance_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Attendance record deleted successfully!'))
        return super().delete(request, *args, **kwargs)


class ClassAttendanceView(LoginRequiredMixin, ListView):
    """View for displaying attendance by class"""
    model = AttendanceRecord
    template_name = 'attendance/class_attendance.html'
    context_object_name = 'attendance_records'
    paginate_by = 10
    
    def get_queryset(self):
        """Filter records by class"""
        self.class_obj = get_object_or_404(Class, pk=self.kwargs['class_id'])
        return AttendanceRecord.objects.filter(class_record=self.class_obj).order_by('-date')
    
    def get_context_data(self, **kwargs):
        """Add class object to context"""
        context = super().get_context_data(**kwargs)
        context['class'] = self.class_obj
        return context


class StudentAttendanceView(LoginRequiredMixin, ListView):
    """View for displaying attendance by student"""
    model = StudentAttendance
    template_name = 'attendance/student_attendance.html'
    context_object_name = 'student_attendance'
    paginate_by = 20
    
    def get_queryset(self):
        """Filter attendance by student"""
        self.student = get_object_or_404(UserProfile, pk=self.kwargs['student_id'], user_type='student')
        return StudentAttendance.objects.filter(student=self.student).order_by('-attendance_record__date')
    
    def get_context_data(self, **kwargs):
        """Add student object and summary to context"""
        context = super().get_context_data(**kwargs)
        context['student'] = self.student
        
        # Get attendance statistics
        attendance_stats = StudentAttendance.objects.filter(student=self.student).values('status').annotate(count=Count('status'))
        context['stats'] = {item['status']: item['count'] for item in attendance_stats}
        
        return context


class AttendanceReportView(StaffRequiredMixin, TemplateView):
    """View for attendance reports and statistics"""
    template_name = 'attendance/attendance_reports.html'
    
    def get_context_data(self, **kwargs):
        """Add report data to context"""
        context = super().get_context_data(**kwargs)
        
        # Get all classes
        context['classes'] = Class.objects.all()
        
        # Get monthly summaries if a class is selected
        class_id = self.request.GET.get('class_id')
        if class_id:
            class_obj = get_object_or_404(Class, pk=class_id)
            context['selected_class'] = class_obj
            context['summaries'] = AttendanceSummary.objects.filter(
                class_record=class_obj
            ).order_by('-year', '-month')
            
        return context
