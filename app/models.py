from django.db import models

# Create your models here.
class Animal(models.Model):
	class Meta:
		verbose_name = 'Animal'
		verbose_name_plural = 'Animais'

	identificacao_unica = models.CharField(max_length=255, unique=True, verbose_name='Identificação única')
	nome = models.CharField(max_length=255, verbose_name='Nome')
	rfid = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='RFID')
	foto = models.ImageField(upload_to='bois/', null=True, blank=True, default='bois/default-boi.jpg', verbose_name='Foto')

	def __str__(self):
		return self.identificacao_unica