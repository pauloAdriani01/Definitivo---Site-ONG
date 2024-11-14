from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from .models import Imagem
from .forms import ImagemForm, CriacaoSuperUsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

class homepageView(TemplateView):
    template_name = 'homepage.html'

class quemSomosView(TemplateView):
    template_name = 'quemSomos.html'

class oqueFazemosView(TemplateView):
    template_name = 'oqueFazemos.html'

class doacoesView(TemplateView):
    template_name = 'doacoes.html'

class testeView(TemplateView):
    template_name = 'teste.html'
    
#View pra Upload de Imagem
class UploadImagemView(CreateView):
    model = Imagem
    form_class = ImagemForm
    template_name = 'UploadImagem.html'
    success_url = reverse_lazy('homepage')

    def test_func(self):
        return self.request.user.is_staff

class homepageView(ListView):
    model = Imagem
    template_name = 'homepage.html'
    context_object_name = 'imagens'

    def test_func(self):
        return self.request.user.is_staff

class DeletarImagemView(LoginRequiredMixin, View):
    def post(self, request, pk):
        # Verificar se o usuário é superusuário (admin)
        if not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão para excluir imagens.")
        
        imagem = get_object_or_404(Imagem, pk=pk)
        imagem.delete()
        return redirect('homepage')
    
class AreaAdmView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Imagem
    template_name = 'AreaAdm.html'
    context_object_name = 'imagens'
    fields = ['titulo', 'imagem']

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagens'] = Imagem.objects.all()
        return context

class CriacaoSuperUsuarioView(CreateView):
    form_class = CriacaoSuperUsuarioForm
    template_name = 'CriacaoSuperUsuario.html'
    success_url = reverse_lazy('AreaAdm')

class CarrosselView(ListView):
    model = Imagem
    template_name = 'homepage.html'
    context_object_name = 'imagens'  