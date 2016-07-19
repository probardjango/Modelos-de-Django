from django.shortcuts import render

# Create your views here.
def detail_view(request, pk=None):
	return render(request, "detail.html", {})