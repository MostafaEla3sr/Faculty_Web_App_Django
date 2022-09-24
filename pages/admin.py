from django.contrib import admin
from .models import student ,doctor, TeachingAssistant , subject  

# Register your models here.

admin.site.register(student)
admin.site.register(doctor)
admin.site.register(TeachingAssistant)
admin.site.register(subject)

