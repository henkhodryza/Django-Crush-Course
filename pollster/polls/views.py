from django.shortcuts import render

from .models import Question, Choice

# Get Question and display them


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and Choice


def detail(request, quedtion_id):
    try:
        question = Question.objects.get(pk=quedtion_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/results.html', {'question': question})


# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # Create your views here.
