from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def mustafa(request):
    return render(request, 'mustafa/mustafa.html')
