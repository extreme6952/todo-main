# Generated by Django 4.2.6 on 2024-04-21 01:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasktodo', '0012_alter_like_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='like',
            new_name='task',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'task')},
        ),
    ]