# Generated by Django 2.0.2 on 2019-05-25 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20190518_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['fechaEvento'], 'verbose_name': 'evento', 'verbose_name_plural': 'eventos'},
        ),
    ]
