from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('feature/',views.feature, name="feature"),
    path('contact/',views.contact, name="contact"),
] 

