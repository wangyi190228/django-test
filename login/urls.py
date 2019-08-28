from django.urls import path
from . import views

urlpatterns = (          
    path('login/', views.aflogin),
    path('logout/', views.aflogout),
    path('home/', views.home),
    path('resetpwd/', views.resetpwd),    
)
 
    
    
