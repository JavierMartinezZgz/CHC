# Generated by Django 2.0.2 on 2019-05-18 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0007_provincia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['codigo'], 'verbose_name': 'provincia', 'verbose_name_plural': 'provincias'},
        ),
    ]
