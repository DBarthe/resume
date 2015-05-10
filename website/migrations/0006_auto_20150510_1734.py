# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150510_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceTranslation',
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
        migrations.RemoveField(
            model_name='experiencetranslate',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='experiencetask',
            name='ExperienceTranslate',
        ),
        migrations.DeleteModel(
            name='ExperienceTranslate',
        ),
        migrations.AddField(
            model_name='experiencetask',
            name='experiencetranslation',
            field=models.ForeignKey(default=1, to='website.ExperienceTranslation'),
            preserve_default=False,
        ),
    ]
