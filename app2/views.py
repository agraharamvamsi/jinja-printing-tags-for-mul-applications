from django.shortcuts import render

# Create your views here.
def second(request):
    d={'subject':'django','trainer':'Harshadvali'}
    return render(request,'second.html',d)