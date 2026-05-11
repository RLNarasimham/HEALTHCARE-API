"""
URL configuration for healthcare_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from healthcare_api_app import views
from rest_framework.routers import DefaultRouter


router1=DefaultRouter()
router2=DefaultRouter()

router1.register('patients',views.PatientViewSet,basename="patients")
router2.register('doctors',views.DoctorViewSet,basename="doctors")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.show_home_view),
    path('patients/',views.show_patients_view),
    path('doctors/',views.show_doctors_view),
    path('api/',include(router1.urls)),
    path('api/',include(router2.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
