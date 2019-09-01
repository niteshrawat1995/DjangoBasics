# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('model_admin', '0004_auto_20190901_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='identifier',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='source',
            name='identifier',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='identifier',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
