from django.shortcuts import render
from product.models import Product
from product.serializer import ProductSerializer, MessageSerializer
from . import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from product.test import Message
from rest_framework import status
from rest_framework import mixins,generics

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def listproducts(request):
    query=Product.objects.all()
    serializer_class= ProductSerializer(query,many=True)
    # context={
    #     'serializer_class_data':serializer_class.data
    # }
    return Response(serializer_class.data)

@api_view(['GET','POST'])
def listmessages(request):
    message_obj= Message('gollavenu1996@gmail.com','Hi hello ...')
    serializer_class= MessageSerializer(message_obj)
    return Response(serializer_class.data)



class ListProductc(APIView):
    
    def get(self,request):
        query=Product.objects.all()
        serializer_class=ProductSerializer(query,many=True)
        return Response(serializer_class.data)
    
    def post(self,request):
        serializer_obj=ProductSerializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved = serializer_obj.save()
            return Response({"Success": "Product {} is successfully created".format(product_saved.name)})
        return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class ProductDetailed(APIView):
    def get(self,request,pid):
        query=Product.objects.filter(product_id=pid)
        serializer_class=ProductSerializer(query,many=True)
        return Response(serializer_class.data)
    
    def put(self,request,pid):
        product_obj=Product.objects.get(product_id=pid)
        # print(product_obj)
        serializer_obj=ProductSerializer(product_obj,data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved=serializer_obj.save()
            return Response({"Success":"Product {} is updated successfully".format(product_saved.name)})
        return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request,pid):
        product_obj=Product.objects.get(product_id=pid)
        product_obj.delete()
        return Response(status=status.HTTP_200_OK)
    
    
class ListProductsMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class DetailedProductsMixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    
    
    
    
class ListProductsGeneric(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class DetailedProductsGeneric(generics.RetrieveAPIView,
                              generics.UpdateAPIView,
                              generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    