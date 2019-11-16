from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from webapp.models import Product


class ProductIndexView(ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'
    model = Product
    ordering = []


class ProductView(PermissionRequiredMixin, DetailView):
    template_name = 'products/product.html'
    model = Product
    permission_required = 'webapp.view_product'
    permission_denied_message = '403 Access Denied!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        reviews = product.reviews.all()
        paginator = Paginator(reviews, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['reviews'] = page.object_list
        context['is_paginated'] = page.has_other_pages()
        return context
