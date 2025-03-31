from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from django.contrib import messages

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    messages.success(request, f'{product.name} добавлен в корзину!')
    return redirect('product_list')
def cart_view(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity
        })

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def update_cart(request, product_id):
    if request.method == "POST":
        new_quantity = int(request.POST.get("quantity", 1))
        cart = request.session.get('cart', {})

        if new_quantity > 0:
            cart[str(product_id)] = new_quantity
            messages.success(request, "Количество обновлено!")
        else:
            cart.pop(str(product_id), None)
            messages.success(request, "Товар удалён из корзины!")

        request.session['cart'] = cart
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart.pop(str(product_id), None)
        messages.success(request, "Товар удалён из корзины!")
    request.session['cart'] = cart
    return redirect('cart_view')
