# Generated by Django 2.2.4 on 2019-09-01 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190901_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
    ]
