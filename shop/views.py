from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from shop.models import mem,Category
from cart.forms import CartAddmemForm
from django.db.models import Q
from .forms import Filterform
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
    u=[]
    lmem=[]
    for memos in mems:
        u=User.objects.filter(likes=memos)
        if request.user in u:
            lmem.append(memos.id)

    if u==None:
        print('1')
    else:
        print("2")
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
    'cart_mem_form': cart_mem_form,
    'lmem':lmem
    })
@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        id= request.POST.get('id', None)
        mem_like = get_object_or_404(mem, id=id)
        print(user)
        print(id)
        print("You disliked this")

        if mem_like.likes.filter(id=user.id).exists():
            # user has already liked this mem
            # remove like/user
            mem_like.likes.remove(user)
            message = 'You disliked this'
            print("You disliked this")
        else:
            # add a new like for a mem
            mem_like.likes.add(user)
            message = 'You liked this'
            print("You liked this")

    ctx = {'likes_count': mem_like.total_likes(), 'message': message}
    print(ctx)
    # use mimetype instead of content_type if django < 5
    return HttpResponse(json.dumps(ctx), content_type='application/json')
#     return redirect('List_shop',question)
