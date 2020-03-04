'''
A serializer class is very similar to a Django Form class, 
and includes similar validation flags on the various fields, 
such as required, max_length and default.
Serializer class 與 Django Form class 非常相似，
並且在各個字段上都包含類似的驗證標誌，例如 required ， max_length 和 default。
'''
from .models import Patient
from rest_framework import serializers


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        #fields = ['id', 'name', 'sbp_raw', 'dbp_raw', 'hr_raw']
        fields = '__all__'