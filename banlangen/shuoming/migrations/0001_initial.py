# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('roomID', models.IntegerField()),
                ('loc', models.CharField(max_length=10)),
                ('roomName', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('studentName', models.CharField(max_length=4)),
                ('age', models.IntegerField()),
                ('student', models.ForeignKey(to='shuoming.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('teacherName', models.CharField(max_length=4)),
                ('course', models.CharField(max_length=10)),
                ('teacher', models.OneToOneField(to='shuoming.ClassRoom')),
            ],
        ),
    ]
