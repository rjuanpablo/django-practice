# Generated by Django 4.2.13 on 2024-06-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]