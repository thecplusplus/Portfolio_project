# Generated by Django 2.2.14 on 2020-08-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_pub',
            field=models.DateTimeField(),
        ),
    ]
