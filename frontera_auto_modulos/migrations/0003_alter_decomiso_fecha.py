# Generated by Django 4.0.5 on 2024-06-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontera_auto_modulos', '0002_remove_decomiso_profesional_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decomiso',
            name='fecha',
            field=models.DateTimeField(auto_now=True, db_column='dc_fecha'),
        ),
    ]