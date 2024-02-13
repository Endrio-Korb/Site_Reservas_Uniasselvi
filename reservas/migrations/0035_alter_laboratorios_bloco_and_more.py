# Generated by Django 4.2.3 on 2023-11-29 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0034_delete_reservassalas_delete_salas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorios',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.blocos'),
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.blocos'),
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.periodos'),
        ),
    ]
