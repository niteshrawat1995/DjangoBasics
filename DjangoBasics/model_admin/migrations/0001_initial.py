# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-25 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import model_admin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Source name')),
                ('slug', models.SlugField(unique=True, verbose_name='Content Slug')),
                ('icon', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Content icon')),
                ('doc', models.FileField(blank=True, null=True, upload_to=model_admin.models.upload_location, verbose_name='Doc File')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Source name')),
                ('type', models.CharField(choices=[('edx', 'Edx'), ('connect', 'Connect')], max_length=255, verbose_name='Source Type')),
                ('title', models.CharField(max_length=255, verbose_name='Source Title')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Source order')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Content Source',
                'verbose_name_plural': 'Content Sources',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_admin.Source'),
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('name', 'title')]),
        ),
    ]
