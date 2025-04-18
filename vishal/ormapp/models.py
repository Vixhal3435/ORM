from django.db import models
from django.contrib import admin
class Movies(models.Model):
    person_id= models.CharField(max_length=20, help_text="User ID")
    name= models.CharField(max_length=100)
    person_email= models.EmailField()
    seats= models.IntegerField()
    Movie_Name=models.CharField(max_length=20)
    Show_Date=models.DateTimeField()
    Phone_Number=models.CharField(max_length=10, help_text="Phone number")
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'name', 'person_email', 'seats', 'Movie_Name','Show_Date','Phone_Number')