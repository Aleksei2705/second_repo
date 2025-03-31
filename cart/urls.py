from django.urls import path
from .views import add_to_cart
from .views import cart_view, update_cart, remove_from_cart

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', cart_view, name='cart_view'),  # Страница корзины
    path('update/<int:product_id>/', update_cart, name='update_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
