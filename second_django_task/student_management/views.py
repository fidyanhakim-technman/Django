# student_management/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Standard, Student
from .serializers import StandardSerializer, StudentSerializer

class StandardList(APIView):
    def get(self, request):
        standards = Standard.objects.all()
        serializer = StandardSerializer(standards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StandardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StandardDetail(APIView):
    def get_object(self, pk):
        try:
            return Standard.objects.get(pk=pk)
        except Standard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        standard = self.get_object(pk)
        serializer = StandardSerializer(standard)
        return Response(serializer.data)

    def put(self, request, pk):
        standard = self.get_object(pk)
        serializer = StandardSerializer(standard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        standard = self.get_object(pk)
        standard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
