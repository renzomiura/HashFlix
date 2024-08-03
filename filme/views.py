from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarPerfilForm, HomepageForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def homepage(request):
#     return render(request,"homepage.html")

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = HomepageForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)

        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarperfil')
# def homefilmes(request):
#     context = {}
#     listaFilmes = Filme.objects.all()
#     context['listaFilmes'] = listaFilmes
#     return render(request,"homefilmes.html", context)

class Homefilmes(LoginRequiredMixin, ListView):
     template_name = "homefilmes.html"
     model = Filme

class Detalhesfilmes(LoginRequiredMixin, DetailView):
    template_name = "detalhefilmes.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes +=1
        filme.save()
        usuario = request.user
        usuario.filmesVisto.add(filme)
        return super(Detalhesfilmes, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)

        filmesRelacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:3]
        context['filmesRelacionados'] = filmesRelacionados
        return context

class Pesquisa(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termoPesquisa = self.request.GET.get('query')

        if termoPesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termoPesquisa)
            return object_list
        else:
            return None

class CriarPerfil(FormView):
    template_name = "criarperfil.html"
    form_class = CriarPerfilForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:login')
