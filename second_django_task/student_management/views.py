from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


#Pagination
def student_list(request, page=1, per_page=0):
    # Fetch all student records
    students = Student.objects.all()

    # Handle search functionality
    search_name = request.GET.get('search_name')
    if search_name:
        students = students.filter(name__icontains=search_name)

    # Create Paginator instance
    paginator = Paginator(students, per_page)

    # Get the records for the requested page
    page_obj = paginator.get_page(page)

    if search_name:
        return render(request, 'student_list.html', {'page_obj': page_obj, 'per_page': per_page, 'page': page,'search':search_name})

    return render(request, 'student_list.html', {'page_obj': page_obj, 'per_page': per_page, 'page': page}) 