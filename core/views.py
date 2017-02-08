from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	texts = [ 'Lorem ipsum dolor sit amet', 'consetetur adipisicing elit']
	context = {

		'title': 'django e-commerce',
		'texts': texts
	}
	return render(request, 'index.html', context)
# Create your views here.
