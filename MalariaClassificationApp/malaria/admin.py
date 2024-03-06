from django.contrib import admin
from .models import PatientRecords


# Register your models here.
class PatientRecordsAdmin(admin.ModelAdmin):
    list_display = ["patient", "pred_class", "score", "image", "desc"]


admin.site.register(PatientRecords, PatientRecordsAdmin)
