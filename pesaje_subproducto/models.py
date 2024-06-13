from django.db import models
from users.models import Usuario
# Create your models here.

class PesajeSubproducto(models.Model):

    peso_sebo = models.FloatField(blank=False, null=False, db_column="ps_peso_sebo")
    peso_esofago = models.FloatField(blank=False, null=False, db_column="ps_peso_esofago")
    fecha = models.DateTimeField(blank=False, null=False, db_column="ps_fecha")
    serie = models.IntegerField(blank=False, null=False, db_column="ps_serie")
    responsable = models.IntegerField(blank=False, null=False, db_column="ps_responsable")
    usuario = models.ForeignKey(Usuario, default=None, on_delete = models.DO_NOTHING, db_column='ps_fk_usuario')
        
    def __str__(self):
        return self.serie

    class Meta:
        db_table = "pesaje_subproducto"
