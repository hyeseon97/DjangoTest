from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func(request):
    return HttpResponse("장고테스트 난 장고 마스터")
