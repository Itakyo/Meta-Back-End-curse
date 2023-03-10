from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    #category = serializers.StringRelatedField()
    class Meta:
        model = MenuItem
        fields  = ['id','title','price','stock','price_after_tax']
        
    
        
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
        
    def validate(self, attrs):
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)