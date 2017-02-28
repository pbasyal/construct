from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	location = models.CharField(max_length=30)
	tender_contract = models.CharField(max_length=50)
	start_date = models.DateTimeField(auto_now_add=True)
	completion_date = models.DateField()
	budget = models.CharField(max_length=150)
	media = models.ImageField(upload_to = 'Photos', blank = True)
	documents = models.FileField(upload_to = 'Documents', blank = True)
	status = models.CharField(max_length=15)

	def __str__(self):
		return self.name



class Report(models.Model):
	project_name = models.ForeignKey(Project, on_delete = models.CASCADE)
	complaint = models.TextField()
	image = models.ImageField(upload_to = 'Report_Images', blank = True)
	publish = models.BooleanField(default = False)

	def __str__(self):
		report = 'Report Description{}'.format(self.complaint)
		return report[:20]


