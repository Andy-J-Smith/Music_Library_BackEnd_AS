# Generated by Django 4.0.3 on 2022-03-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_song_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='liked',
            field=models.IntegerField(default=0),
        ),
    ]