from django.db import models
from django.urls import reverse

# Create your models here.

class Gear(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} | {self.model}"
    
    class Meta:
        verbose_name_plural = "gear"

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'gear_id': self.id})

    def getName(self):
        return f"{self.make} | {self.model}"


# Options for category
CATEGORIES = (
    ('G', 'Guitar'),
    ('K', 'Keyboard'),
    ('M', 'Microphone'),
    ('P', 'Pro Audio'),
    ('S', 'Software'),
    ('O', 'Other')
)

class Category(models.Model):
    gear = models.ForeignKey(
        Gear,
        on_delete=models.CASCADE
    )
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES
    )
    def __str__(self):
        return f"{self.get_category_display()}"

class Retailer(models.Model):
    name = models.CharField(max_length=250)
    gear = models.ManyToManyField(Gear)

    def get_absolute_url(self):
        return reverse('retailer_detail', kwargs={'pk': self.id})
    
    

