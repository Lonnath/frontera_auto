# Generated by Django 4.0.5 on 2024-06-14 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vicera', '0002_remove_vicera_pesaje_subproducto'),
        ('pesaje_subproducto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesajesubproducto',
            name='vicera',
            field=models.ForeignKey(db_column='ps_fk_vicera', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='vicera.vicera'),
        ),
    ]
