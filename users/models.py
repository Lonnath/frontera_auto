from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    nombre = models.CharField(max_length=50, null=False, db_column="us_nombre")
    apellido = models.CharField(max_length=50, null=False, db_column="us_apellido")
    fecha_nacimiento = models.DateTimeField(auto_now=True, db_column="us_fecha_nacimiento")
    direccion = models.CharField(max_length=255, null=False, db_column="us_direccion")
    telefono = models.CharField(max_length=25, null=False, db_column="us_telefono")
    tipo_usuario = models.CharField(max_length=20, null=False, db_column="us_tipo_usuario")
    password = models.CharField(max_length=255, null=False, db_column="us_pass")
    usuario = models.CharField(max_length=20, null=False, unique=True, db_column="us_usuario")
    cc_documento = models.IntegerField(blank=False, null=False, db_column="us_cc_documento", unique=True)
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = "usuarios"
