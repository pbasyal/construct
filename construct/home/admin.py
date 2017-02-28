from django.contrib import admin

# Register your models here.
from .models import Project, Report
admin.site.register(Project)
admin.site.register(Report)