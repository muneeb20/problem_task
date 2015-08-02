# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jenkins_conf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetail',
            name='job_description',
        ),
        migrations.AddField(
            model_name='jobdetail',
            name='job_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
