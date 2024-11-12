from django.urls import path
from .views import homepageView, quemSomosView, oqueFazemosView, doacoesView, testeView

urlpatterns = [
    path('', homepageView.as_view(template_name='homepage.html'), name='homepage'),
    path('quemSomos', quemSomosView.as_view(template_name='quemSomos.html'), name='quemSomos'),
    path('oqueFazemos', oqueFazemosView.as_view(template_name='oqueFazemos.html'), name='oqueFazemos'),
    path('doacoes', doacoesView.as_view(template_name='doacoes.html'), name='doacoes'),
    path('teste', testeView.as_view(template_name='teste.html'), name='teste')
]