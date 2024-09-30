from django.urls import path
from .views import CourseListCreateView, CourseRetrieveUpdateDestroyView

urlpatterns = [
    path('', CourseListCreateView.as_view()),
    path('<int:pk>/', CourseRetrieveUpdateDestroyView.as_view()),
]