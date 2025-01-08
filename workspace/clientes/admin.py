from django.contrib import admin
from clientes.models import Cliente
from .models import Contato

admin.site.register(Cliente)
admin.site.register(Contato)