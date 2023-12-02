from django.shortcuts import render

def meal(request):
    return render(request, 'base.html')

