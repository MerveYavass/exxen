# Hata mesajlarını verebilmek için: ,redirect ekledim
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Hata mesajlarını verebilmek için:
from django.contrib import messages 
# login için:
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre1 == sifre2:
            # Kullanıcı adı kullanımda mı ? 
            if User.objects.filter(username = kullanici).exists():
                messages.error(request, 'Kullanıcı İsmi Mevcut')
                return redirect('register')
            # Email kullanımda mı ? 
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email Kullanımda')
                return redirect('register')
            # Şifre karakter sayısı kontrolü
            elif len(sifre1) < 6:
                messages.error(request, 'Şifrenin en az 6 karakterli olması gerekir')
                return redirect('register')
            # Şifre de boşluk olmasın kontrolü
            elif " " in sifre1:
                messages.error(request, 'Şifrede boşluk bırakılamaz')
                return redirect('register')
            # Kullanıcı kaydetme işlemi
            else:
                user = User.objects.create_user(username = kullanici, email = email, password = sifre1)
                user.save()
                messages.success(request, 'Kullanıcı Oluşturuldu')
                return redirect('index')
    # Şifreler eşit değilse:
        else:
            messages.error(request, 'Şifreler Uyuşmuyor')
            return redirect('register')
    return render(request, 'register.html')
# SON

# Login Fonksiyonu:
def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST.get('kullanici')
        sifre = request.POST.get('sifre')

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
    return render(request, 'login.html')    
# SON