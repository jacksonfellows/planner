from django.db import models
import datetime

class Event(models.Model):
	event = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	start = models.DateTimeField()
	end = models.DateTimeField()
	day = models.CharField(max_length=200)

	def __str__(self):
		return self.day + ": " + self.event + " " + self.name