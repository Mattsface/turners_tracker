# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnerswarehouse', '0002_auto_20150612_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='upc_code',
            field=models.BigIntegerField(blank=True),
        ),
    ]
