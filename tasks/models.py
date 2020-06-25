from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	title = models.CharField(max_length=200)
	date_set = models.DateTimeField('date set')
	description = models.TextField(blank=True)	
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def summary(self):
		return self.description[:50]

	def pub_date_pretty(self):
		return self.date_set.strftime('%e %b %Y')
		