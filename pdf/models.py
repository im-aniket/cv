from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    member = models.IntegerField(max_length=20000, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.TextField(max_length=1000)
    skill = models.TextField(max_length=1000)
    

    def __str__(self):
        return str(self.name)
    