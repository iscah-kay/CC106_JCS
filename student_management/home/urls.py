from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('Home/', RedirectView.as_view(pattern_name='home', permanent=False)),
]