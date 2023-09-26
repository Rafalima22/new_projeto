from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse('HomE33')


def sobre(request):
    return HttpResponse('sobre 22')


def contato(request):
    return HttpResponse('contato 01')


def email(request):
    return HttpResponse('este é minha pagina de email')
