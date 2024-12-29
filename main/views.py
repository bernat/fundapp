from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'main/home.html', {
        'title': 'Welcome to My Fund App'
    })
