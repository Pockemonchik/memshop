from django import forms
from profiles.models import UserProfile
from shop.models import mem
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
class MemForm(forms.ModelForm):
    mem_img = forms.ImageField(required=False)
    class Meta:
        model=mem
        fields=('mem_img','disctiption','cost','category','available')
class ProfileForm(forms.ModelForm):
     user_picture=forms.ImageField(required=False)
     class Meta:
         model=UserProfile
         fields=('user_picture',)
