from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentsList
from .serializers import StudentsListSerializer , PresenceOrAbsenceSerializer
from datetime import datetime
from .models import StudentsList
from drf_spectacular.utils import extend_schema , OpenApiParameter


@extend_schema(tags=["بخش دانش آموزان"] , summary="اضافه کردن دانش آموز")
class AddStudentView(APIView):
    serializer_class = StudentsListSerializer
    def post(self, request):
        serializer = StudentsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "done"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["بخش دانش آموزان"] , summary="دریافت لیست کل دانش آموز ها")
class StudentsListView(APIView):
    serializer_class = StudentsListSerializer
    def get(self, request):
        queryset = StudentsList.objects.all()
        serializer = StudentsListSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["بخش حضور و غیاب "] , summary="حضور و غیاب دانش آموزان")
class AddPresenceOrAbsenceView(APIView):
    serializer_class = PresenceOrAbsenceSerializer
    def post(self, request):
        serializer = PresenceOrAbsenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "done"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)