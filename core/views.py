from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, valor1, valor2):
    resultado = valor1 + valor2
    return HttpResponse('<h1>O valor da soma dos valores é: {} '.format(resultado))

def subtracao(request, valor1, valor2):
    resultado = valor1 - valor2
    return HttpResponse('<h1>O valor da subtracao dos valores é: {} '.format(resultado))

def divisao(request, valor1, valor2):
    resultado = valor1 / valor2
    return HttpResponse('<h1>O valor da divisao dos valores é: {} '.format(resultado))

def multiplicacao(request, valor1, valor2):
    resultado = valor1 * valor2
    return HttpResponse('<h1>O valor da multiplicacao dos valores é: {} '.format(resultado))