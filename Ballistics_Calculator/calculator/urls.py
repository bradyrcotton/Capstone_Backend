from django.urls import path
from . import views

urlpatterns = [
    path('shooter/', views.ShooterList.as_view()),
    path('rifle/', views.RifleList.as_view()),
    path('rifle/<int:pk>/', views.RifleBuild.as_view()),
    path('dope/', views.DopeList.as_view())
]