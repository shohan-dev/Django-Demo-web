from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api_send_get.views import *
from home.views import *
from students.views import *
from shop.views import *

# Define URLs and corresponding views for product-related functionality
product_urls = [
    path("product_data/", get_data),
    path("about/", about),
    path("student/", student_s),
    path("register/", register),
    path("email/", send_mail_from_user),
    path("login/", login_page),
    path("logout/", logout_page),
]

# Define other URLs and corresponding views
other_urls = [
    path('', home),
    path("table/", table),
    path("get_data/", get_filtered_data),
    path("send_data/", post_data),
    path("send_data_file/", post_data_file),
    path("delete_txt_table/<int:id>/", delete_txt),
    path("update_table/<int:id>/", update_table),
    path('admin/', admin.site.urls),
]

# Combine all URL patterns
urlpatterns = other_urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += product_urls

