from django.urls import path
from miMascotasorgApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('servicios', views.servicios, name="servicios"),
    path('servicios/<str:tipo>', views.tipoServicio, name="tipo-servicio"),
    path('servicios/<str:tipo>/<int:id>', views.detalleServicio, name="detalle-servicio"),
    path('mascotas', views.mascotas, name="mascotas"),
    path('mascotas/<str:tipo>', views.tipoMascotas, name="tipo-mascotas"),
    path('consejos/<int:id>', views.detalleConsejo, name="detalle-consejo"),
    path('consejos', views.consejos, name="consejos"),
    path('contacto', views.contacto, name="contacto"), 
]

handler404 = "miMascotasorgApp.views.error_404"
handler500 = "miMascotasorgApp.views.error_500"

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)