# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20150513_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalskill',
            name='icon',
            field=models.FileField(upload_to=b'', null=True, verbose_name='icon', blank=True),
        ),
    ]
