# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('a_desc', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField()),
                ('r_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('t_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='a_region',
            field=models.ForeignKey(to='myapp.Region'),
        ),
        migrations.AddField(
            model_name='ad',
            name='a_tag',
            field=models.ForeignKey(to='myapp.Tag'),
        ),
    ]
