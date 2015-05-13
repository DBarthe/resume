# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150510_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer', models.CharField(max_length=255, verbose_name='employer')),
                ('year_from', models.PositiveIntegerField(help_text='the year when the job began', verbose_name='start year')),
                ('year_to', models.PositiveIntegerField(help_text='the year when the job ended, or null', null=True, verbose_name='ending year')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExperienceTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text='Some lines that describe how the task was amazing !', verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceTranslate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(help_text='The youngest translation for a language will be selected', verbose_name='date', auto_now_add=True)),
                ('language', models.CharField(help_text='The language code (like "en" or "fr")', max_length=5, verbose_name='language')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('experience', models.ForeignKey(to='website.Experience')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='experiencetask',
            name='ExperienceTranslate',
            field=models.ForeignKey(to='website.ExperienceTranslate'),
        ),
    ]
