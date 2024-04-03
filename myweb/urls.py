from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from students.views import *
from shop.views import *

# PRODUCT_URL = [
#     path("product_data/", get_data),
    
# ]

urlpatterns = [
    path('', home),
    path("product_data/", get_data),
    path("about/", about),  # Add trailing slashes to all paths
    path("student/", student_s),
    path("register/", register),
    path("login/", login_page),  # Add trailing slash here
    path("logout/", logout_page),  # Add trailing slashes to all paths
    path("table/", table),
    path("delete_txt_table/<int:id>/", delete_txt),  # Add trailing slash here
    path("update_table/<int:id>/", update_table),  # Add trailing slash here
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

