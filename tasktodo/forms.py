from django import forms



from .models import *



class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ['body']



class NewTaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = ['title','text','image']