from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ('Acao','Acao'),
    ('Aventura','Aventura'),
    ('Comedia','Comedia'),
    ('Documentario','Documentario'),
    ('Drama','Drama'),
    ('FiccaoCientifica','FiccaoCientifica'),
    ('Musical','Musical'),
    ('Romance','Romance'),
    ('Suspense','Suspense'),
    ('Outros','Outros'),
)
#criar filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumbFilmes')
    descricao = models.TextField(max_length=2000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    dataCriacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

#criar episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + ' - ' + self.titulo


class Usuario(AbstractUser):
    filmesVisto = models.ManyToManyField("Filme")