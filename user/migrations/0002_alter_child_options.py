# Generated by Django 4.0.1 on 2022-01-14 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'ordering': ['first_name'], 'verbose_name_plural': 'Children'},
        ),
    ]
