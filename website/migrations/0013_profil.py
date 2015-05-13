# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20150512_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(max_length=31, verbose_name='first name')),
                ('lastname', models.CharField(max_length=31, verbose_name='last name')),
                ('birthdate', models.DateField(verbose_name='birth date')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('phone', models.CharField(max_length=31, verbose_name='phone number')),
                ('street_address', models.CharField(max_length=255, verbose_name='street address')),
                ('zip_code', models.CharField(max_length=15, verbose_name='zip code')),
                ('city', models.CharField(max_length=31, verbose_name='city name')),
                ('country', models.CharField(max_length=31, verbose_name='country name')),
                ('title', models.CharField(max_length=255, verbose_name='current position in life (ex: student...)')),
                ('github', models.URLField(verbose_name='url of the github account')),
            ],
        ),
    ]
