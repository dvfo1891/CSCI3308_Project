# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 22:01
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.CharField(max_length=1024)),
                ('time', models.DateTimeField(default=datetime.datetime(2016, 4, 14, 22, 1, 33, 833966, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='notification',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL),
        ),
    ]