from .models import Player, Paradigm, Programmer
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        #fields = ['id', 'url', 'name', 'paradigm']

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ['id', 'url', 'name']

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ['id', 'url', 'name', 'players']

