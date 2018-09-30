from django.db import models

# Create your models here.
class Rolls(models.Model):
    name = models.CharField('название ролла', max_length=50)
    description = models.TextField('описание')
    price = models.IntegerField('цена')
    photo = models.ImageField('фото',upload_to='rolls/photo',default='',blank=True)

    class Meta:
        verbose_name = 'ролл'
        verbose_name_plural = 'rolls'

    def __str__(self):
        return self.name

class Sets(models.Model):
    name = models.CharField('название сета', max_length=50)
    description = models.TextField('описание')
    price = models.IntegerField('цена')
    photo = models.ImageField('фото', upload_to='sets/photo', default='', blank=True)

    class Meta:
        verbose_name = 'сет'
        verbose_name_plural = 'sets'


    def __str__(self):
        return self.name


class Sushi(models.Model):
    name = models.CharField('название суши', max_length=50)
    description = models.TextField('описание')
    price = models.IntegerField('цена')
    photo = models.ImageField('фото', upload_to='sushi/photo', default='', blank=True)

    class Meta:
        verbose_name = 'суши'
        verbose_name_plural = 'sushi'

    def __str__(self):
        return self.name

class Soups(models.Model):
    name = models.CharField('название супа', max_length=50)
    description = models.TextField('описание')
    price = models.IntegerField('цена')
    photo = models.ImageField('фото', upload_to='soups/photo', default='', blank=True)

    class Meta:
        verbose_name = 'суп'
        verbose_name_plural = 'soups'

    def __str__(self):
        return self.name

class MainFood(models.Model):
    name = models.CharField('название супа', max_length=50)
    photo = models.ImageField('фото', upload_to='soups/photo', default='', blank=True)
    address =models.CharField('адрес url', max_length=50,blank=True)


    class Meta:
        verbose_name = 'меню на главной'
        verbose_name_plural = 'меню на главной'

    def __str__(self):
        return self.name

