from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Book(models.Model):

	name=models.CharField(max_length=100)
	author=models.OneToOneField(User,related_name='users')
	def __str__(self):
		return self.name
class MultipleBooks(models.Model):
	name=models.CharField(max_length=100)
	author=models.ForeignKey(User)
	def  __str__(self):
		return self.name

class MultiAuthoeBooks(models.Model):
	name=models.CharField(max_length=100)
	authoe=models.ManyToManyField(User)
	def  __str__(self):
		return self.name

class User_extra(models.Model):
	user=models.OneToOneField(User)
	age=models.PositiveIntegerField()
	gender=models.CharField(max_length=6,choices=(("Male",'male'),("Female",'female')))
	address=models.TextField()
	def  __str__(self):
		return self.user.username