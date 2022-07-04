from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Season(models.Model):
    season_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.season_name  


class Type(models.Model):
    season_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.season_name


class Item(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Picture(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    image = models.ImageField(default='defualt.png', upload_to ='item_pics')

    def __str__(self):
        return f'{self.item.name} Picture'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) 



#class Cart(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(default=datetime.now)      


#class CartItem(models.Model):
#    product = models.ForeignKey(Item, on_delete=models.CASCADE)
#    quantity = models.IntegerField(default=1)
#    price_ht = models.FloatField(blank=True)
#    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


#    def __str__(self):
#        return  self.client + " - " + self.product          