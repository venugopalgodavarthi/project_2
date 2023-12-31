# Generated by Django 4.2.6 on 2023-11-03 05:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='dob',
            field=models.DateField(default='2021-05-06'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal',
            name='dor',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal',
            name='gender',
            field=models.CharField(choices=[['male', 'Male'], ['female', 'Female']], default='Male', max_length=10),
            preserve_default=False,
        ),
    ]
