from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ugc_tracker', views.ugc_tracker, name='ugc_tracker')
]