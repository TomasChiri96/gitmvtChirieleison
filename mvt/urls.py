"""mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mvt1.views import familia, familia1, familia2, perro1, perro2, plantilla_madre, plantilla_padre, plantilla_sister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('padre_familia/', familia ),
    path('madre_familia/',familia1),
    path('sister_familia/',familia2),
    path('plantilla_madre/', plantilla_madre),
    path('plantilla_padre/', plantilla_padre ),
    path('plantilla_sister/', plantilla_sister)
]
