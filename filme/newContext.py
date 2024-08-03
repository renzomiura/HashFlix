from .models import Filme

def listaRecentes(request):
    listaFilmes = Filme.objects.all()
    filmesRecentes = listaFilmes.order_by('-dataCriacao')[0:10]

    return{'listaRecentes':filmesRecentes}

def listaPopular(request):
    listaFilmes = Filme.objects.all()
    filmesPopulares = listaFilmes.order_by('-visualizacoes')[0:10]

    return{'listaPopular':filmesPopulares}

def filmeDestaque(request):
    #filmeDestaque = Filme.objects.order_by('-dataCriacao')[0]
    listaFilmes = Filme.objects.all()
    filmesRecentes = listaFilmes.order_by('-dataCriacao')[0:10]

    if filmesRecentes:
        filmeDestaque = filmesRecentes[0]
    else:
        filmeDestaque = None

    return{'filmeDestaque':filmeDestaque}

#def listaVisto(request):
#    listaVisto = Usuario.objects.all()

#    return{'listaVisto':listaVisto}