# Generated by Django 4.0 on 2022-01-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedTaskDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_user', models.CharField(max_length=100)),
                ('task_update_description', models.CharField(max_length=200)),
                ('task_progress_status', models.CharField(max_length=50)),
                ('task_update_file', models.CharField(max_length=200)),
                ('task_updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'assgned_task_description',
            },
        ),
        migrations.CreateModel(
            name='PersonalTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=30)),
                ('task_description', models.CharField(max_length=100)),
                ('task_assigned_at', models.DateTimeField()),
                ('task_accomplish_date', models.DateTimeField()),
                ('task_progress_status', models.CharField(max_length=50)),
                ('task_status', models.BooleanField()),
            ],
            options={
                'db_table': 'personal_task',
            },
        ),
        migrations.CreateModel(
            name='UserNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(max_length=50)),
                ('note_description', models.CharField(max_length=200)),
                ('note_added_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'user_note',
            },
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=30)),
                ('task_description', models.CharField(max_length=100)),
                ('task_assigned_at', models.DateTimeField()),
                ('task_accomplish_date', models.DateTimeField()),
                ('task_assigned_by', models.CharField(max_length=50)),
                ('task_progress_status', models.CharField(max_length=50)),
                ('task_assigned_to', models.CharField(max_length=50)),
                ('task_status', models.BooleanField()),
            ],
            options={
                'db_table': 'user_task',
            },
        ),
    ]
