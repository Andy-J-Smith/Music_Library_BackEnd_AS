# Generated by Django 4.0.3 on 2022-03-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='liked',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
