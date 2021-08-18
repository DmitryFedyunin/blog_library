# Generated by Django 3.2.5 on 2021-08-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=150, verbose_name='Автор')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
                ('description', models.TextField()),
            ],
        ),
    ]