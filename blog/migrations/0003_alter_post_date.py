# Generated by Django 4.2.7 on 2023-11-23 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 18, 0, 24, 342228, tzinfo=datetime.timezone.utc), verbose_name='Дата создания поста'),
        ),
    ]
