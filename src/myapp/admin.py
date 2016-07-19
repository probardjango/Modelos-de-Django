from django.contrib import admin

# Register your models here.
from .forms import LibroModelForm
from .models import Libro


class LibroModelAdmin(admin.ModelAdmin):
	form = LibroModelForm
	list_display = ["titulo", "autor", "precio", "superventa"]
	search_fields = ["autor", "titulo"]
	list_filter = ["precio"]
	list_editable = ["precio"]


admin.site.register(Libro, LibroModelAdmin)