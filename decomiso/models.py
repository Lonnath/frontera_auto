from django.db import models
from users.models import Usuario

class Decomiso (models.Model):

    usuario = models.ForeignKey(Usuario, default=None, on_delete = models.DO_NOTHING, db_column='dc_fk_usuario')
    ciudad = models.CharField(max_length=25, blank=False, null=False, db_column="dc_ciudad")
    producto = models.CharField(max_length=25, blank=False, null=False, db_column="dc_producto")
    serie = models.CharField(max_length=15, blank=False, null=False, db_column="dc_serie")
    fecha = models.DateTimeField(blank=False, null=False, db_column="dc_fecha")
    cifra = models.IntegerField(blank=False, null=False, db_column="dc_cifra")
    cantidad = models.IntegerField(blank=False, null=False, db_column="dc_cantidad")
    causa = models.CharField(max_length=255, blank=False, null=False, db_column="dc_causa")
    profesional_cargo = models.IntegerField(blank=False, null=False, db_column="dc_profesional_cargo")
    foto = models.CharField(max_length=150, blank=False, null=False, db_column="dc_foto")
    veterinario = models.IntegerField(blank=False, null=False, db_column="dc_veterinario")
    turno = models.IntegerField(blank=False, null=False, db_column="dc_turno")
    
    def __str__ (self) :
        return self.serie

    class Meta:
        db_table = 'decomiso'