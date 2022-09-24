from django.shortcuts import redirect
from email import message
from multiprocessing import context
from tokenize import Special
from unicodedata import name
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from .models import student 
from .forms import  StudentForm  , DoctorForm , SubjectForm , TeachingAssistantForm 
from django.shortcuts import render
from pages.models import student ,doctor , TeachingAssistant , subject 

def index(request):
    return render(request , "pages/index.html")

def Student(request):
    return render(request , "pages/student.html")

def Doctor(request):
    return render(request , "pages/doctor.html")

def Teaching_assistant(request):
    return render(request , "pages/teachingassistant.html")

def Subject(request):
    return render(request , "pages/subject.html")

def createStudent(request):
    if request.method =="POST":
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request , "pages/addstudent.html" , {"StudentForm" : StudentForm})

def showStudent(request):
    return render(request , "pages/showstudent.html" , {"showstudent" :student.objects.all().order_by("id") } )

def DeleteStudent(request,id):
    delstudent = student.objects.get(id=id)
    delstudent.delete()
    return redirect('/pages/showstudent')

def UpdateStudent(request , id):
    student_id = student.objects.get(id= id)
    if request.method == 'POST':
        student_save = StudentForm(request.POST , request.FILES , instance= student_id)
        if student_save.is_valid():
            student_save.save()
            return redirect('/pages/showstudent')
    else:
        student_save = StudentForm(instance= student_id)
    context ={
        'edit_student' : student_save
    }
    return render(request , 'pages/updatestudent.html' , context)


def createDoctor(request):
    if request.method =="POST":
        data = DoctorForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request , "pages/adddoctor.html" , {"DoctorForm" : DoctorForm})

def showDoctor(request):
    return render(request , "pages/showdoctor.html" , {"showdoctor" :doctor.objects.all().order_by("id") } )

def DeleteDoctor(request,id):
    deldoctor = doctor.objects.get(id=id)
    deldoctor.delete()
    return redirect('/pages/showdoctor')

def UpdateDoctor(request , id):
    doctor_id = doctor.objects.get(id= id)
    if request.method == 'POST':
        doctor_save = DoctorForm(request.POST , request.FILES , instance= doctor_id)
        if doctor_save.is_valid():
            doctor_save.save()
            return redirect('/pages/showdoctor')
    else:
        doctor_save = DoctorForm(instance= doctor_id)
    context ={
        'edit_doctor' : doctor_save
    }
    return render(request , 'pages/updatedoctor.html' , context)

def createTeachingAssistant(request):
    if request.method =="POST":
        data = TeachingAssistantForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request , "pages/addteachingassistant.html" , {"TeachingAssistantForm" : TeachingAssistantForm})

def showTeachingAssistant(request):
    return render(request , "pages/showteachingassistant.html" , {"showteachingassistant" :TeachingAssistant.objects.all().order_by("id") } )

def DeleteTeachingAssistant(request,id):
    delteachingassistant = TeachingAssistant.objects.get(id=id)
    delteachingassistant.delete()
    return redirect('/pages/showteachingassistant')

def UpdateTeachingAssistant(request , id):
    teachingassistant_id = TeachingAssistant.objects.get(id= id)
    if request.method == 'POST':
        teachingassistant_save = TeachingAssistantForm(request.POST , request.FILES , instance= teachingassistant_id)
        if teachingassistant_save.is_valid():
            teachingassistant_save.save()
            return redirect('/pages/showteachingassistant')
    else:
        teachingassistant_save = TeachingAssistantForm(instance= teachingassistant_id)
    context ={
        'edit_teachingassistant' : teachingassistant_save
    }
    return render(request , 'pages/updateteachingassistant.html' , context)

def createSubject(request):
    if request.method =="POST":
        data = SubjectForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request , "pages/addsubject.html" , {"SubjectForm" : SubjectForm})

def showSubject(request):
    return render(request , "pages/showsubject.html" , {"showsubject" :subject.objects.all().order_by("id") } )

def DeleteSubject(request,id):
    delsubject = subject.objects.get(id=id)
    delsubject.delete()
    return redirect('/pages/showsubject')

def UpdateSubject(request , id):
    subject_id = subject.objects.get(id= id)
    if request.method == 'POST':
        subject_save = SubjectForm(request.POST , request.FILES , instance= subject_id)
        if subject_save.is_valid():
            subject_save.save()
            return redirect('/pages/showsubject')
    else:
        subject_save = SubjectForm(instance= subject_id)
    context ={
        'edit_subject' : subject_save
    }
    return render(request , 'pages/updatesubject.html' , context)
