'''
A serializer class is very similar to a Django Form class, 
and includes similar validation flags on the various fields, 
such as required, max_length and default.
Serializer class 與 Django Form class 非常相似，
並且在各個字段上都包含類似的驗證標誌，例如 required ， max_length 和 default。
'''
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

