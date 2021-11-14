# Generated by Django 2.2.24 on 2021-11-14 18:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livlyf', '0008_auto_20211114_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_detail',
            name='Dose_completed',
        ),
        migrations.RemoveField(
            model_name='personal_detail',
            name='Last_Dose_taken_date',
        ),
        migrations.RemoveField(
            model_name='personal_detail',
            name='Vaccine_chosen',
        ),
        migrations.CreateModel(
            name='Vaccine_Consumer',
            fields=[
                ('Constumer_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Dose_completed', models.IntegerField(default=0)),
                ('Last_Dose_taken_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('Aadhar_number', models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to='livlyf.Personal_Detail')),
                ('Vaccine_chosen', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='livlyf.Vaccine_detail')),
            ],
        ),
    ]
