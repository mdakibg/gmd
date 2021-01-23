from django.shortcuts import render
from django.http import request
from .models import Project

# Create your views here.
def index(request):
    CATEGORY_CHOICES = [
        'Flooring & Staircase',
        'Carving',
        'Home & Garden Decor',
        'Inlay',
        'Home Mandir',
        'Wall Cladding',
        'Qibla & Mimbar',
        'Jali',
        'Katera & Kabr',
        'Railing',
        'Name Plate',
    ]

    results = list()

    for category in CATEGORY_CHOICES:
        results.append({
            'first': Project.objects.get(tag=0.0, category=category),
            'projects': Project.objects.all().filter(category=category).exclude(tag=0.0).order_by('tag')
        })

    return render(request, 'info/index.html', {
        'results': results
    })