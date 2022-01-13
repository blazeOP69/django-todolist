from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index, name="index"),
    
    path('create/', views.create, name="create"),
    
    path('create-task/', views.user_task, name="task.create"),

    path('assign-task/', views.assigned_task_desc, name="task.assign"),
    path('assign-task/task-assign/', views.assigned_task_desc_data, name="task.assign.data"),

    path('personal-task/', views.personal_task, name="task.personal"),

    path('user-note/', views.user_note, name="user.note"),
    path('user-note-add/', views.user_note_add, name="user.note.add"),

]