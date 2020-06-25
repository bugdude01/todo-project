from django.db import models

class User(models.Model):
	username = models.CharField(max_length=200)
	profile_pic = models.ImageField(upload_to='images/')