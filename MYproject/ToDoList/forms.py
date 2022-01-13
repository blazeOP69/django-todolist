from django import forms
from django.db.models import fields
from ToDoList.models import UserTask
from ToDoList.models import AssignedTaskDesc
from ToDoList.models import PersonalTask
from ToDoList.models import UserNote

class UserTaskForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = "__all__"

class AssignedTaskDescForm(forms.ModelForm):
    class Meta:
        model = AssignedTaskDesc
        fields = "__all__"

class PersonalTaskForm(forms.ModelForm):
    class Meta:
        model = PersonalTask
        fields = "__all__"

class UserNoteForm(forms.ModelForm):
    class Meta:
        model = UserNote
        fields = "__all__"