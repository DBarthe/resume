# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_skilltranslate_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(help_text='The youngest translation for a language will be selected', verbose_name='date', auto_now_add=True)),
                ('language', models.CharField(help_text='The language code (like "en" or "fr")', max_length=5, verbose_name='language')),
                ('description', models.TextField(help_text='A one or two lines description of the skill', verbose_name='description')),
                ('skill', models.ForeignKey(to='website.Skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='skilltranslate',
            name='skill',
        ),
        migrations.DeleteModel(
            name='SkillTranslate',
        ),
    ]
