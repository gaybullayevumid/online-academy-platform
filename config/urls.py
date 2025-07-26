from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.courses.urls", namespace="courses")),
    # path("paymnets/", include("apps.payments.urls", namespace="payments")),
    # path("quizzes/", include("apps.quizzes.urls", namespace="quizzes")),
    # path("certificates/", include("apps.certificates.urls", namespace="certificates")),
    # path("enrollments/", include("apps.enrollments.urls", namespace="enrollments")),
    # path("users/", include("apps.users.urls", namespace="users")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]