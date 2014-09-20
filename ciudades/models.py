from django.db import models
from departamentos.models import Departamento
# Create your models here.

class Ciudad(models.Model):
	nombre = models.CharField(max_length = 140)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.nombre