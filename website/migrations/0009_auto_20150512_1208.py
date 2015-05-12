# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150511_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='year_to',
            field=models.PositiveIntegerField(help_text='the year when the job ended, otherwise leave it blank', null=True, verbose_name='ending year', blank=True),
        ),
        migrations.AlterField(
            model_name='technicalskill',
            name='category',
            field=models.CharField(default=b'OT', max_length=2, verbose_name='category', choices=[(b'LA', 'Language'), (b'FA', 'Framework'), (b'SY', 'System'), (b'DA', 'Database'), (b'SO', 'Software'), (b'OT', 'Other')]),
        ),
    ]
