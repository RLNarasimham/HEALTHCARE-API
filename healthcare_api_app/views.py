from django.shortcuts import render
from healthcare_api_app.models import Doctor,Patient
from rest_framework import viewsets
from healthcare_api_app.serializers import PatientSerializer
import requests
from healthcare_api_app.serializers import DoctorSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.test import RequestFactory

# Create your views here.
@login_required
def show_patients_view(request):
    factory = RequestFactory()
    internal_request = factory.get('/api/patients/')
    internal_request.user = request.user

    view = PatientViewSet.as_view({'get': 'list'})
    response = view(internal_request)

    if response.status_code == 200:
        if isinstance(response.data, dict) and 'results' in response.data:
            patient_data = response.data['results']
        else:
            patient_data = response.data
    else:
        patient_data = []

    return render(request, 'healthcare_api_app/patients_details.html', {'p_data': patient_data})


@login_required
def show_doctors_view(request):
    factory=RequestFactory()
    internal_request=factory.get('/api/doctors/')

    internal_request.user=request.user

    view=DoctorViewSet.as_view({'get':'list'})
    response=view(internal_request)

    doctor_data=response.data if response.status_code == 200 else []

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