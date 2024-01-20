from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer


class CustomerList(APIView):
    def get(self, request):
        users = Customer.objects.all()
        serializer = CustomerSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
             raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomerSerializer(user)
        return Response(serializer.data)
