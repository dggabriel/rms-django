from rest_framework import serializers
from rmsmodel.models import AssetClasses
 
class AssetClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssetClasses
        fields=('asset_class_name','asset_class_description')
