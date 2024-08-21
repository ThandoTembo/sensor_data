from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sensor_data.urls')),  # Make sure this line is correct
]
