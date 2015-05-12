# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20150512_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_from', models.PositiveIntegerField(help_text='the year when the formation began', verbose_name='start year')),
                ('year_to', models.PositiveIntegerField(help_text='the year when the formation ended, otherwise leave it blank', null=True, verbose_name='ending year', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EducationTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(help_text='The youngest translation for a language will be selected', verbose_name='date', auto_now_add=True)),
                ('language', models.CharField(help_text='The language code (like "en" or "fr")', max_length=5, verbose_name='language')),
                ('school', models.CharField(max_length=255, verbose_name='school')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('education', models.ForeignKey(to='website.Experience')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
