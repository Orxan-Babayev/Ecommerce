from django.shortcuts import render

def cart(request):
    return render(request, 'product-cart.html')

def checkout(request):
    return render(request, 'product-checkout.html')

def wishlist(request):
    return render(request, 'user-wishlist.html')
