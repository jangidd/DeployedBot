# Generated by Django 5.1 on 2024-08-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_ecgpatientdetails_xraypatientdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='NonReportable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='total_cases',
            name='total_nonreported_ecg',
            field=models.IntegerField(default=0),
        ),
    ]