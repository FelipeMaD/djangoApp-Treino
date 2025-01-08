from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Mundo")


def carrinho(request):
    carrinho = []
    for i in range(3):
        carrinho.append(f"Item{i}")
    return HttpResponse(f"Seu carrinho de compras contém os itens: {carrinho}")

def sobreNos(request):
    return HttpResponse("Página focada treinar conceitos http e django")

