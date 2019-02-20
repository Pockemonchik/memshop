from django import forms

class Filterform(forms.Form):
    CHOICES=[('1','По возрастанию'),('2','По убыванию')]
    price= forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    p1=forms.IntegerField(initial=0)
    p2=forms.IntegerField(initial=1000)
