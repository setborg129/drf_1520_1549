from django.db import models
from django.utils import timezone
from users.models import User


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название проекта')
    repo_link = models.TextField(blank=True, verbose_name="Слыка на репозитарий")
    users = models.ManyToManyField(User, verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


def __str__(self):
    return f'{self.name}'


class ToDolist(models.Model):
    project = models.ForeignKey(Project, models.PROTECT, verbose_name='Проект')
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлена')
    user = models.ForeignKey(User, models.PROTECT, verbose_name='Автор заметки')
    is_active = models.BooleanField(default=False, verbose_name='Состояние')

    class Meta:
        verbose_name = ("Заметка")
        verbose_name_plural = ("Заметки")

    def __str__(self):
        return self.project


