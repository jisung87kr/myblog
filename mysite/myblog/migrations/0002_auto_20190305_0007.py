# Generated by Django 2.1.7 on 2019-03-04 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 4, 15, 7, 6, 934339, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 3, 4, 15, 7, 6, 934376, tzinfo=utc)),
        ),
    ]
