# Generated by Django 3.0.2 on 2020-01-12 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200111_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 22, 11, 34, 378930), verbose_name='date published'),
        ),
    ]
