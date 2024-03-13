from rest_framework import serializers 

from .models import Category, Product, File 



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Category 
        fields = ['title','description','avatar']
        
        

class FileSerializer(serializers.ModelSerializer):
    
    file_type = serializers.SerializerMethodField()
    
    class Meta:
        
        model = File
        fildes = ['id','title','file','file_type']
        
        

class ProductSerializer(serializers.ModelSerializer):
    
    categories = CategorySerializer(many=True)
    
    
    class Meta:
        
        model = Product 
        fields = ['pk','title','description','avatar','categories']