# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(max_length=100)),
                ('job_description', models.TextField(null=True, blank=True)),
                ('status', models.CharField(max_length=20)),
                ('execution_time', models.DateTimeField()),
            ],
        ),
    ]
