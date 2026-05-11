from django.shortcuts import render
from healthcare_api_app.models import Doctor,Patient
from rest_framework import viewsets
from healthcare_api_app.serializers import PatientSerializer
import requests
from healthcare_api_app.serializers import DoctorSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@login_required
def show_patients_view(request):
    url=request.build_absolute_uri('/api/patients/')
    response=requests.get(url,cookies=request.COOKIES)
    patient_data=response.json() if response.ok else []
    return render(request,'healthcare_api_app/patients_details.html',{'p_data':patient_data})

@login_required
def show_doctors_view(request):
    url=request.build_absolute_uri('/api/doctors/')
    response=requests.get(url,cookies=request.COOKIES)
    doctor_data=response.json() if response.ok else []
    return render(request,'healthcare_api_app/doctors_details.html',{'d_data':doctor_data})

def show_home_view(request):
    return render(request,'healthcare_api_app/homepage.html')

class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]