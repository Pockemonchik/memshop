from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from shop.models import mem,Category
from cart.forms import CartAddmemForm
def List_shop(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    mems=mem.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        mems=mems.filter(category=category)
    cart_mem_form = CartAddmemForm()
    return render(request , 'shop/mems.html',
    {
    'mems':mems,
    'category':category,
    'categories':categories,
    'cart_mem_form': cart_mem_form
    })
