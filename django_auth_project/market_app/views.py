# from django.shortcuts import render

# from rest_framework import generics
# from market_app.models import Manufacturer, Product, ManufacturerUser
# from market_app.api.serializers import ManufacturerSerializer, ProductSerializer, ManufacturerUserSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# class ManufacturerList(generics.ListCreateAPIView):
#     queryset = Manufacturer.objects.all()
#     serializer_class = ManufacturerSerializer

# class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Manufacturer.objects.all()
#     serializer_class = ManufacturerSerializer

# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ManufacturerUserList(generics.ListCreateAPIView):
#     queryset = ManufacturerUser.objects.all()
#     serializer_class = ManufacturerUserSerializer

# class ManufacturerUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ManufacturerUser.objects.all()
#     serializer_class = ManufacturerUserSerializer

# class ManufacturerProductListCreate(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         manufacturer_id = self.kwargs['manufacturer_id']
#         return Product.objects.filter(manufacturer_id=manufacturer_id)
    
#     def perform_create(self, serializer):
#         manufacturer_id = self.kwargs['manufacturer_id']
#         serializer.save(manufacturer_id=manufacturer_id)