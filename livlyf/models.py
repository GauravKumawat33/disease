from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Personal_Detail(models.Model):
    Aadhar_number=models.CharField(primary_key = True,max_length=12)
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    Birth_date=models.DateField()
    Sex=models.CharField(max_length=1)
    City=models.CharField(max_length=30)
    Locality=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)
    Email_ID=models.EmailField(max_length = 254)

class Hospital(models.Model):
    Hospital_ID=models.IntegerField(primary_key = True)
    Hospital_name=models.CharField(max_length=30)
    Av_ICU_Beds=models.IntegerField()
    Av_Normal_Beds=models.IntegerField()
    Av_Oxygen_Cylinder=models.IntegerField()
    City=models.CharField(max_length=30)
    Locality=models.CharField(max_length=30)
    Type=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)


class Patient(models.Model):
    Patient_ID=models.IntegerField(primary_key = True)
    Aadhar_number=models.ForeignKey(
        Personal_Detail, on_delete=models.CASCADE)
    Hospital_ID=models.ForeignKey(
        Hospital, on_delete=models.CASCADE)
    Disease_Name=models.CharField(max_length=30)
    Patient_Condition=models.CharField(max_length=30)
    Registration_Date=models.DateField()


class Vaccine_detail(models.Model):
    Vaccine_ID=models.IntegerField(primary_key = True)
    Vaccine_name=models.CharField(max_length=30)
    Disease_targetting=models.CharField(max_length=30)
    Required_Doses=models.IntegerField()
    Interval_btw_Doses_indays=models.IntegerField()

class Vaccination_Center(models.Model):
    Center_ID=models.IntegerField(primary_key = True)
    Center_name=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    Locality=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)

class Center_Vaccine_reln(models.Model):
    Relation_ID=models.IntegerField(primary_key = True)
    Center_ID=models.ForeignKey(
        Vaccination_Center, on_delete=models.CASCADE)
    Vaccine_ID=models.ForeignKey(
        Vaccine_detail, on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Which_Dose=models.IntegerField()

class Vaccine_Consumer(models.Model):
    Constumer_ID=models.IntegerField(primary_key = True)
    Aadhar_number=models.ForeignKey(
        Personal_Detail, on_delete=models.CASCADE)
    Vaccine_chosen=models.CharField(max_length=30)
    Dose_completed=models.IntegerField()
    Last_Dose_taken_date=models.DateField()

class Appointment(models.Model):
    Appointment_Num=models.IntegerField(primary_key = True)
    Center_ID=models.ForeignKey(
        Vaccination_Center, on_delete=models.CASCADE)
    Vaccine_ID=models.ForeignKey(
        Vaccine_detail, on_delete=models.CASCADE)
    Aadhar_number=models.ForeignKey(
        Personal_Detail, on_delete=models.CASCADE)
    Which_Dose=models.IntegerField()
    Last_Dose_taken_date=models.DateField()
    Date=models.DateField()
    Slot_Time=models.DateField()



    