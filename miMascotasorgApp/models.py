from tabnanny import verbose
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save

# --------------------------------- MODELOS BASE --------------------------------- #

class ModelBase(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    titulo = models.TextField(blank=False, max_length=100)
    subtitulo = models.TextField(blank=False, max_length=200)
    detalle = RichTextField()
    time = models.DateTimeField(auto_now=True)    
    bibliografia = models.URLField(blank=True, null=True)
    
    class Meta:
        abstract = True

class ModelBaseMascota(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    nombre = models.TextField(blank=False, max_length=100) 
    caracter = models.TextField(blank=False, max_length=100)       
    salud = models.TextField(blank=False, max_length=100) 
    altura = models.TextField(blank=False, max_length=100) 
    peso = models.TextField(blank=False, max_length=100) 
    observaciones = models.TextField(blank=False, max_length=150)
    
    class Meta:
        abstract = True


# --------------------------------- SERVICIOS --------------------------------- #

class Sanitario(ModelBase):
    imagen = models.ImageField(blank=False, upload_to='sanitario', default="")
    
    class Meta:
        verbose_name = 'Sanitarios'
        verbose_name_plural = 'Sanitarios'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)    

@receiver(pre_delete, sender=Sanitario)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)

class Legal(ModelBase):
    imagen = models.ImageField(blank=False, upload_to='legal', default="")
    
    class Meta:
        verbose_name = 'Legal'
        verbose_name_plural = 'Legal'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

@receiver(pre_delete, sender=Legal)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)
    

class Alimentacion(ModelBase):
    imagen = models.ImageField(blank=False, upload_to='alimentacion', default="")
    
    class Meta:
        verbose_name = 'Alimentacion'
        verbose_name_plural = 'Alimentacion'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

@receiver(pre_delete, sender=Alimentacion)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)

class Alojamiento(ModelBase):
    imagen = models.ImageField(blank=False, upload_to='alojamiento', default="")
    
    class Meta:
        verbose_name = 'Alojamiento'
        verbose_name_plural = 'Alojamiento'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

@receiver(pre_delete, sender=Alojamiento)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)
    
class Entrenamiento(ModelBase):
    imagen = models.ImageField(blank=False, upload_to='entrenamiento', default="")
    
    class Meta:
        verbose_name = 'Entrenamiento'
        verbose_name_plural = 'Entrenamiento'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

@receiver(pre_delete, sender=Entrenamiento)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)
    
class Otros(ModelBase):
    imagen = models.ImageField(blank=False, upload_to='otros', default="")
    
    class Meta:
        verbose_name = 'Otros'
        verbose_name_plural = 'Otros'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

@receiver(pre_delete, sender=Otros)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)

class Consejos(ModelBase):
    imagen = models.ImageField(blank=False, upload_to='consejos', default="")
    keyword = models.CharField(blank=False, max_length=200, default="")
    
    class Meta:
        verbose_name = 'Consejos'
        verbose_name_plural = 'Consejos'
        
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

@receiver(pre_delete, sender=Consejos)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)
    
# --------------------------------- MASCOTAS --------------------------------- #

class perro(ModelBaseMascota):
    tipo = models.CharField(max_length=50, choices=(
    ('grande','grande'),
    ('mediano', 'mediano'),
    ('pequeño','pequeño'),
    ), default='grande')
    imagen = models.ImageField(blank=False, upload_to='perro', default="")
    
    class Meta:
        verbose_name = 'Perro'
        verbose_name_plural = 'Perro'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

class gato(ModelBaseMascota):
    tipo = models.CharField(max_length=50, choices=(
    ('pelo largo','pelo largo'),
    ('pelo mediano', 'pelo mediano'),
    ('pelo corto','pelo corto'),
    ), default='pelo largo')
    imagen = models.ImageField(blank=False, upload_to='gato', default="")
    
    class Meta:
        verbose_name = 'Gato'
        verbose_name_plural = 'Gato'
    
    # def __str__(self):
    #     return str(self.id, self.titulo, self.subtitulo, self.detalle, self.imagen)

class caballo(ModelBaseMascota):
    tipo = models.CharField(max_length=50, choices=(
    ('sangre caliente','sangre caliente'),
    ('sangre fria', 'sangre fria'),
    ('sangre templada','sangre templada'),
    ('pony','pony'),
    ('pura sangre','pura sangre'),
    ('barroco','barroco'),
    ), default='sangre caliente')
    imagen = models.ImageField(blank=False, upload_to='caballo', default="")
    
    class Meta:
        verbose_name = 'Caballo'
        verbose_name_plural = 'Caballo'
    
class pajaro(ModelBaseMascota):
    tipo = models.CharField(max_length=50, choices=(
    ('grandes','grandes'),
    ('medianos', 'medianos'),
    ('pequeños', 'pequeños'),
    ), default='grandes')
    imagen = models.ImageField(blank=False, upload_to='pajaro', default="")
    
    class Meta:
        verbose_name = 'Pajaro'
        verbose_name_plural = 'Pajaro'

class peces(ModelBaseMascota):
    tipo = models.CharField(max_length=50, choices=(
    ('agua dulce','agua dulce'),
    ('agua salada','agua salada')
    ), default='agua dulce')
    imagen = models.ImageField(blank=False, upload_to='peces', default="")
    
    class Meta:
        verbose_name = 'Peces'
        verbose_name_plural = 'Peces'