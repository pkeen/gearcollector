from django.db import models

# Create your models here.

class Gear(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} | {self.model}"
    
    class Meta:
        verbose_name_plural = "gear"
