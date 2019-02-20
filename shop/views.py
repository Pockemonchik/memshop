from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from shop.models import mem,Category
from cart.forms import CartAddmemForm
from django.db.models import Q
from .forms import Filterform
def List_shop(request,category_slug=None,question=None):
    category=None
    categories=Category.objects.all()
    mems=mem.objects.filter(available=True)
    #поиск по категориям
    if category_slug and not question:
        category=get_object_or_404(Category, slug=category_slug)
        mems=mems.filter(category=category)
    #поиск по описанию
    question = request.GET.get('q')
    if not category_slug and question:
        mems = mem.objects.filter(Q(disctiption__icontains=question))
    #форма корзины
    cart_mem_form = CartAddmemForm()
    #форма фильтра по цене

    if request.method=="POST":
        filter=Filterform(request.POST)
        p1=request.POST.get('p1')
        p2=request.POST.get('p2')
        price_filter=request.POST.get('price')
        print(p1,p2)
        if price_filter=='1':
            mems=mem.objects.filter(Q(cost__gte=p1)&Q(cost__lte=p2)).order_by('cost')
        else:
            mems=mem.objects.filter(Q(cost__gte=p1)&Q(cost__lte=p2)).order_by('-cost')


    else:
        filter=Filterform()

    return render(request , 'shop/mems.html',
    {
    'filter':filter,
    'mems':mems,
    'category':category,
    'categories':categories,
    'cart_mem_form': cart_mem_form
    })

#     return redirect('List_shop',question)
