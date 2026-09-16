from django.contrib import admin
from .models import User, Email, Patient, Report

# Register your models here.

admin.site.register(User),
admin.site.register(Email),
admin.site.register(Patient),
admin.site.register(Report),