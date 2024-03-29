# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 19:42
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20160414_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='assignment',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Course'),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='difficulty',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='course',
            name='difficulty',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='course',
            name='url',
            field=models.URLField(max_length=256),
        ),
        migrations.AlterField(
            model_name='course',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
