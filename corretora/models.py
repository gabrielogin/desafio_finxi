from django.db import models
from django.utils import timezone


class Imovel(models.Model):
    author = models.ForeignKey('auth.User')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    TIPOS = (
		('al', 'Aluguel'),
		('cp', 'Casa Própria'),
	)
    imovel = models.CharField(
		max_length=2,
		choices=TIPOS,
		default='al',
	)
    endereco = models.CharField(max_length=350)
    cidade = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    valor = models.IntegerField()
    imagem = models.ImageField(upload_to = 'uploads/')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
