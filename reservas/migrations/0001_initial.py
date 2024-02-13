# Generated by Django 4.2.2 on 2023-06-28 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('bloco', models.CharField(max_length=1)),
                ('numero_sala', models.IntegerField()),
                ('capacidade', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_laboratorios',
            },
        ),
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('numero_sala', models.IntegerField()),
                ('bloco', models.CharField(max_length=1)),
                ('capacidade', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_salas',
            },
        ),
        migrations.CreateModel(
            name='ReservasSalas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_professor', models.CharField(max_length=100)),
                ('periodo', models.CharField(default='NOTURNO', max_length=20)),
                ('numero_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.salas')),
            ],
            options={
                'db_table': 'tb_reserva_salas',
            },
        ),
        migrations.CreateModel(
            name='ReservasLaboratorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField()),
                ('nome_professor', models.CharField(max_length=100)),
                ('periodo', models.CharField(default='NOTURNO', max_length=20)),
                ('estado', models.IntegerField(default=0)),
                ('nome_laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.laboratorios')),
            ],
            options={
                'db_table': 'tb_reservas_laboratorios',
            },
        ),
    ]
