from django.urls import path
from .views import CoursesListView


app_name = "courses"
urlpatterns = [
    path("", CoursesListView.as_view(), name="courses_list"),
]