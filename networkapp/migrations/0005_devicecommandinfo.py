# Generated by Django 2.1.5 on 2019-02-11 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkapp', '0004_auto_20190210_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceCommandInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_command', models.CharField(max_length=100, unique=True)),
                ('command_name', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
