from email.policy import default
from django.db import models
from auth_user.models import CustomUser as User

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media')
    ratings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def getImage(self):
        return self.image.url


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.JSONField(default=dict)
