from django.contrib import admin

from miMascotasorgApp.models import Alimentacion, Alojamiento, Consejos, Entrenamiento, Legal, Otros, Sanitario, caballo, gato, pajaro, peces, perro

# ------ SERVICIOS ------- #

class SanitarioAdmin(admin.ModelAdmin):
      list_display = ('id', 'titulo', 'subtitulo')
admin.site.register(Sanitario, SanitarioAdmin)

class LegalAdmin(admin.ModelAdmin):
      list_display = ('id', 'titulo', 'subtitulo')
admin.site.register(Legal, LegalAdmin)

class AlimentacionAdmin(admin.ModelAdmin):
      list_display = ('id', 'titulo', 'subtitulo')
admin.site.register(Alimentacion, AlimentacionAdmin)

class AlojamientoAdmin(admin.ModelAdmin):
      list_display = ('id', 'titulo', 'subtitulo')
admin.site.register(Alojamiento, AlojamientoAdmin)

class EntrenamientoAdmin(admin.ModelAdmin):
      list_display = ('id', 'titulo', 'subtitulo')
admin.site.register(Entrenamiento, EntrenamientoAdmin)

class OtrosAdmin(admin.ModelAdmin):
      list_display = ('id', 'titulo', 'subtitulo')
admin.site.register(Otros, OtrosAdmin)

class ConsejosAdmin(admin.ModelAdmin):
      list_display = ('id', 'titulo', 'subtitulo')
admin.site.register(Consejos, ConsejosAdmin)

# ------ MASCOTAS ------- #

class PerroAdmin(admin.ModelAdmin):
      list_display = ('id', 'nombre', 'tipo')
      search_fields = ['tipo', 'nombre']
admin.site.register(perro, PerroAdmin)

class GatoAdmin(admin.ModelAdmin):
      list_display = ('id', 'nombre', 'tipo')
      search_fields = ['tipo', 'nombre']
admin.site.register(gato, GatoAdmin)

class CaballoAdmin(admin.ModelAdmin):
      list_display = ('id', 'nombre', 'tipo')
      search_fields = ['tipo', 'nombre']
admin.site.register(caballo, CaballoAdmin)

class PecesAdmin(admin.ModelAdmin):
      list_display = ('id', 'nombre', 'tipo')
      search_fields = ['tipo', 'nombre']
admin.site.register(peces, PecesAdmin)

class PajaroAdmin(admin.ModelAdmin):
      list_display = ('id', 'nombre', 'tipo')
      search_fields = ['tipo', 'nombre']
admin.site.register(pajaro, PajaroAdmin)
