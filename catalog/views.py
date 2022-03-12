from django.shortcuts import render

from .models import Pizza


def index(request):
    context = {
        'pizza': Pizza.objects.all()
    }
    return render(request, 'index.html', context=context)
# Create your views here.
