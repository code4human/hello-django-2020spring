from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect #HttpResponse
#from django.templates import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        # 템플릿 변수명 : Python 객체
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    '''
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        #뷰는 요청된 질문의 ID 가 없을 경우
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question})
    '''
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/detail.html', {'question':question})
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    #response = "You're looking at the results of question %s.")
    #return HttpResponse(response %question_id)
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
    '''
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))