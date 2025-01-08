"""
URL configuration for treinoFerias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import re_path
from .views import home, carrinho, sobreNos
from clientes.views import clientes, cliente_detail, cliente_por_nome

urlpatterns = [
    re_path(r'^$', home),
    re_path(r'^clientes/$', clientes),

    # nessa url abaixo, utiliza-se regex da seguinte forma: 
    # apos determinar cliente em: cliente/, define que o id do cliente será um parametro chamado id em: 
    # /(?P) dizendo q será um parametro
    # <id> dizendo que se chamará id
    # depois, temos que passar o tipo do id e o tamanho dele em: \d{1,3} -> inteiro, podendo ter 1 até 3 casas (1-999)
    # por fim, fecha a barra e encerra com dolar. então, de regex, temos: /(?P<id>\d{1,3})/

    re_path(r'^cliente/(?P<id>\d{1,3})/$' , cliente_detail),

    # se eu quiser ids de qualquer tamanho, coloco + ao inves de {1,3} depois de \d

    re_path(r'^cliente/(?P<nome>\w+)/$' , cliente_por_nome),

    re_path(r'^carrinho/$', carrinho),
    re_path(r'^sobre/$', sobreNos),
    re_path(r'^admin/', admin.site.urls),
    
]
