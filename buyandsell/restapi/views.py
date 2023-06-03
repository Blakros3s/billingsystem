from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app_buyer.models import *
from app_seller.models import *
from .serializers import *

class OrderList(APIView):
    def get(self, request):
        orders = Purchase.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    def get_object(self, id):
        try:
            return Purchase.objects.get(id=id)
        except Purchase.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        order = self.get_object(id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        order = self.get_object(id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        order = self.get_object(id)
        order.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)



class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)
    


class BillList(APIView):
    def get(self, request):
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillDetail(APIView):
    def get_object(self, id):
        try:
            return Bill.objects.get(id=id)
        except Bill.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        bill = self.get_object(id)
        serializer = BillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        bill = self.get_object(id)
        serializer = BillSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        bill = self.get_object(id)
        bill.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)