from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect

def index(request):
    contactform = ContactForm()
    if request.method == 'POST':
        return render(request, 'success.html')
    else:
        return render(request, 'index.html', {'myform': contactform})

def success(request):
    return render(request, 'success.html')