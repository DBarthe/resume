# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'OT', max_length=2, choices=[(b'LA', b'Language'), (b'SY', b'System'), (b'DA', b'Database'), (b'SO', b'Software'), (b'OT', b'Other')])),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('weight', models.IntegerField(default=0, help_text=b'Will determine the display order, higher first')),
                ('icon', models.FileField(null=True, upload_to=b'')),
            ],
        ),
    ]
