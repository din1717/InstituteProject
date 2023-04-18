
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('studapi/', include('student.urls')),
    path('user_management/', include('register.urls')),

]
"http://127.0.0.1:8000/user_management/register"
