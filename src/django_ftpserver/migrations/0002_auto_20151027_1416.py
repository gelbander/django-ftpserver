# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ftpserver', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ftpuseraccount',
            name='home_dir',
        ),
        migrations.RemoveField(
            model_name='ftpusergroup',
            name='home_dir',
        ),
    ]
