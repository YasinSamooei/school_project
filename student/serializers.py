from rest_framework import serializers
from .models import StudentsList





class StudentsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentsList
        fields = "__all__"

