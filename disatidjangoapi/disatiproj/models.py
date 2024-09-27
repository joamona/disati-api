from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos

class CatastrosIberoamerica(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    paisid = models.IntegerField()
    nombre_division = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        db_table = 'geo_data.catastros_iberoamerica'
        managed = False  

    def __str__(self):
        return f"ID: {self.id}, País: {self.pais}, PaisId: {self.paisId}, Nombre de división: {self.nombre_division}, Nombre: {self.nombre}, URL: {self.url}, Código: {self.codigo}"

class PaisesIberoamerica(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    paisid = models.IntegerField()
    url = models.CharField(max_length=255)
    miembro_cpci = models.CharField(max_length=255)
    miembro_appat = models.CharField(max_length=255)
    data_2011 = models.CharField(max_length=255)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        db_table = 'geo_data.paises_iberoamerica'
        managed = False  

    def __str__(self):
        return f"ID: {self.id}, País: {self.pais}, PaisId: {self.paisId},  Miembro CPCI: {self.miembro_cpci}, Miembro APPAT: {self.miembro_appat}, URL: {self.url}"


class AppatMiembros(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    paisid = models.IntegerField()
    institucion = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    funciona = models.BooleanField()
    idioma = models.CharField(max_length=255)

    class Meta:
        db_table = 'appat_miembros'
        managed = False

    def __str__(self):
        return f"ID: {self.id}, País: {self.pais}, PaisId: {self.paisid}, Institución: {self.institucion}, Web: {self.web}, Funciona: {self.funciona}, Idioma: {self.idioma}"

class CpciMiembros(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    paisid = models.IntegerField()
    institucion = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    funciona = models.BooleanField()
    idioma = models.CharField(max_length=255)

    class Meta:
        db_table = 'cpci_miembros'
        managed = False  

    def __str__(self):
        return f"ID: {self.id}, País: {self.pais}, PaisId: {self.paisid}, Institución: {self.institucion}, Web: {self.web}, Funciona: {self.funciona}, Idioma: {self.idioma}"

class CpciObservadores(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    paisid = models.IntegerField()
    institucion = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    funciona = models.BooleanField()
    idioma = models.CharField(max_length=255)
    listado = models.BooleanField()
    logo = models.BooleanField()

    class Meta:
        db_table = 'cpci_observadores'
        managed = False  

    def __str__(self):
        return f"ID: {self.id}, País: {self.pais}, PaisId: {self.paisid}, Institución: {self.institucion}, Web: {self.web}, Funciona: {self.funciona}, Idioma: {self.idioma}, Listado: {self.listado}, Logo: {self.logo}"

class DatosEncuesta(models.Model):
    id = models.AutoField(primary_key=True)
    orden = models.IntegerField()
    enunciado = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    paisid = models.IntegerField()
    nombre_entidad = models.CharField(max_length=255)

    class Meta:
        db_table = 'datos_encuesta'
        managed = False  

    def __str__(self):
        return f"ID: {self.id}, Orden: {self.orden}, Enunciado: {self.enunciado}, Respuesta: {self.respuesta}, País: {self.pais}, PaisId: {self.paisid}, Entidad: {self.nombre_entidad}"

