# Generated by Django 5.2.1 on 2025-05-27 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shedult', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='last_ame',
            new_name='last_name',
        ),
    ]
