# Generated by Django 3.0.8 on 2021-09-12 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 8, 28, 3, 708635, tzinfo=utc)),
        ),
    ]
