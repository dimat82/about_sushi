from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField('имя',max_length=50)
    email = models.EmailField('e-mail',max_length=100)
    phone = models.CharField('телефон',max_length=100)
    content = models.TextField('Обратная связь')

    def __str__(self):
        return self.name



