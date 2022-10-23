from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media')

    def getImage(self):
        return self.image.url
