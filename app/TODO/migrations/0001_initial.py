# Generated by Django 4.1.7 on 2023-03-21 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_book_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2023-03-21')),
                ('due_date', models.DateField(default='2023-03-21')),
                ('is_active', models.BooleanField(default=True, verbose_name='Состояние')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user', verbose_name='Заметки')),
            ],
            options={
                'verbose_name': 'ToDolist',
                'verbose_name_plural': 'ToDolists',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название проекта')),
                ('repo_link', models.TextField(blank=True, verbose_name='Слыка на репозитарий')),
                ('users', models.ManyToManyField(to='users.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
