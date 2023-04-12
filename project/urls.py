from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('programs', views.programs, name="programs"),
    path('programs/<str:slug>', views.program_detail, name="program_detail"),

    # All paths to the application app
    path('application/', include('application.urls')),
]
