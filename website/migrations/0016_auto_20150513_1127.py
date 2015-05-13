# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20150513_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiletranslation',
            name='title',
            field=models.CharField(help_text='current position in life (ex: student...)', max_length=255, verbose_name='title'),
        ),
    ]
