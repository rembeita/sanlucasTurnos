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



def confirmaturno(request):
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
		aniovalue = str(formvar['year'])      	
		mesvalue = str(formvar['month'])      	
		buttondayvalue = str(formvar['buttonDay'])      	
	buttondayvalue = buttondayvalue.split('|')
	fechadatabasevalue = buttondayvalue[0]
	listahora = buttondayvalue[1:]
	fechaparse = fechadatabasevalue.split('-')
	fechavalue = fechaparse[2] + "-" + fechaparse[1] + '-' + fechaparse[0]
	
	dicmedicolibre = []
	for i in listahora:
		data = i
		data = data.replace('t','')
		data = data.replace(' ','')
		print data
		if len(data) < 4:
			data = "0" + data
			data = data[:2] + ":" + data[2:]
#			dicmedicolibre[i] = data
			dicmedicolibre.append([i, data])

		else:
			data = data[:2] + ":" + data[2:]
			dicmedicolibre.append([i, data])
			#dicmedicolibre[i] = data

	print listahora
	print dicmedicolibre
	context = locals()
	context["nomPaciente"] = nombrepacientevalue
	context["dniPaciente"] = dnipacientevalue
	context["especialidad"] = especialidadvalue 
	context["nomMedico"] = nombremedicovalue
	context["codMedico"] = codmedvalue
#	context["LISTAMEDICOLIBRE"] = listamedicolibre
	context["dicMedicoLibre"] = dicmedicolibre
	context["fecha"] = fechavalue
	context["fechaDatabase"] = fechadatabasevalue
	return render(request, 'turnosapp/confirmaturno.html', context)
