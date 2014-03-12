from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Poll



def index(request):
    latest_question_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    question = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, poll_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on question %s." % poll_id)


