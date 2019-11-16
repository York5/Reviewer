from django.views.generic import ListView

from webapp.models import Product


class ProductIndexView(ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'
    model = Product
    ordering = []
