from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'hello/hello.html')


# def hello(request):
#     return render(request, 'hello/hello.html')
