# Generated by Django 5.0.6 on 2024-05-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='complete',
        ),
        migrations.AddField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
