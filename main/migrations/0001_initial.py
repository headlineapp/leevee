# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-22 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('tweet_id', models.IntegerField()),
                ('text', models.TextField(max_length=300)),
                ('truncated', models.BooleanField()),
                ('source', models.CharField(max_length=300)),
                ('in_reply_to_status_id', models.IntegerField()),
                ('in_reply_to_user_id', models.IntegerField()),
                ('in_reply_to_screen_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('screen_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('profile_image_url', models.URLField()),
                ('entities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Entities')),
            ],
        ),
        migrations.CreateModel(
            name='UserMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mention_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='entities',
            name='user_mentions',
            field=models.ManyToManyField(to='main.UserMention'),
        ),
    ]
