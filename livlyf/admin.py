from django.contrib import admin

from .models import Center_Vaccine_reln, Hospital, Patient, Personal_Detail, Vaccination_Center, Vaccine_detail

# Register your models here.
admin.site.register(Personal_Detail)
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Vaccination_Center)
admin.site.register(Vaccine_detail)
admin.site.register(Center_Vaccine_reln)
# admin.site.register(Vaccine_Consumer)
# admin.site.register(Appointment)



