from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    PhoneNumber = models.IntegerField(null=True)
    Course = models.CharField(max_length=20)


    def __str__(self):
        return (self.Name)