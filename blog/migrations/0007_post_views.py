# Generated by Django 4.2.7 on 2023-12-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Проссмотры'),
        ),
    ]
