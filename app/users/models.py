from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=64, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    Birthday = models.DateField(auto_now=False, null=True)
    email = models.CharField(max_length=128, unique=True, verbose_name='E-Mail')

    def __str__(self):
        return f'{self.user_name | self.first_name | self.last_name | self.Birthday | self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user_name


class Biography(models.Model):
    text = models.TextField(null=True, blank=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Book(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
