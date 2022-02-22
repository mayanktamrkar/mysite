from django.db import models
class Contact(models.Model):
    name =models.TextField()
    email=models.TextField()

    def __str__(self):
        return self.name 

# Create your models here.
