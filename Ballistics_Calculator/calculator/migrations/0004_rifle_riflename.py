# Generated by Django 3.1.8 on 2021-07-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_dope'),
    ]

    operations = [
        migrations.AddField(
            model_name='rifle',
            name='rifleName',
            field=models.CharField(default=None, max_length=50),
        ),
    ]