# Generated by Django 2.1.5 on 2019-02-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkapp', '0005_devicecommandinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_site',
            new_name='fname',
        ),
        migrations.AlterField(
            model_name='devicecommandinfo',
            name='command_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
