from django.contrib import admin
from .models import StudentsList , Grade , PresenceOrAbsence



@admin.register(StudentsList)
class StudentsListAdmin(admin.ModelAdmin):
    list_display = ("fullname", "grade")
    search_fields = ("grade", "fullname")

admin.site.register(Grade)

admin.site.register(PresenceOrAbsence)