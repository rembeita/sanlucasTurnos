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



def finalturno(request):
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
		horadatabasevalue = str(formvar['horaDatabase'])
		horavalue = str(formvar['hora'])


        context = locals()	
	context["nomPaciente"] = nombrepacientevalue
	context["dniPaciente"] = dnipacientevalue
	context["especialidad"] = especialidadvalue 
	context["nomMedico"] = nombremedicovalue
	context["codMedico"] = codmedvalue
	context["fecha"] = fechavalue
	context["hora"] = horavalue
	context["horarioMedico"] = horariomedicovalue
	fechaDatabase = fechadatabasevalue
	horadatabasevalue = horadatabasevalue.replace(' ','')

	aplicarcambio = Tblhmed.objects.all().filter( medico = codmedvalue )
	aplicarcambio = aplicarcambio.filter( fecha = fechaDatabase )
	
	estadoturno = aplicarcambio.values(horadatabasevalue)[0][horadatabasevalue]
    
	if (formvar.has_key('confirmar')):
		if estadoturno == "X":
			mensaje = "Su turno ha sido confirmado. Muchas Gracias."
			color	= "green"
			aplicarcambio = aplicarcambio.update( **{horadatabasevalue: "C" })
		else:
			mensaje = "No se pudo confirmar el turno o el mismo se encuentra ocupado. Favor de volver a intentar."
			color   = "red"

		context["mensaje"] = mensaje
		context["color"] = color
		return render(request, 'turnosapp/finalturno.html', context)
	
	if (formvar.has_key('confirmareimprimir')):
		if estadoturno == "X":
			mensaje = "Su turno ha sido confirmado. Muchas Gracias. " 
			color	= "green"
			aplicarcambio = aplicarcambio.update( **{horadatabasevalue: "C" })
			return render(request, 'turnosapp/finalturnopdf.html', context)
		else:
			mensaje = "No se pudo confirmar el turno o el mismo se encuentra ocupado. Favor de volver a intentar." 
			color   = "red"
			context["mensaje"] = mensaje
			context["color"] = color
			return render(request, 'turnosapp/finalturno.html', context)


