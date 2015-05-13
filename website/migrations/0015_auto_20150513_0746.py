# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20150512_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(help_text='The youngest translation for a language will be selected', verbose_name='date', auto_now_add=True)),
                ('language', models.CharField(help_text='The language code (like "en" or "fr")', max_length=5, verbose_name='language')),
                ('title', models.CharField(max_length=255, verbose_name='current position in life (ex: student...)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
        migrations.AddField(
            model_name='profiletranslation',
            name='profiles',
            field=models.ForeignKey(to='website.Profile'),
        ),
    ]
