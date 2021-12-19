from django.urls import path
from  .  import views
urlpattern = [
    path('', views.home, name ='home'),
    path('room/', views.room, name ='room'),
]