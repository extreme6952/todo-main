# Generated by Django 4.2.6 on 2024-04-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktodo', '0002_remove_comment_task_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('text', models.TextField(blank=True)),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
