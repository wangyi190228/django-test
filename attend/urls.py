from django.urls import path
from . import views

urlpatterns = (   
    path('attend/', views.attend),
)
 