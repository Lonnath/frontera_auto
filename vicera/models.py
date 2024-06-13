from django.db import models
from pesaje_subproducto.models import PesajeSubproducto

class Vicera(models.Model):
    
    pesaje_subproducto = models.ForeignKey(PesajeSubproducto, default=None, on_delete = models.DO_NOTHING, db_column='vc_fk_pesaje_subproducto')
    turno = models.IntegerField(blank=False, null=False, db_column="vc_turno")
    cifra = models.IntegerField(blank=False, null=False, db_column="vc_cifra")
    peso = models.IntegerField(blank=False, null=False, db_column="vc_peso")
    serie = models.CharField(max_length=15, null=False, db_column="us_serie")
    responsable_firma = models.IntegerField(blank=False, null=False, db_column="vc_responsable_firma")
    tipo_vicera = models.CharField(max_length=150, null=False, db_column="us_tipo_vicera")
    
    def __str__(self):
        return self.serie
    
    class Meta:
        db_table = 'vicera'