from django.utils import timezone

from .models import Category, Product, File
from subscriptions.models import Subscription

from .serializers import CategorySerializer, FileSerializer, ProductSerializer

from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated


# Create your views here.




class CategoryListView(APIView):
    
    def get(self,request):
    
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context = {'request': request})
        return Response(serializer.data, status = status.HTTP_200_OK)


class CategoryDetailView(APIView):
    
    def get(self,request,pk):
        
        try:
            category = Category.objects.get(pk=pk)
            
        except category.DoesNotExist:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CategorySerializer(category, context = {'request': request})
        
        return Response(serializer.data, status = status.HTTP_200_OK)
        
        
    
    




class ProductListView(APIView):
    
    def get(self,request):
        
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data, status= status.HTTP_200_OK)     


class ProductDetailView(APIView):
    
    def get(self,request,pk):
        
        permission_class = [IsAuthenticated]
        
        if not Subscription.objects.filter(
            user=request.user,
            expire_time__gt=timezone.now()
        ).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
        
            product = Product.objects.get(pk=pk)
        
        except product.DoesNotExist:
            
            return Response(status= status.HTTP_400_BAD_REQUEST)
            
        serializer = ProductSerializer(product, context = {'request': request})
        
        return Response(serializer.data, status= status.HTTP_200_OK)
        
                                  


# class FileListView(APIView):
    
#     def get()      



# class FileDetailView():
    
    
#     pass                       
