# Generated by Django 3.2.25 on 2024-03-05 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_dicomdata_radiologist_dicomdata_radiologist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dicomdata',
            name='total_cases',
        ),
    ]
