from django.db import models

class Imagem(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')
    context_object_name = 'imagens'
    
    def __str__(self):
        return self.titulo
