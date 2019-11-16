from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

OTHER = 'other'
CATEGORY_CHOICES = [(OTHER, 'other'), ('clothing', 'Clothing'), ('electronics', 'Electronics'), ('food', 'Food'),
                    ('household', 'Household')]


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Product Name')
    category = models.CharField(max_length=40, null=False, blank=False, verbose_name='Category', default=OTHER,
                                choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    image = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Product Image')

    def __str__(self):
        return self.name

    def average(self):
        average = self.reviews.aggregate(Avg('rating'))
        return average['rating__avg']


class Review(models.Model):
    author = models.ForeignKey(User, null=True, blank=False, default=None, verbose_name='Author',
                               on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Project',
                                related_name='reviews')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Text')
    rating = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                 verbose_name='rating')

    def __str__(self):
        return 'Review of {} by {}'.format(self.product, self.author)

