from django.urls import path
from . import views

urlpatterns = [
    path('receive/', views.receive_data, name='receive_data'),
    path('', views.display_data, name='display_data'),
]
