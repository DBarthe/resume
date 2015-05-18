# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_technicalskill_icon_attribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.FileField(upload_to=b'', null=True, verbose_name='picture', blank=True),
        ),
    ]
