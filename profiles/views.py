from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from shop.models import mem
from profiles.forms import MemForm,ProfileForm

def detail_profile(request,slug):
    profile=get_object_or_404(UserProfile,user__username=slug)
    mems=mem.objects.filter(author=profile)
    #считаем лайки
    likes_count=0;
    for memos in mems.iterator():
        likes_count+=memos.total_likes()
    print(likes_count)
    #считаем рейтинг
    pr=UserProfile.objects.order_by('user_balance')
    profile_index=0;
    for p in pr:
        profile_index+=1
        if p==profile:
            break
    rating=(profile_index/pr.count())*100

    print(rating)
    #обработка загрузки картинки
    if request.method=="POST":
        form=MemForm(request.POST,request.FILES)
        if form.is_valid():
            new_mem=form.save(commit=False)
            new_mem.author=profile
            new_mem.save()
        profileForm=ProfileForm(request.POST,request.FILES)
        if profileForm.has_changed():
            avatar=profileForm.save(commit=False)
            avatar.user=profile.user
            avatar.save()
    else:
        form=MemForm()
        profileForm=ProfileForm()


    return render(request, 'profiles/profiles.html',
{
'profile':profile,
'mems':mems,
'form':form,
'profileForm':profileForm,
'rating':rating
})

def add_to_shop(request,mem_id):
    mem_to_shop = get_object_or_404(mem, id=mem_id)
    mem_to_shop.available =True
    mem_to_shop.save(update_fields=['available'])
    return redirect('detail_profile',mem_to_shop.author)

def del_from_shop(request,mem_id):
    mem_to_shop = get_object_or_404(mem, id=mem_id)
    mem_to_shop.available =False
    mem_to_shop.save(update_fields=['available'])
    return redirect('detail_profile',mem_to_shop.author)



# Create your views here.
