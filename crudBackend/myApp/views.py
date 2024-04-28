from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.views import APIView
from . import serializers
from . import models
# Create your views here.


class myViews(APIView):
    def post(self, request):
        data=request.data
        print(data)
        srl=serializers.mySerializer(data=data)
        if srl.is_valid():
            srl.save()
            return Response({
                'status':True,
                'msg':"Successfully created client"
            })
        else:
            return Response({
                'status':400,
                'msg':"An Error occured while creating client",
                "Error":srl.errors
            })
    
    def get(self, request):
        data=models.Clients.objects.all()
        srl=serializers.mySerializer(data, many=True)
        return Response(srl.data)
    
    def patch(self, request):
        data=request.data
        obj=models.Clients.objects.get(uid=data.get('uid'))
        srl=serializers.mySerializer(data=data, instance=obj)
        if srl.is_valid():
            srl.save()
            return Response({
                'status':True,
                'msg':"Successfully updated client"
            })
        else:
            return Response({
                'status':400,
                'msg':"An Error occured while creating client",
                "Error":srl.errors
            })
        
    def delete(self, request):
        obj=models.Clients.objects.get(uid=request.data.get('uid'))
        # srl=serializers.mySerializer(instance=obj)
        obj.delete()
        return Response({
            'status':True,
            'msg':"Successfully deleted client"
        })