# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20150515_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalskill',
            name='icon_attribution',
            field=models.URLField(help_text='set it if the license requires it', null=True, verbose_name="a link to the author's website", blank=True),
        ),
    ]
