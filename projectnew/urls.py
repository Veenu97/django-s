"""
URL configuration for projectnew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from newapp import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro',views.content),
    path('add',views.content1),
    path('subtract',views.content2),
    path('multiply',views.content3),
    path('division',views.content4),
    path('cube',views.content5),
    path('cuboid',views.content6),
    path('rectangle',views.content7),
    path('square',views.content8),
    path('arearec',views.content9),
    path('areasquare',views.content10),
    path('appp',views.new),
    path('r1',views.sume),
    path('ddtt',views.dt),
    path('home',views.h1),
    path('about',views.a1),
    path('form',views.form),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)