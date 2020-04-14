from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    CATEGORY_TYPE = [
        (0, 'Sport'),
        (1, 'Beauty')
    ]
    type = models.IntegerField(choices=CATEGORY_TYPE, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('type',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Item(models.Model):
    """Item """
    name = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(decimal_places=3, max_digits=100)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class RegistrationSportBeauty(models.Model):

    name_place = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    number_people = models.IntegerField()
    user = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Order from " + str(self.user)

    class Meta:
        ordering = ('name_place',)