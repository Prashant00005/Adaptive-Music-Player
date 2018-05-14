# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-03-17 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='usermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happy', models.FloatField(default=0.5)),
                ('sad', models.FloatField(default=0.5)),
                ('angry', models.FloatField(default=0.5)),
                ('anxious', models.FloatField(default=0.5)),
                ('loving', models.FloatField(default=0.5)),
                ('fearful', models.FloatField(default=0.5)),
                ('updaterate', models.FloatField(default=0.0)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
