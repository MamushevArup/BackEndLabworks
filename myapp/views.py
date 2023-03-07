from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = request.GET.get("name", "world")
    return HttpResponse("Hello, {}!".format(name))

def message(request):
    message = request.GET.get("search", "something wrong")
    return render(request, 'search.html', {'message': message})

