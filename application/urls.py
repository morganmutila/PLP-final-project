from django.urls import path
from .import views

urlpatterns = [
    path('', views.application, name='apply'),

    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name="register"),
    path('logout', views.logoutUser, name="logout"),
]