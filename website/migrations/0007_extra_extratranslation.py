# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150510_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('weight', models.IntegerField(default=0, help_text='Will determine the display order, higher first', verbose_name='weight')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtraTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(help_text='The youngest translation for a language will be selected', verbose_name='date', auto_now_add=True)),
                ('language', models.CharField(help_text='The language code (like "en" or "fr")', max_length=5, verbose_name='language')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(help_text='An optional description of this extra', null=True, verbose_name='description')),
                ('extra', models.ForeignKey(to='website.Extra')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
