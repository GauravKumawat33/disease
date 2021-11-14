# Generated by Django 2.2.24 on 2021-11-14 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livlyf', '0006_auto_20211114_2140'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vaccine_Consumer',
        ),
        migrations.AddField(
            model_name='personal_detail',
            name='Dose_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personal_detail',
            name='Last_Dose_taken_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='personal_detail',
            name='Vaccine_chosen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='livlyf.Vaccine_detail'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Locality',
            field=models.CharField(choices=[('Kati Ghati', 'Kati Ghati'), ('Kala Kuan', 'Kala Kuan'), ('Ashoka Circle', 'Ashoka Circle'), ('Panvel', 'Panvel')], max_length=30),
        ),
        migrations.AlterField(
            model_name='personal_detail',
            name='Aadhar_number',
            field=models.CharField(default=None, max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vaccination_center',
            name='Locality',
            field=models.CharField(choices=[('Kati Ghati', 'Kati Ghati'), ('Kala Kuan', 'Kala Kuan'), ('Ashoka Circle', 'Ashoka Circle'), ('Panvel', 'Panvel')], max_length=30),
        ),
    ]
