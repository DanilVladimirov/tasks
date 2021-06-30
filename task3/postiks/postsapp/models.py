import os
import random

from django.contrib.auth.models import User
from django.db import models
import datetime


def file_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return f'{basefilename}_{randomstr}{file_extension}'


class Publication(models.Model):
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
    
    title = models.CharField(max_length=200,
                             default='no-title')
    text = models.TextField(default='no-text')
    img = models.ImageField(upload_to=file_path)
    date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='publication',
                             null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    text = models.TextField(default='no-text')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='u_comments',
                               null=True)
    publication = models.ForeignKey(Publication,
                                    on_delete=models.CASCADE,
                                    related_name='comment')

    def __str__(self):
        return f'{self.text[:10]}...'
