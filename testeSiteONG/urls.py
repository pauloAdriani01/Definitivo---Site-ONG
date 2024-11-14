from homepageONG.views import homepageView, quemSomosView, oqueFazemosView, doacoesView, testeView, UploadImagemView, DeletarImagemView, CriacaoSuperUsuarioView, AreaAdmView,CarrosselView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homepageView.as_view(template_name='homepage.html'), name='homepage'),
    path('quemSomos', quemSomosView.as_view(template_name='quemSomos.html'), name='quemSomos'),
    path('oqueFazemos', oqueFazemosView.as_view(template_name='oqueFazemos.html'), name='oqueFazemos'),
    path('doacoes', doacoesView.as_view(template_name='doacoes.html'), name='doacoes'),
    path('teste', testeView.as_view(template_name='teste.html'), name='teste'),
    path('admin/', AreaAdmView.as_view(), name='AreaAdm'),
    path('admin/upload/', UploadImagemView.as_view(), name='UploadImagem'),
    path('imagens/deletar/<int:pk>/', DeletarImagemView.as_view(), name='DeletarImagem'),
    path('admin/criarsuperusuario/', CriacaoSuperUsuarioView.as_view(), name='CriacaoSuperUsuario'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('carrossel/', CarrosselView.as_view(), name='carrossel'),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
