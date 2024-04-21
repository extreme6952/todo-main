# Generated by Django 4.2.6 on 2024-04-21 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasktodo', '0014_task_users_like_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='user_like', to=settings.AUTH_USER_MODEL),
        ),
    ]