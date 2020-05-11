from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.template import loader
from django.views import generic
from mysite import settings

# Create your views here.
#def index(request):
#    question_list = Question.objects.order_by('pub_date')[:5]
#    #return render(request, 'polls/index.html', {'q_list':question_list})
#    temp = loader.get_template('polls/index.html')
#    return HttpResponse(temp.render({'q_list':question_list}, request))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'q_list'
    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]


#def select(request, question_id):
#    target_question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/select.html', {'tar_q':target_question})

class SelectView(generic.DetailView):
    template_name = 'polls/select.html'
    #queryset = Question.objects.all()
    model = Question
    context_object_name = 'tar_q'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q_list"] = Question.objects.all()
        return context
    
    

def vote(request, question_id):
    target_question = get_object_or_404(Question, pk=question_id)
    print(request.build_absolute_uri('/'))
    try: 
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/select.html', {'tar_q':target_question, 'error_msg':'Error occured.', 'applist': applist})
    else:
        selected_choice.vote_cnt+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

#def result(request, question_id):
#    target_question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/result.html', {'tar_q':target_question})

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'
    context_object_name = 'tar_q'
