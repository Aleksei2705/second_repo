from django.urls import path
from .views import product_list, product_detail, about_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),  # Обрати внимание на этот путь
    
]

