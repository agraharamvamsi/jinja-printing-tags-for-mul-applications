from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'vignesh','age':'22'}
    return render(request,'first.html',d)
