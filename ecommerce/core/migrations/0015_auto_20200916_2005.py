# Generated by Django 3.0 on 2020-09-16 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200909_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='countries',
            new_name='country',
        ),
    ]
