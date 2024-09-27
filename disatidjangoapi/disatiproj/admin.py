from django.contrib import admin
from .models import PaisesIberoamerica, CatastrosIberoamerica, AppatMiembros, CpciMiembros, CpciObservadores, DatosEncuesta

# Register your models here.
admin.site.register(PaisesIberoamerica)
admin.site.register(CatastrosIberoamerica)
admin.site.register(AppatMiembros)
admin.site.register(CpciMiembros)
admin.site.register(CpciObservadores)
admin.site.register(DatosEncuesta)
