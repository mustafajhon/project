from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def sahil(request):
    return render(request, 'shail/sahil.html')
