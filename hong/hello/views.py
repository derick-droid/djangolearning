from django.shortcuts import render
from django.http import HttpResponse
from .models import Questionpolls

# Create your views here.
# uploading html content
def question(request):
    questions = Questionpolls.objects.all()
    context = {
        'questions_objects' : questions
    }
    return render(request, 'hello/question.html', context)
def home(request): 
    return render (request, 'hello/home.html')

def about(request):
    return render(request, 'hello/about.html')

# giving response
def greet(request):
    return HttpResponse('hello mr coder(programmer)')

def greeting(request):
    return HttpResponse('hello boy')

def great(request):
    return HttpResponse('coming home')