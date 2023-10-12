from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentsList
from .serializers import StudentsListSerializer
from datetime import datetime



class AddStudentView(APIView):
    serializer_class = StudentsListSerializer
    def post(self, request):
        serializer = StudentsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "done"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


