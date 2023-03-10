"""exxen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

#index sayfasına süslü parantezler içinde film resimlerini yazmama rağmen döngüye girmedi onun için eklediğim şeyler:
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from filmler.views import *
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('filmler.urls')),
    path('kullanici/', include('kullanici.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#index sayfasına süslü parantezler içinde film resimlerini yazmama rağmen döngüye girmedi onun için eklediğim şeyler:
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

handler404 = 'filmler.views.view_404'