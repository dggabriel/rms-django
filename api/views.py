from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rmsmodel.models import AssetClasses
from .serializers import AssetClassesSerializer
# Create your views here.
@api_view(['GET'])
def getAssetClasses(request):
    asset_classes = AssetClasses.objects.all()
    serializer = AssetClassesSerializer(asset_classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postAssetClasses(request):
    serializer = AssetClassesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
