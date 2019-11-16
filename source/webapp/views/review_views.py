from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ProductReviewForm
from webapp.models import Review, Product


class ReviewForProductCreateView(CreateView):
    model = Review
    template_name = 'reviews/create.html'
    form_class = ProductReviewForm

    def dispatch(self, request, *args, **kwargs):
        self.product = self.get_product()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.product = self.get_product()
        self.object = self.product.reviews.create(
            **form.cleaned_data
        )
        self.object.author = self.request.user
        self.object.save()
        return redirect('webapp:product_view', pk=self.product.pk)

    def get_product(self):
        product_pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=product_pk)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reviews/update.html'
    form_class = ProductReviewForm
    context_object_name = 'review'
    permission_required = 'webapp.change_review'
    permission_denied_message = '403 Access Denied!'

    def test_func(self):
        self.object= self.get_review()
        return self.request.user.has_perm('accounts.changer_review') or self.request.user.pk == self.object.author.pk

    def get_review(self):
        review_pk = self.kwargs.get('pk')
        review = get_object_or_404(Review, pk=review_pk)
        return review

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_review'
    permission_denied_message = '403 Access Denied!'
