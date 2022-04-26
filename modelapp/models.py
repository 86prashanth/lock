from ctypes.util import find_msvcrt
from django.db import models

class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.image