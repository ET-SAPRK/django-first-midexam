from django.urls import path
from . import views

urlpatterns = [
     path('', views.apiOverview, name="api-overview"),
     path('student-list/', views.studentList, name="student-list"),
     path('student-list/<str:pk>/', views.detailView, name='student-detail'),
]
