from django.urls import path,include
from kioskoapp import views 
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('agregar_perfil/',views.agregar_perfil, name='agregar_perfil'),
    path('agregar_tag/',views.agregar_tag, name='agregar_tag'),
]
