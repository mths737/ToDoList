# Generated by Django 5.0.6 on 2024-05-16 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('complete', models.BooleanField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
