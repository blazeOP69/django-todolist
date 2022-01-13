from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from datetime import date
import calendar
from calendar import HTMLCalendar
from ToDoList.forms import UserTaskForm
from ToDoList.forms import AssignedTaskDescForm
from ToDoList.forms import UserNoteForm
from ToDoList.forms import PersonalTaskForm
from ToDoList.models import UserNote

# Create your views here.
def index(request, year=date.today().year, month=date.today().month):
    title = "This is a title"
    year = int(year)
    month = int(month)

    if year < 1999 or year > 2099:
        year = date.today().year
    
    month_name = calendar.month_name[month]

    cal = HTMLCalendar().formatmonth(year, month)

    title = "Current Month: " + month_name
    data = {'title':title, 'cal': cal , 'month': month}
    return render(request, "base.html", data)
    return render(request,"base.html")

def create(request):
    return HttpResponse("this method stores data")

# For Models

def user_task(request):
    userTask = UserTaskForm
    return render(request, "formodel.html", {'form':userTask})

def assigned_task_desc(request):
    assign = AssignedTaskDescForm
    return render(request, 'formodel.html', {'form':assign })

def assigned_task_desc_data(request):
    task_user=request.POST['task_user']
    task_update_description=request.POST['task_update_description']
    task_progress_status=request.POST['task_progress_status']
    task_update_file=request.POST['task_update_file']
    task_updated_at=request.POST['task_updated_at']
    data  = {

        'task_user' : task_user,
        'task_update_description' : task_update_description,
        'task_progress_status' : task_progress_status,
        'task_update_file' : task_update_file,
        'task_updated_at' : task_updated_at,
    }        
    return render(request, 'task_desc.html' , {'data':data} )
        
    

def personal_task(request):
    personal = PersonalTaskForm
    return render(request, 'formodel.html', {'form': personal})    

def user_note(request):
    note = UserNoteForm
    return render(request, 'user_note.html', {'form': note})

def user_note_add(request):
    template = 'user_note.html'

    # filtering request method
    if request.method == "POST":
        # filtering request data
        title = request.POST.get('note_title')
        description = request.POST.get('note_description')
        added_at = request.POST.get('note_added_at')
        
        # creating object of model
        un = UserNote(note_title=title, note_description=description, note_added_at=added_at)
        un.save()
        # creating object of form
        note = UserNoteForm
        
        # success message
        msg = "Success"

        # sending response to request
        return render(request, template, {'form': note, 'msg': msg, 'data': un})
    else:
        note = UserNoteForm
        msg = "Fail"
        return render(request, template, {'form': note, 'msg': msg})
   

    