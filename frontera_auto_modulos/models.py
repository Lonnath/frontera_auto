from django.db import models
from users.models import Usuario


class Vicera(models.Model):
    
    turno = models.IntegerField(blank=False, null=False, db_column="vc_turno")
    cifra = models.IntegerField(blank=False, null=False, db_column="vc_cifra")
    peso = models.IntegerField(blank=False, null=False, db_column="vc_peso")
    serie = models.CharField(max_length=15, null=False, db_column="vc_serie")
    responsable_firma = models.IntegerField(blank=False, null=False, db_column="vc_responsable_firma")
    tipo_vicera = models.CharField(max_length=150, null=False, db_column="vc_tipo_vicera")
    
    def __str__(self):
        return self.serie
    
    class Meta:
        db_table = 'vicera'
    
class Decomiso (models.Model):

    usuario = models.ForeignKey(Usuario, default=None, on_delete = models.DO_NOTHING, db_column='dc_fk_usuario')
    ciudad = models.CharField(max_length=25, blank=False, null=False, db_column="dc_ciudad")
    producto = models.CharField(max_length=25, blank=False, null=False, db_column="dc_producto")
    serie = models.CharField(max_length=15, blank=False, null=False, db_column="dc_serie")
    fecha = models.DateTimeField(auto_now=True, blank=False, null=False, db_column="dc_fecha")
    cifra = models.IntegerField(blank=False, null=False, db_column="dc_cifra")
    cantidad = models.IntegerField(blank=False, null=False, db_column="dc_cantidad")
    causa = models.CharField(max_length=255, blank=False, null=False, db_column="dc_causa")
    foto = models.ImageField(upload_to='fotos/', blank=False, null=False, db_column="dc_foto")
    turno = models.IntegerField(blank=False, null=False, db_column="dc_turno")
    observacion = models.CharField(max_length=255, blank=True, null=False, db_column="dc_observacion")
    
    def __str__ (self) :
        return self.serie

    class Meta:
        db_table = 'decomiso'


class PesajeSubproducto(models.Model):

    peso_sebo = models.FloatField(blank=False, null=False, db_column="ps_peso_sebo")
    peso_esofago = models.FloatField(blank=False, null=False, db_column="ps_peso_esofago")
    fecha = models.DateTimeField(auto_now=True, blank=False, null=False, db_column="ps_fecha")
    serie = models.IntegerField(blank=False, null=False, db_column="ps_serie")
    responsable = models.IntegerField(blank=False, null=False, db_column="ps_responsable")
    usuario = models.ForeignKey(Usuario, default=None, on_delete = models.DO_NOTHING, db_column='ps_fk_usuario')
    vicera = models.ForeignKey(Vicera, default=None, on_delete = models.DO_NOTHING, db_column='ps_fk_vicera')
    
    def __str__(self):
        return self.serie

    class Meta:
        db_table = "pesaje_subproducto"