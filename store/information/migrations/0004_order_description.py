# Generated by Django 2.1.7 on 2019-03-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_auto_20190305_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(default='description', max_length=250),
        ),
    ]