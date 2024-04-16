from typing import Iterable
from django.db import models

from django.utils import timezone

from django.utils.text import slugify

from unidecode import unidecode

from django.urls import reverse

from django.contrib.auth.models import User


from imagekit.models import ProcessedImageField

from imagekit.processors import ResizeToFill





class Task(models.Model):

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250,
                            blank=True)

    text = models.TextField(blank=True)

    image = ProcessedImageField(upload_to='task_image/%Y/%m/%d',
                                processors=[ResizeToFill(820,500)],
                                format='JPEG',
                                options={'quality': 80},
                                blank=True,
                                null=True)

    is_complete = models.BooleanField(default=False)

    publish = models.DateTimeField(default=timezone.now,null=True)

    created = models.DateTimeField(auto_now_add=True,null=True)

    updated = models.DateTimeField(auto_now=True,null=True)



    class Meta:

        ordering = ['-publish']

        indexes = [
            models.Index(fields=['-publish'])
        ]

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(unidecode(self.title))


        super().save(*args, **kwargs )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("task_detail", args=[self.id,
                                            self.slug])
    






class Comment(models.Model):

    task = models.ForeignKey(Task,
                             on_delete=models.CASCADE,
                             related_name='comments')
    
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True)

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:

        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created'])
        ]

    
    def __str__(self):

        return f"Comment {self.user} by {self.task}"
    

class Profile(models.Model):

    user = models.OneToOneField(User,
                                related_name='profiles',
                                on_delete=models.CASCADE)
    
    photo = models.ImageField(upload_to='profile/%d/%m/%y',blank=True)


    def __str__(self):

        return f"Profile the {self.user.username}"
    
