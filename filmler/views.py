from django.shortcuts import render
from .models import *
# Create your views here.
# Sayfayı görüntülemek için:
def index(request):
    filmler = Film.objects.all()
    context = {
        'filmler':filmler
    }
    return render(request, 'index.html', context)