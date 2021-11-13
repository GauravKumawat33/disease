from django.db.models import fields
import django_filters
from django_filters import DateFilter, CharFilter
from .models import Hospital,Vaccination_Center,Vaccine_detail

class OrderFilter(django_filters.FilterSet):
    Hosp_name=CharFilter(field_name='Hospital_name',lookup_expr='icontains')

    class Meta:
        model=Hospital
        fields=['City','Locality','Type',]

class OrderFilterC(django_filters.FilterSet):
    Center_name=CharFilter(field_name='Center_name',lookup_expr='icontains')

    class Meta:
        model=Vaccination_Center
        fields=['City','Locality',]

class OrderFilterV(django_filters.FilterSet):
    Vacc_name=CharFilter(field_name='Vaccine_name',lookup_expr='icontains')

    class Meta:
        model=Vaccine_detail
        fields=['Required_Doses','Disease_targetting',]
