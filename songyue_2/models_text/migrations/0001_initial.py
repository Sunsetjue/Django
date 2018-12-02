# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('manage_id', models.IntegerField()),
                ('manage_name', models.CharField(max_length=4)),
                ('manage_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=20)),
                ('school_address', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='manage',
            name='my_school',
            field=models.OneToOneField(to='models_text.School'),
        ),
    ]
