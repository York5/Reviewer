from django import forms
from django.contrib.auth.models import User
from webapp.models import Product, Review


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'product']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = []
