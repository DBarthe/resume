# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150509_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilltranslate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 10, 13, 50, 36, 380436, tzinfo=utc), auto_now_add=True, help_text='The youngest translation for a language will be selected', verbose_name='date'),
            preserve_default=False,
        ),
    ]
