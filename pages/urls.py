from django.urls import path
from . import views

urlpatterns = [
    path('index' , views.index , name='index'),

    path('student',views.Student , name = 'student'),
    path('doctor',views.Doctor , name = 'doctor'),
    path('teaching_assistant',views.Teaching_assistant , name = 'teaching_assistant'),
    path('subject',views.Subject , name = 'subject'),
    
    path('addstudent',views.createStudent , name = 'addstudent'),
    path('adddoctor',views.createDoctor , name = 'adddoctor'),
    path('addteachingassistant',views.createTeachingAssistant , name = 'addteachingassistant'),
    path('addsubject',views.createSubject , name = 'addsubject'),
    
    path('showstudent',views.showStudent , name = 'showstudent'),
    path('showdoctor',views.showDoctor , name = 'showdoctor'),
    path('showteachingassistant',views.showTeachingAssistant , name = 'showteachingassistant'),
    path('showsubject',views.showSubject , name = 'showsubject'),
    
    path('updatestudent/<int:id>',views.UpdateStudent , name = 'updatestudent'),
    path('updatedoctor/<int:id>',views.UpdateDoctor , name = 'updatedoctor'),
    path('updateteachingassistant/<int:id>',views.UpdateTeachingAssistant , name = 'updateteachingassistant'),
    path('updatesubject/<int:id>',views.UpdateSubject , name = 'updatesubject'),

    path('DeleteStudent/<int:id>',views.DeleteStudent , name = 'DeleteStudent'),
    path('DeleteDoctor/<int:id>',views.DeleteDoctor , name = 'DeleteDoctor'),
    path('DeleteTeachingAssistant/<int:id>',views.DeleteTeachingAssistant , name = 'DeleteTeachingAssistant'),
    path('DeleteSubject/<int:id>',views.DeleteSubject , name = 'DeleteSubject'),

]