from django.urls import path
from . import views

urlpatterns = (          
    path('login/', views.aflogin),
    path('logout/', views.logout),
    path('resetpwd/', views.resetpwd),    
)
 
    
    
