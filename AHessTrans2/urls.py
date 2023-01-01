from django.urls import path
from .views import (
    base,
    login,
    register,
    logoutUser,
    settingsProfile,
    Writecomment,
    index,
    password_reset_request,
    messages,
    about,
    

)


app_name='AHessTrans2'

urlpatterns = [
    path('',index,name='index'),
    path('base/',base,name='base'),
    path('about/',about,name='about'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logoutUser,name='logout'),
    path('settings/',settingsProfile,name='settings'),
    path('comment/<str:pk>',Writecomment,name='comment'),
    path('messages/<str:pk>/',messages,name='messages'),
    path("password_reset", password_reset_request, name="password_reset")
    
    
]