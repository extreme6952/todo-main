from django.shortcuts import get_object_or_404, render

from .forms import *

from .models import *

from django.shortcuts import redirect

from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt




def task_list(request):

    task = Task.objects.all()

    if request.method=='POST':

        form = NewTaskForm(data=request.POST,
                           files=request.FILES)
        
        if form.is_valid():

            cd = form.cleaned_data

            new_task = form.save(commit=False)

            new_task.user = request.user

            new_task.save()

            messages.success(request,
                             'Задача успешно добавлена')

            return redirect(new_task.get_absolute_url())
        
        else:

            messages.error(request,
                           'При заполнении данных произошла ошибка')
            

    else:

        form = NewTaskForm(files=request.FILES,
                           data=request.GET)
        

    return render(request,
                  'task/task_list.html',
                  {'task':task,
                   'form':form})


def task_detail(request,task_id,slug):

    task = get_object_or_404(Task,
                             id=task_id,
                             slug=slug)
    
    form = CommentForm()

    comments = task.comments.filter(active=True)

    
    

    
    return render(request,
                  'task/task_detail.html',
                  {'task_detail':task,
                   'form':form,
                   'comments':comments})

def update_task(request,slug,task_id):

    task = get_object_or_404(Task,
                             slug=slug,
                             id=task_id)
    
    task.is_complete = not task.is_complete

    task.save()

    return redirect('index')


def delete_task(request,id,slug):

    task = get_object_or_404(Task,slug=slug,
                             id=id)
    task.delete()



def delete_task(request,task_id,slug):

    task = get_object_or_404(Task,slug=slug,
                             id=task_id)
    task.delete()

    

    return redirect('index')

@require_POST
def task_comment(request,task_id,slug):

    

    if request.method=='POST':

        task = get_object_or_404(Task,
                             id=task_id,
                             slug=slug)

        form = CommentForm(data=request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.user = request.user

            comment.task = task

            comment.save()

            messages.success(request,
                             'Ваш комментарий был успешно добавлен')

            return redirect(task.get_absolute_url())
        
        else:

            messages.error(request,
                           'При заполнении формы произошла ошибка')
            
    else:

        form = CommentForm()

    return render(request,
                  'task/includes/comment_form.html',
                  {'form':form,
                   'comment':comment,
                   'task':task})