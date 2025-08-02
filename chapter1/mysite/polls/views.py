from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello, world. you are in a polls index')

def detail(request,question_id):
    return HttpResponse("You're looking at question %s."  % question_id)

def results(request, question_id):
    response =  HttpResponse("You're looking at results of question %s.")
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're vooting on question %s." % question_id)
