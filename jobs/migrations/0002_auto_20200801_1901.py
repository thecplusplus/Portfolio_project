# Generated by Django 2.2.14 on 2020-08-01 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='image',
            new_name='imagech',
        ),
    ]
