# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-06-27 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0002_remove_lesson_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='teacher_note',
            field=models.TextField(blank=True),
        ),
    ]
