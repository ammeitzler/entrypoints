from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Anticipating(models.Model):
	question = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return '%d: %s' % (self.question)

class Check(models.Model):
	question = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return '%d: %s' % (self.question)

class CheckSentiment(models.Model):
	question = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return '%d: %s' % (self.question)