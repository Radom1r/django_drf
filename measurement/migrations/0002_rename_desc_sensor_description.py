# Generated by Django 4.2.6 on 2023-11-02 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='desc',
            new_name='description',
        ),
    ]
