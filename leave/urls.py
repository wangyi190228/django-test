from django.urls import path
from . import views

urlpatterns = (   
    path('annual/', views.annual), 
    path('overview/', views.overview), 
    path('annuallist/', views.annuallist),  
    path('annualdays/', views.annualdays),  
    path('approvallist/', views.approvallist),   
    path('staffleave/', views.staffleave),   
    path('detail/', views.detail),   
)
 