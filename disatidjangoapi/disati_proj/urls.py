"""
URL configuration for disati_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from disatiproj.views import PaisesIberoamericaList, CatastrosIberoamericaList, DataByPaisIdList
from disatiproj import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('catastros_iberoamerica/', CatastrosIberoamericaList.as_view(), name='delegaciones-catastrales-list'),
    path('paises_iberoamerica/', PaisesIberoamericaList.as_view(), name='catastros-iberoamerica-list'),
    path('datos/<int:paisid>/', DataByPaisIdList.as_view(), name='data-by-pais-id'),
]
