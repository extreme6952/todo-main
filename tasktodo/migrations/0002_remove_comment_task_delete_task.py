# Generated by Django 4.2.6 on 2024-04-14 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasktodo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='task',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]