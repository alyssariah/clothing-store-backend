from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartItemViewSet, CartExpandedViewSet, CartItemEdit, OrderViewSet, OrderDetails, OrderExpandedViewSet, SearchDatabase

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('items', CartItemViewSet, basename='items')
router.register('orders', OrderViewSet, basename='orders')

custom_urlpattern = [
    url(r'items-json/$', CartExpandedViewSet.as_view(), name='item-expand'),
    url(r'items/(?P<pk>\d+)/$', CartItemEdit.as_view(), name='item-edit'),
    url(r'orders-json/$', OrderExpandedViewSet.as_view(), name='order-expand'),
    url(r'orders/(?P<pk>\d+)/$', OrderDetails.as_view(), name='order-edit'),
    url(r'search/$', SearchDatabase.as_view(), name='search')
]
urlpatterns = router.urls
urlpatterns += custom_urlpattern