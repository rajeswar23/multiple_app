from django.shortcuts import render

# Create your views here.
def mowa(request):
    return render(request,'mowa.html')
def mummy(request):
    return render(request,'mummy.html')