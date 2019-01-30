from django.shortcuts import render
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from shop.models import mem
from profiles.forms import MemForm,ProfileForm

def detail_profile(request,slug):
    profile=get_object_or_404(UserProfile,user__username=slug)
    mems=mem.objects.filter(author__username=profile.user.username)
    print(profile.user_id)
    if request.method=="POST":
        form=MemForm(request.POST,request.FILES)
        if form.is_valid():
            new_mem=form.save(commit=False)
            new_mem.author=profile.user
            new_mem.save()
        profileForm=ProfileForm(request.POST,request.FILES)
        if profileForm.is_valid():
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



# Create your views here.
