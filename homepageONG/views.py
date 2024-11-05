from django.views.generic import TemplateView

class homepageView(TemplateView):
    template_name = 'homepage.html'

class quemSomosView(TemplateView):
    template_name = 'quemSomos.html'

class oqueFazemosView(TemplateView):
    template_name = 'oqueFazemos.html'

class doacoesView(TemplateView):
    template_name = 'doacoes.html'
    
