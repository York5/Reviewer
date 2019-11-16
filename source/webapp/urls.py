from django.urls import path
from webapp.views import ProductIndexView, ProductView, ReviewForProductCreateView, ProductUpdateView,\
    ProductDeleteView, ProductCreateView

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view'),
    path('project/<int:pk>/add-review/', ReviewForProductCreateView.as_view(), name='product_review_create'),
    path('project/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('project/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    ]

