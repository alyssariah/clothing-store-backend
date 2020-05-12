from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    Product, CartItem, Order
)
from .serializers import (
    ProductSerializer, CartItemSerializer, CartFullSerializer, OrderSerializer, OrderFullSerializer
)
from django.contrib.postgres.search import SearchVector, SearchQuery


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    serializer_class = ProductSerializer
    def create(self, request):
        return super().create(request)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    def perform_create(self, serializer):
        serializer.save()

class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        # list  categories per current loggedin user
        queryset = CartItem.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = CartItemSerializer
    def create(self, request, *args, **kwargs):
        # check if category already exists for current logged in user
        return super().create(request)
    # user can only delete category he created
    def destroy(self, request, *args, **kwargs):
        category = CartItem.objects.get(pk=self.kwargs["pk"])
        if not request.user == category.owner:
            raise PermissionDenied("You can not delete this item")
        return super().destroy(request, *args, **kwargs)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CartExpandedViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        # list  categories per current loggedin user
        queryset = CartItem.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = CartFullSerializer

class CartItemEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = CartItem.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Order.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        category = CartItem.objects.get(pk=self.kwargs["pk"])
        if not request.user == category.owner:
            raise PermissionDenied("You can not delete this item")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Order.objects.filter(owner=self.request.user)
        return queryset
    serializer_class = OrderSerializer

class OrderExpandedViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        # list  categories per current loggedin user
        queryset = Order.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = OrderFullSerializer

class SearchDatabase(generics.ListAPIView):
    def get_queryset(self):
        search_term = self.request.GET.get('q',)
        queryset = Product.objects.annotate(search=SearchVector('name', 'category',),).filter(search=search_term)
        return queryset
    serializer_class = ProductSerializer
