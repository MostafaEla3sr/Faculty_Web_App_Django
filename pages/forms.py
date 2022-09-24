from dataclasses import fields
from email.policy import default
from importlib import import_module
from django import forms

from pages.models import  student , doctor ,TeachingAssistant, subject

class StudentForm (forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
        

class DoctorForm (forms.ModelForm):
    class Meta:
        model=doctor
        fields='__all__'


class TeachingAssistantForm (forms.ModelForm):
    class Meta:
        model=TeachingAssistant
        fields='__all__'


class SubjectForm (forms.ModelForm):
    class Meta:
        model=subject
        fields='__all__'
