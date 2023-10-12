from django.urls import path
from . import views

urlpatterns = [
    path("add", views.AddStudentView.as_view()),
]
