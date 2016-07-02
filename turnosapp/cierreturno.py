from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView

from .models import Chc
from .models import Turnos
from .models import Dres
from .models import Espec
from .models import Tblhmed

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect



def cierreturno(request):
	if request.method == 'POST':
		formvar = request.POST
                if (formvar.has_key('return')):
                        if (str(formvar['return']) == 'Salir'):
                                return HttpResponseRedirect('/turnosapp/')

		especialidadvalue = str(formvar['especialidad'])
		nombremedicovalue = str(formvar['nomMedico'])
		codmedvalue = str(formvar['codMedico'])
		nombrepacientevalue = str(formvar['nomPaciente'])      	
		dnipacientevalue = str(formvar['dniPaciente'])
		fechavalue = str(formvar['fecha'])
		horariomedicovalue = str(formvar['horarioMedico'])
		fechadatabasevalue = str(formvar['fechaDatabase'])

	horariomedicovalue = horariomedicovalue.split('|')
	horadatabasevalue = horariomedicovalue[0]
	horavalue = horariomedicovalue[1]
        context = locals()	
	context["nomPaciente"] = nombrepacientevalue
	context["dniPaciente"] = dnipacientevalue
	context["especialidad"] = especialidadvalue 
	context["nomMedico"] = nombremedicovalue
	context["codMedico"] = codmedvalue
	context["fecha"] = fechavalue
	context["hora"] = horavalue
	context["fechaDatabase"] = fechadatabasevalue
	context["horaDatabase"] = horadatabasevalue
	

	return render(request, 'turnosapp/cierreturno.html', context)
