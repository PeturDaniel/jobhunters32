# Generated by Django 5.0.5 on 2024-05-08 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
        ('job_offers', '0003_joboffer_publish_date'),
        ('user', '0003_jobseekerprofile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobrecommendation',
            name='contact_availability',
        ),
        migrations.AddField(
            model_name='jobrecommendation',
            name='contacted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='jobrecommendation',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobrecommendation',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobrecommendation',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jobrecommendation',
            name='role',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('house_number', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField()),
                ('cover_letter', models.CharField(max_length=9999)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_application.jobexperience')),
                ('job_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_offers.joboffer')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_application.jobrecommendation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.jobseekerprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='Applications',
        ),
    ]
