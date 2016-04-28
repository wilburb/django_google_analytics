# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAnalytics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('web_property_id', models.CharField(max_length=15, blank=True)),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
        ),
    ]
