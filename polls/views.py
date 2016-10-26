"""
Descripcion de varios metodos que se usaran en las encuestas
"""

from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')

    assert template!=None
    print("Ha superado el test")
    
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    """ Muestra informacion de la pregunta seleccionada. """
    return HttpResponse("Estas viendo la pregunta numero %s." % question_id)

def results(request, question_id):
    """ Muestra los resultados de la pregunta """
    response = "Aqui se muestran los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """ Permite votar la pregunta """
    return HttpResponse("Estas votando a la pregunta %s." % question_id)
