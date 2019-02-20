from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from shop.models import mem
from profiles.forms import MemForm,ProfileForm

def detail_profile(request,slug):
    profile=get_object_or_404(UserProfile,user__username=slug)
    mems=mem.objects.filter(author=profile)
    print(profile.user_id)
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
