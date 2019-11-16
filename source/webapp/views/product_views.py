from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductIndexView(ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'
    model = Product
    ordering = []


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product

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


class ProductCreateView(PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'products/product_create.html'
    permission_required = 'webapp.add_product'
    permission_denied_message = '403 Access Denied!'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    context_object_name = 'product'
    permission_required = 'webapp.change_product'
    permission_denied_message = '403 Access Denied!'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'
    permission_denied_message = '403 Access Denied!'

