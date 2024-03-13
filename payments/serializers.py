from rest_framework import serializers 

from .models import Gateway, Payment 


class GatewaySerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Gateway 
        fields = ('title', 'description', 'avatar', 'is_enable')
        
        
        
    
# class PaymentSerializer(serializers.ModelSerializer):
    
#     class Meta:
        
#         model = Payment
#         fields = ('')