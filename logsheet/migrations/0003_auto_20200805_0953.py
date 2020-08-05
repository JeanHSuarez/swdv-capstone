# Generated by Django 3.1 on 2020-08-05 09:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
        ('logsheet', '0002_delete_timesheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='logpost',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='DailyAggregator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('signInCount', models.IntegerField(default=0)),
                ('signOutCount', models.IntegerField(default=0)),
                ('totalDuration', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.member')),
            ],
        ),
    ]
