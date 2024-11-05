from django.urls import path
from .views import MyTemplateView

urlpatterns = [
    path('', MyTemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('quemSomos', MyTemplateView.as_view(template_name='quemSomos.html'), name='quemSomos'),
    path('oqueFazemos', MyTemplateView.as_view(template_name='oqueFazemos.html'), name='oqueFazemos'),
    path('doacoes', MyTemplateView.as_view(template_name='doacoes.html'), name='doacoes')
]