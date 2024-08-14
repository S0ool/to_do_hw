# Generated by Django 5.0.6 on 2024-08-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('done', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
