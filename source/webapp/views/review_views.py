from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

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

    class ReviewUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    template_name = 'reviews/update.html'
    form_class = IssueForm
    context_object_name = 'issue'
    permission_required = 'webapp.change_issue'
    permission_denied_message = '403 Access Denied!'

    def test_func(self):
        project_users = []
        for user in self.get_object().project.users.all():
            project_users.append(user)
        return self.request.user in project_users
