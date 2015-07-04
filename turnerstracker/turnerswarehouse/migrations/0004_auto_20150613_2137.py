# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnerswarehouse', '0003_auto_20150613_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='upc_code',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
