from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=200)
	date_set = models.DateTimeField('date set')
	summary = models.CharField(max_length=200)
