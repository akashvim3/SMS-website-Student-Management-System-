from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import Course, Class, Subject, Assignment

# Staff required mixin
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin to require staff status"""
    def test_func(self):
        """Test if user is staff"""
        return self.request.user.is_staff


# Course views
class CourseListView(LoginRequiredMixin, ListView):
    """View for listing all courses"""
    model = Course
    template_name = 'academics/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10


class CourseDetailView(LoginRequiredMixin, DetailView):
    """View for displaying course details"""
    model = Course
    template_name = 'academics/course_detail.html'
    context_object_name = 'course'


class CourseCreateView(StaffRequiredMixin, CreateView):
    """View for creating a new course"""
    model = Course
    template_name = 'academics/course_form.html'
    fields = ['name', 'code', 'description', 'duration']
    success_url = reverse_lazy('course_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Course created successfully!'))
        return super().form_valid(form)


class CourseUpdateView(StaffRequiredMixin, UpdateView):
    """View for updating an existing course"""
    model = Course
    template_name = 'academics/course_form.html'
    fields = ['name', 'code', 'description', 'duration']
    
    def form_valid(self, form):
        messages.success(self.request, _('Course updated successfully!'))
        return super().form_valid(form)


class CourseDeleteView(StaffRequiredMixin, DeleteView):
    """View for deleting a course"""
    model = Course
    template_name = 'academics/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Course deleted successfully!'))
        return super().delete(request, *args, **kwargs)


# Class views
class ClassListView(LoginRequiredMixin, ListView):
    """View for listing all classes"""
    model = Class
    template_name = 'academics/class_list.html'
    context_object_name = 'classes'
    paginate_by = 10


class ClassDetailView(LoginRequiredMixin, DetailView):
    """View for displaying class details"""
    model = Class
    template_name = 'academics/class_detail.html'
    context_object_name = 'class'


class ClassCreateView(StaffRequiredMixin, CreateView):
    """View for creating a new class"""
    model = Class
    template_name = 'academics/class_form.html'
    fields = ['name', 'course', 'year', 'section', 'class_teacher']
    success_url = reverse_lazy('class_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Class created successfully!'))
        return super().form_valid(form)


class ClassUpdateView(StaffRequiredMixin, UpdateView):
    """View for updating an existing class"""
    model = Class
    template_name = 'academics/class_form.html'
    fields = ['name', 'course', 'year', 'section', 'class_teacher']
    
    def form_valid(self, form):
        messages.success(self.request, _('Class updated successfully!'))
        return super().form_valid(form)


class ClassDeleteView(StaffRequiredMixin, DeleteView):
    """View for deleting a class"""
    model = Class
    template_name = 'academics/class_confirm_delete.html'
    success_url = reverse_lazy('class_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Class deleted successfully!'))
        return super().delete(request, *args, **kwargs)


# Subject views
class SubjectListView(LoginRequiredMixin, ListView):
    """View for listing all subjects"""
    model = Subject
    template_name = 'academics/subject_list.html'
    context_object_name = 'subjects'
    paginate_by = 10


class SubjectDetailView(LoginRequiredMixin, DetailView):
    """View for displaying subject details"""
    model = Subject
    template_name = 'academics/subject_detail.html'
    context_object_name = 'subject'


class SubjectCreateView(StaffRequiredMixin, CreateView):
    """View for creating a new subject"""
    model = Subject
    template_name = 'academics/subject_form.html'
    fields = ['name', 'code', 'description', 'credits', 'classes', 'teachers']
    success_url = reverse_lazy('subject_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Subject created successfully!'))
        return super().form_valid(form)


class SubjectUpdateView(StaffRequiredMixin, UpdateView):
    """View for updating an existing subject"""
    model = Subject
    template_name = 'academics/subject_form.html'
    fields = ['name', 'code', 'description', 'credits', 'classes', 'teachers']
    
    def form_valid(self, form):
        messages.success(self.request, _('Subject updated successfully!'))
        return super().form_valid(form)


class SubjectDeleteView(StaffRequiredMixin, DeleteView):
    """View for deleting a subject"""
    model = Subject
    template_name = 'academics/subject_confirm_delete.html'
    success_url = reverse_lazy('subject_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Subject deleted successfully!'))
        return super().delete(request, *args, **kwargs)
