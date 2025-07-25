from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("paymnets/", include("apps.payments.urls", namespace="payments")),
    # path("quizzes/", include("apps.quizzes.urls", namespace="quizzes")),
    # path("certificates/", include("apps.certificates.urls", namespace="certificates")),
    # path("enrollments/", include("apps.enrollments.urls", namespace="enrollments")),
    path("", include("apps.courses.urls", namespace="courses")),
    # path("users/", include("apps.users.urls", namespace="users")),
]
