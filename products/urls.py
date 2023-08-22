from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('<int:product_id>', views.products_details, name='details')
]
