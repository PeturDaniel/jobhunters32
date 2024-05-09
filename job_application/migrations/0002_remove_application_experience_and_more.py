# Generated by Django 5.0.5 on 2024-05-09 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='application',
            name='recommendation',
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='job_application',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='job_application.application'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobrecommendation',
            name='job_application',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='job_application.application'),
            preserve_default=False,
        ),
    ]