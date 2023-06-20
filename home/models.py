from django.db import models

# Create your models here.
class profile(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    uname = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    img=models.FileField(default="")
    address = models.CharField(max_length=20)
    work = models.CharField(max_length=10)
    
    def __str__(self):
        return self.uname

    