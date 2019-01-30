from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import mem as Mem
from profiles.models import UserProfile
from .cart import Cart
from .forms import CartAddmemForm

#добавление элемента в корзину
@require_POST
def cart_add(request, mem_id):
    cart = Cart(request)
    mem = get_object_or_404(Mem, id=mem_id)
    form = CartAddmemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(mem=mem,
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')
#удаление элемента корзины
def cart_remove(request, mem_id):
    cart = Cart(request)
    mem = get_object_or_404(Mem, id=mem_id)
    cart.remove(mem)
    return redirect('cart:cart_detail')
# корзина
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
#обработка заказа и измеение можелей
def order(request):
    cart = Cart(request)
    print(cart.get_total_cost)
    client1=request.user
    client=UserProfile.objects.get(user__username=client1.username)
    print(cart)
    print(client.user_balance)
    # total_cost=int(str(cart.get_total_cost))
    if client.user_balance>=cart.get_total_cost():
        mem_ids = cart.get_keys()
        mems=Mem.objects.filter(id__in=mem_ids)
        for mem in mems:
            mem.author=client1
            mem.save()
        cart.clear()
    return render(request, 'cart/detail.html', {'cart': cart})
