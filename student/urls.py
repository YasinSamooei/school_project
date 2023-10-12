from django.urls import path
from . import views

urlpatterns = [
    path("add", views.AddStudentView.as_view()),
    path("list", views.StudentsListView.as_view()),
    path("add-presence-or-absence", views.AddPresenceOrAbsenceView.as_view()),
]
