from django.urls import path
from .views import (
    AttendanceListView, AttendanceDetailView,
    AttendanceCreateView, AttendanceUpdateView, AttendanceDeleteView,
    ClassAttendanceView, StudentAttendanceView, AttendanceReportView
)

urlpatterns = [
    # Attendance URLs
    path('', AttendanceListView.as_view(), name='attendance_list'),
    path('<int:pk>/', AttendanceDetailView.as_view(), name='attendance_detail'),
    path('create/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('<int:pk>/update/', AttendanceUpdateView.as_view(), name='attendance_update'),
    path('<int:pk>/delete/', AttendanceDeleteView.as_view(), name='attendance_delete'),
    
    # Attendance views by class and student
    path('class/<int:class_id>/', ClassAttendanceView.as_view(), name='class_attendance'),
    path('student/<int:student_id>/', StudentAttendanceView.as_view(), name='student_attendance'),
    
    # Reports
    path('reports/', AttendanceReportView.as_view(), name='attendance_reports'),
]