from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomerList.as_view()),
    path('users/<int:pk>/', views.CustomerDetail.as_view()),
]