# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('purpose', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('size', models.SmallIntegerField(default=4)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(related_name='reservations', to='romres.Room'),
        ),
    ]
