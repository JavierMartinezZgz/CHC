# Generated by Django 2.0.2 on 2019-05-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombre', models.CharField(max_length=100, verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'provincia',
                'verbose_name_plural': 'provincias',
                'ordering': ['codigo'],
            },
        ),
    ]
