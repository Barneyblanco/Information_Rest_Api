from rest_framework import serializers
from .models import category, seller, product, order

class categoryserializer(serializers.ModelSerializer):
	class Meta:
		model = category
		fields = '__all__'

class sellerserializer(serializers.ModelSerializer):
	class Meta:
		model = seller
		fields = '__all__'

class productserializer(serializers.ModelSerializer):
	class Meta:
		model = product
		fields = '__all__'

class orderserializer(serializers.ModelSerializer):
	class Meta:
		model = order
		fields = '__all__'