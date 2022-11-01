from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def homepage(request):
    return render(request, 'base.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('compte/', include('account.urls')),
]
