# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20150512_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationtranslation',
            name='education',
            field=models.ForeignKey(to='website.Education'),
        ),
        migrations.AlterField(
            model_name='experiencetask',
            name='experiencetranslation',
            field=models.ForeignKey(to='website.ExperienceTranslation'),
        ),
    ]
