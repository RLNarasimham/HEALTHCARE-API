from django.db import models

# Create your models here.
class Patient(models.Model):
    Patient_Name=models.CharField(max_length=60)
    Patient_ID=models.CharField(max_length=4)
    Patient_Phone_No=models.IntegerField()
    Patient_Treatment=models.TextField()
    Patient_Doctor=models.CharField(max_length=60)

class Doctor(models.Model):
    Doctor_Name=models.CharField(max_length=60)
    Doctor_Specialization=models.CharField(max_length=50)
    No_Of_Patients=models.IntegerField()
    Doctor_Contact_No=models.IntegerField()