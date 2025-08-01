from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'core/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    """Dashboard page view - requires login"""
    template_name = 'core/dashboard.html'


class AboutView(TemplateView):
    """About page view"""
    template_name = 'core/about.html'


class ContactView(TemplateView):
    """Contact page view"""
    template_name = 'core/contact.html'


class CalendarView(TemplateView):
    """Academic Calendar view"""
    template_name = 'core/calendar.html'


class NotificationsView(LoginRequiredMixin, TemplateView):
    """Notifications view - requires login"""
    template_name = 'core/notifications.html' 