from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import UserProfile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class RegisterView(CreateView):
    """User registration view"""
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, _('Your account has been created. You can now log in.'))
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    """User profile view"""
    model = UserProfile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    
    def get_object(self):
        """Return the user's profile"""
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """User profile update view"""
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        """Add both forms to context"""
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
            context['profile_form'] = ProfileUpdateForm(self.request.POST, self.request.FILES, instance=self.request.user.profile)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
            context['profile_form'] = ProfileUpdateForm(instance=self.request.user.profile)
        return context
    
    def form_valid(self, form):
        """Process both forms"""
        context = self.get_context_data()
        user_form = context['user_form']
        profile_form = context['profile_form']
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(self.request, _('Your profile has been updated!'))
            return redirect('profile')
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    def get_object(self):
        """Return the user's profile"""
        return self.request.user.profile


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin to require staff status"""
    def test_func(self):
        """Test if user is staff"""
        return self.request.user.is_staff


class StudentListView(StaffRequiredMixin, ListView):
    """View for listing all students"""
    model = UserProfile
    template_name = 'accounts/student_list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        """Filter to show only students"""
        return UserProfile.objects.filter(user_type='student')


class TeacherListView(StaffRequiredMixin, ListView):
    """View for listing all teachers"""
    model = UserProfile
    template_name = 'accounts/teacher_list.html'
    context_object_name = 'teachers'
    
    def get_queryset(self):
        """Filter to show only teachers"""
        return UserProfile.objects.filter(user_type='teacher')


class AdminListView(StaffRequiredMixin, ListView):
    """View for listing all admins"""
    model = UserProfile
    template_name = 'accounts/admin_list.html'
    context_object_name = 'admins'
    
    def get_queryset(self):
        """Filter to show only admins"""
        return UserProfile.objects.filter(user_type='admin')
