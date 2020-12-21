from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    # return HttpResponse('Hello world!') ---> chtoby nash sait bylo by "Hello world"
    question_list = Question.objects.all()
    context = {'questions': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    print(request)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Choose the ids 1 to 4 for see the pages!')

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    # request.POST
    question = get_object_or_404(Question, pk=question_id)
    # print(request.POST['choice'])
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detaril.html',{
            'question': question,
            'error_messagee': "You didn't select a choice button!"
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})





