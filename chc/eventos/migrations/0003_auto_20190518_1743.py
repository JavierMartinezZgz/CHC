# Generated by Django 2.0.2 on 2019-05-18 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_provincia'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=2, verbose_name='Tipo Evento')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre tipo Evento')),
            ],
            options={
                'verbose_name': 'tipo de evento',
                'verbose_name_plural': 'tipos de eventos',
                'ordering': ['tipo'],
            },
        ),
        migrations.AddField(
            model_name='evento',
            name='tipoevento',
            field=models.ForeignKey(default='00', on_delete=django.db.models.deletion.CASCADE, to='eventos.TipoEvento', verbose_name='Tipo'),
        ),
    ]
