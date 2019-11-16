from django.urls import path
from webapp.views import ProductIndexView

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    ]

