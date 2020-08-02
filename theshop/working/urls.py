from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name="about"),
    path('service/', views.services, name="service"),
    path('contactnifo/', views.contactnifo, name="contactnifo"),
    path('showPost', views.showPost)
]