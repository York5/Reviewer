from django.urls import path
from webapp.views import ProductIndexView, ProductView

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view')
    ]

