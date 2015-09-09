# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='timestamp',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='bodytext',
            new_name='text',
        ),
    ]
