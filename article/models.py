from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('заголовок',max_length=100,unique_for_date='posted')
    description = models.TextField('краткое содержание')
    content = models.TextField('полное содержание')
    posted = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='опубликована')
    photo = models.ImageField('фото',blank=True,null=True)
    class Meta:
        ordering = ['-posted']
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField('заголовок', max_length=100, unique_for_date='posted')
    description = models.TextField('краткое содержание')
    content = models.TextField('полное содержание')
    posted = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='опубликована')
    photo = models.ImageField('фото', blank=True, null=True)

    class Meta:
        ordering = ['-posted']
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title
