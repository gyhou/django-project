# Generated by Django 3.0.2 on 2020-01-16 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200116_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 16, 15, 26, 45, 736828), verbose_name='date published'),
        ),
    ]
