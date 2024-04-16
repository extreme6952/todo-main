from django.contrib import admin

# Register your models here.
from .models import *



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['title','slug','is_complete','created','updated']

    list_filter = ['created','updated']

    search_fields = ['title','text']

    prepopulated_fields = {'slug':('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['task','user','created','active']

    list_filter = ['created','updated']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user']