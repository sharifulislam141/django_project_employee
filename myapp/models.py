from django.db import models

# Create your models here.
class Employess(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField()
    address =models.TextField()
    phone = models.IntegerField()
    def __str__(self):
        return self.name