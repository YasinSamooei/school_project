from rest_framework import serializers
from .models import StudentsList , PresenceOrAbsence





class StudentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentsList
        fields = "__all__"


class PresenceOrAbsenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PresenceOrAbsence
        fields = "__all__"

