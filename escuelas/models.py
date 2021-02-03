# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Coordinaciones(models.Model):
    cve_co = models.IntegerField(primary_key=True)
    cz = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'coordinaciones'
    def __str__(self):
        return self.cz



class Localidades(models.Model):
    cvegeo = models.IntegerField(primary_key=True)
    loc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'localidades'
    def __str__(self):
        return self.loc


class Municipios(models.Model):
    cvegeo = models.IntegerField(primary_key=True)
    mun = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'municipios'
    def __str__(self):
        return self.mun

class Unidad_Operativa(models.Model):
    Clave_Unidad_Operativa = models.CharField(max_length=10,primary_key=True)
    Tipo_Unidad_Operativa = models.CharField(max_length=30,choices=[("Circulo de estudio","Circulo de estudio"),("Punto de encuentro","Punto de encuentro"),("Plaza comunitaria","Plaza comunitaria")])
    Nombre_Unidad_Operativa = models.CharField(max_length=100)
    Municipio = models.ForeignKey(Municipios,models.DO_NOTHING)
    Coordinación = models.ForeignKey(Coordinaciones,models.DO_NOTHING)
    Domicilio = models.CharField(max_length=100)
    Colonia = models.CharField(max_length=100)
    Codigo_Postal = models.CharField(max_length=10)
    Geolocalización = models.PointField()

    class Meta:
        verbose_name_plural = "Unidad Operativa"
    
    def __str__(self):
        
        return self.Clave_Unidad_Operativa
    

class EDOMEX(models.Model):
    cve_ent = models.CharField(max_length=2)
    cve_mun = models.CharField(max_length=3)
    cvegeo = models.CharField(max_length=5)
    nomgeo = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.nomgeo
    class Meta:
        verbose_name_plural="Edomex"
    
