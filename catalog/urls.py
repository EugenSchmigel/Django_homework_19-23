
from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from catalog.views import IndexView, CategoryCatalogListView, ProductListView, CategoryListView, ProductDetailView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/', ProductListView.as_view() , name='product_list'),
    path('<int:pk>/product/', CategoryCatalogListView.as_view(), name='category_catalog'),

    #path('product/view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('product/view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]

