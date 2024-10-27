from django.urls import path

from regular_exam_project_27102024.common.views import HomePageView, DashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
