from polls.models import Question
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    output = ', '.join(q.question_text for q in question_list)

    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" %question_id)

def results(request, question_id):
    return HttpResponse("You are looking at result of question %s" %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

