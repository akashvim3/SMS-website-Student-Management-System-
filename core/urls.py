from django.urls import path
from .views import HomeView, DashboardView, AboutView, ContactView, CalendarView, NotificationsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('notifications/', NotificationsView.as_view(), name='notifications'),
] 