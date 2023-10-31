from django.db import models
from django.contrib import admin
class Football(models.Model):
    pid=models.CharField(max_length=20,help_text="Player ID")
    name=models.CharField(max_length=100)
    jersey_no=models.CharField(max_length=5,default=00000)
    age=models.IntegerField()
    salary=models.IntegerField()
class FootballAdmin(admin.ModelAdmin):
    list_display=('pid','name','jersey_no','age','salary')
