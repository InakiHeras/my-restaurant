from django.db import models

# Create your models here.
class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    dish = models.ForeignKey(Dish, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.dish.name