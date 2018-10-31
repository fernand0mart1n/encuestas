from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class Pregunta(models.Model):
	texto_pregunta = models.CharField(max_length=200)
	fecha = models.DateTimeField('fecha de publicacion')
	
	def __str__(self):
		return self.texto_pregunta

	def fue_publicada_recientemente(self):
		return self.fecha >= timezone.now() - datetime.timedelta(days=1)

class Eleccion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	texto_eleccion = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)
	def __str__(self):
		return self.texto_eleccion