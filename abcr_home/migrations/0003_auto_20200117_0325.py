# Generated by Django 2.2 on 2020-01-16 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abcr_home', '0002_auto_20200117_0257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summary',
            old_name='summary',
            new_name='text',
        ),
    ]
