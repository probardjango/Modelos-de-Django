from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

from django.conf import settings

# Create your models here.
class Libro(models.Model):
	titulo = models.CharField(max_length=120)
	autor = models.CharField(max_length=120)
	slug = models.SlugField(null=True, blank=True)
	precio = models.DecimalField(default=9.99, max_digits=5, decimal_places=2)
	fecha_publicado = models.DateField(null=True, blank=True)
	superventa = models.BooleanField(default=False)
	agregado_por = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")

	def __unicode__(self): #Python 3 __str__
		return self.titulo


	def get_absolute_url(self):
		# return "/detail/%s/" %(self.pk)
		url_name = detail
		return reverse(url_name, kwargs={"pk":self.id})


def libro_pre_save_receptor(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = slugify(instance.titulo)

pre_save.connect(libro_pre_save_receptor, sender=Libro)


def libro_post_save_receptor(sender, instance, created, *args, **kwargs):
	if created:
		if not instance.slug:
			instance.slug = slugify(instance.titulo)
			instance.save()

post_save.connect(libro_post_save_receptor, sender=Libro)





