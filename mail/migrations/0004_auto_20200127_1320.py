# Generated by Django 2.2.8 on 2020-01-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mail", "0003_auto_20200127_0855"),
    ]

    operations = [
        migrations.RenameModel(old_name="LicenceUsage", new_name="UsageUpdate",),
    ]
