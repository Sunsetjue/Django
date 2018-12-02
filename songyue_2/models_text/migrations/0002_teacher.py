# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_text', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('teacher_name', models.CharField(max_length=4)),
                ('teacher_age', models.IntegerField()),
                ('teacher_gender', models.CharField(max_length=1)),
                ('teacher', models.ForeignKey(to='models_text.School')),
            ],
        ),
    ]
