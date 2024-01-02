from django.shortcuts import render
from . import models
from . import forms
import datetime
# Create your views here.

def index(request):
    data_music=models.music.objects.all
    data_site=models.music.objects.all
    form_reg=forms.registerform(request.POST)
    if request.method == "POST":
        if form_reg.is_valid():

            letters=models.inbox()
            letters.name=form_reg.cleaned_data['name']
            letters.email=form_reg.cleaned_data['email']
            letters.user_message=form_reg.cleaned_data['message']
            letters.date=datetime.datetime.now()
            letters.save()
    return render(request,'index.html',context={"music":data_music,'site':data_site,"form":form_reg})