"""mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mooc.accounts import urls as accounts_urls
from mooc.core import urls as core_urls
from mooc.courses import urls as courses_urls
from mooc.forum import urls as forum_urls

urlpatterns = [
    path(r'',
         include(
             (core_urls, 'core'),
             namespace='core')
         ),
    path(r'cursos/',
         include(
             (courses_urls, 'courses'),
             namespace='courses')
         ),
    path(r'conta/',
         include(
             (accounts_urls, 'accounts'),
             namespace='accounts')
         ),
    path(r'forum/',
         include(
             (forum_urls, 'forum'),
             namespace='forum')
         ),
    path(r'admin/',
         admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
