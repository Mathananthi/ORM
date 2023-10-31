# Ex02 Django ORM Web Application
## Date: 31.10.2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)

models.py

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

```
## OUTPUT

![Alt text](<Screenshot (7).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
