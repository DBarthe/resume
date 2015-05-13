# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_extra_extratranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extratranslation',
            name='description',
            field=models.TextField(default='', help_text='An optional description of this extra', verbose_name='description', blank=True),
            preserve_default=False,
        ),
    ]
