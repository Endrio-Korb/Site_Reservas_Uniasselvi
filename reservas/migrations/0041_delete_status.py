# Generated by Django 5.0.3 on 2024-03-05 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0040_rename_laboratorio_id_reservaslaboratorios_laboratorio_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]