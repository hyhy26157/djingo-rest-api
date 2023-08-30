from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from first_app import views #for the include

urlpatterns = [
    
    re_path(r'^photo/', include('first_app.urls')),
    path('admin/', admin.site.urls),
]   
