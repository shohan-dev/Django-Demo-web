from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from students.views import *

# add the static line

urlpatterns = [
    path('', home),
    path("about", about),
    path("student", student_s),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
