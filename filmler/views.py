from django.shortcuts import render, redirect
from .models import *
# Create your views here.
# Sayfayı görüntülemek için:
def index(request):
    filmler = Film.objects.all()
    context = {
        'filmler':filmler
    }
    return render(request, 'index.html', context)

def view_404(request, exception):
    return redirect('/')