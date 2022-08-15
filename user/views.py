from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import models, MyRegister
from .forms import MyForm
from datetime import datetime


# Create your views here.


def home(request):
    return render(request, 'home.html')


# def register(request):
#     return render(request, 'register.html')
@csrf_exempt
def register(request):
    print(request.method)
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            foo = MyRegister(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                phonenumber=form.cleaned_data['phonenumber'],
                address1=form.cleaned_data['address1'],
                address2=form.cleaned_data['address2'],
                city=form.city['city'],
                zipcode=form.zipcode['zipcode'],
                file="test"
            )
            foo.save()
            print("File Saved")
        else:
            return render(request, 'register.html', {'forms': form, 'error': 'Bad data entry.'})
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


