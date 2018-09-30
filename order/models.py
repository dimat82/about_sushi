from django.db import models
from menu.models import *

# Create your models here.
class OrderSushi(models.Model):
    name = models.CharField('имя',max_length=50)
    phone = models.CharField(u'телефон', max_length=100)
    food = models.ForeignKey(Sushi,verbose_name='еда',on_delete='')
    date = models.DateTimeField('Дата заказа',auto_now_add=True,blank=True,null=True)

class OrderSets(models.Model):
    name = models.CharField('имя',max_length=50)
    phone = models.CharField(u'телефон', max_length=100)
    food = models.ForeignKey(Sets,verbose_name='еда',on_delete='')
    date = models.DateTimeField('Дата заказа', auto_now_add=True,blank=True,null=True)

class OrderSoup(models.Model):
    name = models.CharField('имя',max_length=50)
    phone = models.CharField(u'телефон', max_length=100)
    food = models.ForeignKey(Soups,verbose_name='еда',on_delete='')
    date = models.DateTimeField('Дата заказа', auto_now_add=True,blank=True,null=True)

class OrderRolls(models.Model):
    name = models.CharField('имя',max_length=50)
    phone = models.CharField(u'телефон', max_length=100)
    food = models.ForeignKey(Rolls,verbose_name='еда',on_delete='')
    date = models.DateTimeField('Дата заказа', auto_now_add=True,blank=True,null=True)
