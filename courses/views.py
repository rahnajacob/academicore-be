from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializers.common import CourseSerializer
from utils.decorators import handle_exceptions
# Create your views here.

class CourseListCreateView(APIView):
    @handle_exceptions
    def get(self, request):
        courses= Course.objects.all()
        serialized_courses= CourseSerializer(courses, many=True)
        print(serialized_courses.data)
        return Response(serialized_courses.data)

    @handle_exceptions
    def post(self, request):
            course_to_create = CourseSerializer(data = request.data)
            if course_to_create.is_valid():
                course_to_create.save()
                return Response(course_to_create.data, 201)
            print("validation error:", course_to_create.error)
            return Response(course_to_create.errors, 400)

class CourseRetrieveUpdateDestroyView(APIView):

    @handle_exceptions
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serialized_course=CourseSerializer(course)
        print(serialized_course)
        return Response(serialized_course.data)
    
    @handle_exceptions
    def put(self, request, pk):
        course_to_update = Course.objects.get(pk=pk)
        serialized_course= CourseSerializer(course_to_update, data = request.data, partial=True)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        return Response(serialized_course.errors, 400)
    
    @handle_exceptions
    def delete(self, request, pk):
        course_to_delete= Course.objects.get(pk=pk)
        print('Deleteing:', course_to_delete)
        course_to_delete.delete()
        return Response(status=204)

