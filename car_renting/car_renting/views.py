from django.shortcuts import render,redirect

def homepage(request):
    return render(request,'homepage.html')

def search(request):
    return render(request,'search.html')

def searchresult(request):
    return render(request,'searchresult.html')

def carinfo(request):
    return render(request,'carinfo.html')