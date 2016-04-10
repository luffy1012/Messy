from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class Student (models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 50)
    entry_num = models.CharField(max_length =11)
    pic = models.ImageField(upload_to="static/img/profile_pics",blank=True)
    def __str__(self):
        return self.user.username

def create_student_user_callback(sender,instance,**kwargs):
    student,new = Student.objects.get_or_create(user=instance)
post_save.connect(create_student_user_callback,User)
