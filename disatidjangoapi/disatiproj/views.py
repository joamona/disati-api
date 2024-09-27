from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from rest_framework.response import Response
from .models import PaisesIberoamerica, CatastrosIberoamerica, AppatMiembros, CpciMiembros, CpciObservadores, DatosEncuesta
from .serializers import PaisesIberoamericaSerializer, CatastrosIberoamericaSerializer, AppatMiembrosSerializer, CpciMiembrosSerializer, CpciObservadoresSerializer, DatosEncuestaSerializer
from rest_framework import generics

class CatastrosIberoamericaList(generics.ListAPIView):
    serializer_class = CatastrosIberoamericaSerializer

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM geo_data.catastros_iberoamerica")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
        queryset = [CatastrosIberoamerica(**dict(zip(columns, row))) for row in rows]
        return queryset

class PaisesIberoamericaList(generics.ListAPIView):
    serializer_class = PaisesIberoamericaSerializer

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM geo_data.paises_iberoamerica")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
        queryset = [PaisesIberoamerica(**dict(zip(columns, row))) for row in rows]

        return queryset

class DataByPaisIdList(generics.GenericAPIView):
    def get(self, request, paisid, *args, **kwargs):
        appat_miembros_list = AppatMiembros.objects.filter(paisid=paisid)
        cpci_miembros_list = CpciMiembros.objects.filter(paisid=paisid)
        cpci_observadores_list = CpciObservadores.objects.filter(paisid=paisid)
        datos_encuesta_list = DatosEncuesta.objects.filter(paisid=paisid)

        appat_miembros_serializer = AppatMiembrosSerializer(appat_miembros_list, many=True)
        cpci_miembros_serializer = CpciMiembrosSerializer(cpci_miembros_list, many=True)
        cpci_observadores_serializer = CpciObservadoresSerializer(cpci_observadores_list, many=True)
        datos_encuesta_serializer = DatosEncuestaSerializer(datos_encuesta_list, many=True)

        respuesta = {
            'appat_miembros': appat_miembros_serializer.data,
            'cpci_miembros': cpci_miembros_serializer.data,
            'cpci_observadores': cpci_observadores_serializer.data,
            'datos_encuesta': datos_encuesta_serializer.data
        }

        return Response(respuesta)