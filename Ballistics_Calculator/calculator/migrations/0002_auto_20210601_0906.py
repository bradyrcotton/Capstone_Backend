# Generated by Django 3.1.8 on 2021-06-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifle',
            name='scopeAdjustment',
            field=models.IntegerField(default=4),
        ),
    ]
