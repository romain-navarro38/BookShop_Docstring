from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from config.settings import MEDIA_URL, MEDIA_ROOT


def homepage(request):
    return render(request, 'base.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('compte/', include('account.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
