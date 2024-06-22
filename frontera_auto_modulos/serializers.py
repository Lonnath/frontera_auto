from rest_framework import serializers
from .models import *


class PesajeSubproductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PesajeSubproducto
        fields = '__all__'


class ViceraSerializer(serializers.ModelSerializer):
    pesaje_subproductos = PesajeSubproductoSerializer(
        many=True, read_only=True, source='pesajesubproducto_set')

    class Meta:
        model = Vicera
        fields = '__all__'
        extra_fields = ['pesaje_subproductos']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['pesaje_subproductos'] = PesajeSubproductoSerializer(
            instance.pesajesubproducto_set.all(), many=True).data
        return ret


class DecomisoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Decomiso
        fields = '__all__'
    
    def to_representation(self, instance):
        return super().to_representation(instance)
