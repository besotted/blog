# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-11 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='postblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timedata', models.DateTimeField(auto_now_add=True)),
                ('blg', models.ManyToManyField(to='postapp.blog_type')),
            ],
        ),
        migrations.CreateModel(
            name='stopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='postblog',
            name='stic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postapp.stopic'),
        ),
    ]