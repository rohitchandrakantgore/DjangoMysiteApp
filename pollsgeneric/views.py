from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from .models import ChoiceGeneric, QuestionGeneric
from django.utils import timezone
import datetime

class IndexView(generic.ListView):
    template_name = 'pollsgeneric/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return QuestionGeneric.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = QuestionGeneric
    template_name = 'pollsgeneric/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return QuestionGeneric.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = QuestionGeneric
    template_name = 'pollsgeneric/results.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return QuestionGeneric.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(QuestionGeneric, pk=question_id)
    try:
        selected_choice = question.choicegeneric_set.get(pk=request.POST['choice'])
    except (KeyError, ChoiceGeneric.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pollsgeneric/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pollsgeneric:results_generic', args=(question.id,)))
