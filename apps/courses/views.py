from django.views.generic import TemplateView

# Create your views here.

class CoursesListView(TemplateView):
    template_name = "courses/course_list.html"
