from django.db import models
from .Date import Date
from .personalinfo import PersonalInfo
from .Location import Location


class PatientDetails(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    PatientId = models.CharField(max_length=50)
    PatientName = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)
    HeartRate = models.CharField(max_length=30, null=True, blank=True)
    TestDate = models.CharField(max_length=20)
    ReportDate = models.CharField(max_length=20)
    PRInterval = models.CharField(max_length=30, null=True, blank=True)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='ecg_graphs/', null=True, blank=True)
    reportimage = models.FileField(upload_to='ecg_graphs/', null=True, blank=True)
    cardiologist = models.ForeignKey(PersonalInfo, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    isDone = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    NonReportable = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.PatientName)