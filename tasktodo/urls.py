from django.urls import include, path



from . import  views


urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    
    path('',views.task_list,name='index'),

    path('<int:task_id>/<slug:slug>/', views.task_detail,name='task_detail'),

    path('update/<int:task_id>/<slug:slug>',views.update_task,name='update'),

    path('delete/<int:task_id>/<slug:slug>/',views.delete_task,name='delete_suka'),

    path('comment/<int:task_id>/<slug:slug>',views.task_comment, name='commetd'),

    path('<int:id>/<slug:slug>/like/',views.like_post,name='task_like'),

    path('registration/',views.user_registration,name='user_registration')
    
    
]
