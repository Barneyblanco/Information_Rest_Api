from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import category, seller, product, order
from .serializers import categoryserializer, sellerserializer, productserializer, orderserializer


class categoryList(APIView):
	def get(self, request):
		categorys = category.objects.all()
		serializer = categoryserializer(categorys, many=True)
		return Response(serializer.data)

	
class sellerList(APIView):
	def get(self, request):
		sellers = seller.objects.all()
		serializer = sellerserializer(sellers, many=True)
		return Response(serializer.data)


class productList(APIView):
	def get(self, request):
		products = product.objects.all()
		serializer = productserializer(products, many=True)
		return Response(serializer.data)


class orderList(APIView):
	def get(self, request):
		orders = order.objects.all()
		serializer = orderserializer(orders, many=True)
		return Response(serializer.data)