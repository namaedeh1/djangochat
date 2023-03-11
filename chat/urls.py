from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # we're passing a variable into this particular url named room
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]