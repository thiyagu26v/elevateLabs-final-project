from django.urls import path
from .views import ProductListView, RecommendationView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('recommend/', RecommendationView.as_view(), name='recommend'),
]
