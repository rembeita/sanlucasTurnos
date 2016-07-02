from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView

from .models import Chc
from .models import Turnos
from .models import Dres
from .models import Espec

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def elegirHora(request):
	
	if request.method == 'POST':
		formvar = request.POST
		day = str(formvar['day'])
		month = str(formvar['month'])
		year = str(formvar['year'])


	print day
	print year
	print month

	#if returnvalue == "Salir":
         #       return HttpResponseRedirect('/turnosapp/')
	context["hola"]="nada"

	return render(request, 'turnosapp/index.html', context)


