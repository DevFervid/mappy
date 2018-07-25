from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='must/items/%Y/%m/%d', blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
