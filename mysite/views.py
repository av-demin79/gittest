from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello World")

def status(request):
	return HttpResponse("<h1>Hello World</h1> <h2><a href = '/'>прасив</a></h2>")