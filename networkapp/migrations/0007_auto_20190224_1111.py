# Generated by Django 2.1.5 on 2019-02-24 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networkapp', '0006_auto_20190224_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='fname',
            new_name='full_name',
        ),
    ]
