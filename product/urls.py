from django.urls import path,include
from product.views import listproducts,listmessages,ListProductc,ProductDetailed,ListProductsMixins,DetailedProductsMixins,ListProductsGeneric,DetailedProductsGeneric
from product.views import ProductViewSet
from rest_framework.routers import DefaultRouter,SimpleRouter


# router=DefaultRouter()
router=SimpleRouter()
router.register('productviewset',ProductViewSet,basename='product')


urlpatterns = [
    path('productlist/',listproducts, name='productlist'),
    path('messagelist/',listmessages, name='messagelist'),
    path('classproductlist/',ListProductc.as_view(),name='classproductlist'),
    path('classdetailedproduct/<int:pid>/',ProductDetailed.as_view(),name='classdetailedproduct'),
    path('mixinpath/',ListProductsMixins.as_view(),name='mp'),
    path('productmixin/<int:pk>/',DetailedProductsMixins.as_view(),name='mdp'),
    path('productgenericlist/',ListProductsGeneric.as_view(),name='lpg'),
    path('productdetailgeneric/<int:pk>',DetailedProductsGeneric.as_view(),name='pdg')
]+router.urls
