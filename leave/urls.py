from django.urls import path
from . import views

urlpatterns = (   
    path('annual/', views.annual), 
    path('annuallist/', views.annuallist),  
    path('approvallist/', views.approvallist),    
)
 