# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'turnerswarehouse', '0001_initial'), (b'turnerswarehouse', '0002_auto_20150612_0334'), (b'turnerswarehouse', '0003_auto_20150613_2128'), (b'turnerswarehouse', '0004_auto_20150613_2137')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=100)),
                ('upc_code', models.BigIntegerField(null=True, blank=True)),
                ('category', models.ForeignKey(to='turnerswarehouse.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
