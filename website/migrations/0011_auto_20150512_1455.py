# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_education_educationtranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencetask',
            name='experiencetranslation',
            field=models.ForeignKey(to='website.EducationTranslation'),
        ),
    ]
