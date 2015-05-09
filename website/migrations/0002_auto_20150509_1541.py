# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('weight', models.IntegerField(default=0, help_text='Will determine the display order, higher first', verbose_name='weight')),
            ],
        ),
        migrations.CreateModel(
            name='SkillTranslate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(help_text='The language code (like "en" or "en-us")', max_length=5, verbose_name='language')),
                ('description', models.TextField(help_text='A one or two lines description of the skill', verbose_name='description')),
                ('skill', models.ForeignKey(to='website.Skill')),
            ],
        ),
        migrations.AlterField(
            model_name='technicalskill',
            name='category',
            field=models.CharField(default=b'OT', max_length=2, verbose_name='category', choices=[(b'LA', 'Language'), (b'SY', 'System'), (b'DA', 'Database'), (b'SO', 'Software'), (b'OT', 'Other')]),
        ),
        migrations.AlterField(
            model_name='technicalskill',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='technicalskill',
            name='icon',
            field=models.FileField(upload_to=b'', null=True, verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='technicalskill',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='technicalskill',
            name='weight',
            field=models.IntegerField(default=0, help_text='Will determine the display order, higher first', verbose_name='weight'),
        ),
    ]
