from django.shortcuts import render
from django.http import HttpResponse
from django.templates import loader

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        # 템플릿 변수명 : Python 객체
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        #뷰는 요청된 질문의 ID 가 없을 경우
        raise Http404("Question does not exist")
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s.")
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)