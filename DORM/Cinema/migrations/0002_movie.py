# Generated by Django 4.1.3 on 2022-11-07 12:40

import Cinema.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.TimeField()),
                ('release', models.DateTimeField()),
                ('poster', models.ImageField(default='Images/Movies/default.png', upload_to=Cinema.models.movie_directory_path)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('cast', models.ManyToManyField(to='Cinema.actor')),
                ('country', models.ManyToManyField(to='Cinema.country')),
                ('genres', models.ManyToManyField(to='Cinema.genre')),
                ('producers', models.ManyToManyField(to='Cinema.producer')),
                ('production', models.ManyToManyField(to='Cinema.company')),
            ],
            options={
                'ordering': ['release'],
            },
        ),
    ]
