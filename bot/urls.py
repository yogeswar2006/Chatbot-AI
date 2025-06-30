from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    
    path('room/<int:room_id>/', views.home, name='room'),
    
    path('chat-api/<int:room_id>/', views.chat_api, name='chat_api'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.registerPage,name='register'),
   
   
   path('create-room/', views.create_room, name='create_room'),
   
   

]