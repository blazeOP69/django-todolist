# Generated by Django 4.0 on 2022-01-09 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssignedTaskDescription',
            new_name='AssignedTaskDesc',
        ),
        migrations.AlterModelTable(
            name='assignedtaskdesc',
            table='assigned_task_description',
        ),
    ]
