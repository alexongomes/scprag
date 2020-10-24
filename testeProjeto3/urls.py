"""testeProjeto3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from scprag import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('alertas/', views.alertas),
    path('', views.index),

    path('loginscprag/', views.loginscprag),
    path('loginscprag/autentica', views.autentica_login),
    path('logout/', views.logoutscprag),

    path('clientes/', views.listaCliente),
    path('filtro_cliente/', views.listaCliente),
    path('cadastrar_cliente/', views.cadastrar_cliente),
    path('cadastrar_cliente/submit', views.submit_cliente),
    path('cadastrar_cliente/delete/<int:id_cliente>/', views.delete_cliente),

    path('cadastrar_local/delete/<int:id_cliente>/<int:id_local>/', views.delete_local),
    path('cadastrar_local/delete/<int:id_cliente>/<int:id_contato>/', views.delete_contato),

    path('funcionarios/', views.listaFuncionario),
    path('filtro_funcionario/', views.listaFuncionario),
    path('cadastrar_funcionario/', views.cadastrar_funcionario),
    path('cadastrar_funcionario/submit', views.submit_funcionario),
    path('cadastrar_funcionario/delete/<int:id_funcionario>/', views.delete_funcionario),

]
