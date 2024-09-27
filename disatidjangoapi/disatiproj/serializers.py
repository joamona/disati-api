from rest_framework import serializers
from .models import PaisesIberoamerica, CatastrosIberoamerica, AppatMiembros, CpciMiembros, CpciObservadores, DatosEncuesta

class PaisesIberoamericaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaisesIberoamerica
        fields = '__all__'

class CatastrosIberoamericaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatastrosIberoamerica
        fields = '__all__'

class AppatMiembrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppatMiembros
        fields = '__all__'

class CpciMiembrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpciMiembros
        fields = '__all__'

class CpciObservadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpciObservadores
        fields = '__all__'

class DatosEncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosEncuesta
        fields = '__all__'