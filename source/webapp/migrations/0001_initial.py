# Generated by Django 2.2 on 2019-11-16 07:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('category', models.CharField(choices=[('other', 'other'), ('clothing', 'Clothing'), ('electronics', 'Electronics'), ('food', 'Food'), ('household', 'Household')], default='other', max_length=40, verbose_name='Category')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_pics', verbose_name='Product Image')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, verbose_name='Text')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='rating')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='webapp.Product', verbose_name='Project')),
            ],
        ),
    ]
