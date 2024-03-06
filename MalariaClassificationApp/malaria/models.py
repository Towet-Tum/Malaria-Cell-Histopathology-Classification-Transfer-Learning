from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PatientRecords(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Patient")
    pred_class = models.CharField(max_length=100)
    score = models.FloatField()
    desc = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.username
