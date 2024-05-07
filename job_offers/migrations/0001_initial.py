# Generated by Django 5.0.5 on 2024-05-07 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('percentage', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('due_date', models.DateField()),
                ('start_date', models.DateField(default=datetime.datetime(2024, 5, 7, 10, 50, 33, 467361, tzinfo=datetime.timezone.utc))),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]