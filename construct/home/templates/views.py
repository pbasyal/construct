from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def inner(request):
    return render(request, 'inner.html', {})

