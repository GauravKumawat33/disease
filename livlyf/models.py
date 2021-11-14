from django.db import models
from django.db.models.fields import DateField
from django_filters.filters import ChoiceFilter

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
    CATEGORY_CITY=(
        ('Alwar','Alwar'),
        ('Mumbai','Mumbai'),
    )
    CATEGORY_Locality=(
        ('Kati Ghati','Kati Ghati'),
        ('Kala Kuan','Kala Kuan'),
        ('Ashoka Circle','Ashoka Circle'),
    )
    CATEGORY_Type=(
        ('General','General'),
        ('Male','Male'),
        ('Ladies','Ladies'),
        ('Children','Children')
    )

    Hospital_ID=models.IntegerField(primary_key = True)
    Hospital_name=models.CharField(max_length=30)
    Av_ICU_Beds=models.IntegerField()
    Av_Normal_Beds=models.IntegerField()
    Av_Oxygen_Cylinder=models.IntegerField()
    City=models.CharField(max_length=30,choices=CATEGORY_CITY)
    Locality=models.CharField(max_length=30,choices=CATEGORY_Locality)
    Type=models.CharField(max_length=30,choices=CATEGORY_Type)
    Phone=models.CharField(max_length=10)

class Patient(models.Model):
    options=(
        ('Active','Active'),
        ('Recovering','Recovering'),
        ('Critical','Critical'),
        ('Dead','Dead'),
    )
    CATEGORY_DISEASE=(
        ('COVID 19','COVID 19'),
        ('Cancer','Cancer'),
    )
    Patient_ID=models.IntegerField(primary_key = True)
    Aadhar_number=models.ForeignKey(
        Personal_Detail, on_delete=models.CASCADE)
    Hospital_ID=models.ForeignKey(
        Hospital, on_delete=models.CASCADE)
    Disease_Name=models.CharField(max_length=30,choices=CATEGORY_DISEASE)
    Patient_Condition=models.CharField(max_length=30,choices=options)
    Registration_Date=models.DateField()

class Vaccine_detail(models.Model):
    Category_Vaccine=(
        ('Covaxin vaccine','Covaxin vaccine'),
        ('Coishield vaccine','Coishield vaccine'),
        ('Johnson & Johnson vaccine','Johnson & Johnson vaccine'),
        ('Sputnik V','Sputnik V'),
    )
    CATEGORY_DISEASE=(
        ('COVID 19','COVID 19'),
        ('Cancer','Cancer'),
    )
    Vaccine_ID=models.IntegerField(primary_key = True)
    Vaccine_name=models.CharField(max_length=30)
    Disease_targetting=models.CharField(max_length=30,choices=CATEGORY_DISEASE)
    Required_Doses=models.IntegerField()
    Interval_btw_Doses_indays=models.IntegerField()

class Vaccination_Center(models.Model):
    CATEGORY_CITY=(
        ('Alwar','Alwar'),
        ('Mumbai','Mumbai'),
    )
    CATEGORY_Locality=(
        ('Kati Ghati','Kati Ghati'),
        ('Kala Kuan','Kala Kuan'),
        ('Ashoka Circle','Ashoka Circle'),
    )
    Center_ID=models.IntegerField(primary_key = True)
    Center_name=models.CharField(max_length=30)
    City=models.CharField(max_length=30,choices=CATEGORY_CITY)
    Locality=models.CharField(max_length=30,choices=CATEGORY_Locality)
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
    Vaccine_chosen=models.ForeignKey(
        Vaccine_detail, on_delete=models.CASCADE)
    Dose_completed=models.IntegerField()
    Last_Dose_taken_date=models.DateField()


    