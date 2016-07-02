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


def formatear_id_medico(idmedico):
	resultado = 4 - len(idmedico)
	return (" " * resultado) + idmedico

def validaringreso(request):
	if request.method == 'POST':
		formvar = request.POST
		documentovalue = str(formvar['documento'])
		telefonovalue = str(formvar['telefono'])
	chc_info = Chc.objects.all().filter(nro_doc = documentovalue)
	chc_info = chc_info.filter(tele = telefonovalue)
	dicmedicos = {}

	context = locals()

	if not chc_info:
		print "NOvalido"
		mensaje = "Paciente NO registrado o Clave Incorrecta."
		mensaje2 = "Solicite turno telefonicamente."
		context['MENSAJE'] = mensaje
		context['MENSAJE2'] = mensaje2
		return render(request, 'turnosapp/novalidaingreso.html', context)

	nombrepaciente = str(chc_info.values("acciden")[0]["acciden"])
	idpaciente = str(chc_info.values("id")[0]["id"])
	dnipaciente = str(chc_info.values("nro_doc")[0]["nro_doc"])
	context['PACIENTE'] = nombrepaciente
	context['DNIPACIENTE'] = dnipaciente
	
	turnos_info = Turnos.objects.all().filter(id_chc = idpaciente)
	sqlmedicos = turnos_info.values("nro_doc")

	medicosxpaciente = []
	for i in sqlmedicos:
		medicosxpaciente.append(i["nro_doc"])
	dicmedicotmp = {}

	print medicosxpaciente
	for i in medicosxpaciente:
		try:
			medicotmp = []
			valor = formatear_id_medico(i)
			doctores_info = Dres.objects.all().filter(cod_med = valor)
			medicotmp.append(valor)
			print "DOCTOR ESP: " + str(doctores_info.values("cod_esp")[0]["cod_esp"])
			medicotmp.append(str(doctores_info.values("nombre")[0]["nombre"]))
			medicotmp.append(str(doctores_info.values("cod_esp")[0]["cod_esp"]))
			print "ESTE ES MEDICOTMP: " + str(medicotmp)
			valoresp = formatear_id_medico(medicotmp[2])
			valoresp = " 258"
			obtener_especialidad = Espec.objects.all().filter(cod_esp = valoresp).values("nom_esp")[0]["nom_esp"]
	#	obtener_especialidad = Espec.objects.all().values("cod_esp")
			medicotmp.append(str(obtener_especialidad))
			dicmedicotmp[valor]= medicotmp
		except ValueError:
			print ValueError
			pass
	print dicmedicotmp
	if not dicmedicotmp:
		print "NOvalido DICIONARIO"
		mensaje = "No se encontraron medicos registrados." 
		mensaje2 = "Solicite turno telefonicamente."
		context['MENSAJE'] = mensaje
		context['MENSAJE2'] = mensaje2
		return render(request, 'turnosapp/novalidaingreso.html', context)
	
	context["DICMEDICOTMP"] = dicmedicotmp

	return render(request, 'turnosapp/validaingreso.html', context)
