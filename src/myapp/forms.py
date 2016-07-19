from django import forms

from .models import Libro


class LibroModelForm(forms.ModelForm):
	titulo = forms.CharField(widget=forms.Textarea(
		attrs={
			"placeholder": "Como se llama el libro?",
	}))

	class Meta:
		model = Libro
		fields = ["titulo", "autor", "precio"]