# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_profil'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profil',
            new_name='Profile',
        ),
    ]
