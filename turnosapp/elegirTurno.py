from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView

from .models import Tblhmed

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.db.models import Q


def elegirTurno(request):
	import calendar
	import locale
	import datetime

	returnValue=""
	if request.method == 'POST':
		formvar = request.POST
		if (formvar.has_key('accion')):
			avance = int(formvar['avance'])
			accion = str(formvar['accion'])
			if (accion == "Avanzar"):
				avance+=1
			else:
				avance-=1
			nomPaciente = str(formvar['nomPaciente'])
			dniPaciente = str(formvar['dniPaciente'])
		        nomMedico = str(formvar['nomMedico'])
		        codMedico = str(formvar['codMedico'])
		        especialidad = str(formvar['especialidad'])
		else:
			avance=0
			if (formvar.has_key('return')):
				if (str(formvar['return']) == 'Salir'):
					return HttpResponseRedirect('/turnosapp/')
			else:
				medicoEleccion = str(formvar['datosmedico'])
				nomPaciente = str(formvar['nombrepaciente'])
				dniPaciente = str(formvar['dnipaciente'])
				nomMedico, especialidad, codMedico = medicoEleccion.split("||")
	codMedico=codMedico.strip()
	locale.setlocale(locale.LC_ALL, 'es_ES.utf8')
	now=datetime.datetime.now()
#	year=now.year -1
	year=now.year 
	month=now.month+avance

	#controlar si se pasa de mes 12
	if (month > 12): 
		dif=month-12
		year+=1
		month=dif


	#Preparo contexto para devolver a template
	lstFechas=[]
	fechas=Tblhmed.objects.filter(medico=codMedico,fecha__year = "%s" % (year),fecha__month = "%s" % (month)).filter(Q(t700 = "X") | Q(t705 = "X") | Q(t710 = "X") | Q(t715 = "X") | Q(t720 = "X") | Q(t725 = "X") | Q(t730 = "X") | Q(t735 = "X") | Q(t740 = "X") | Q(t745 = "X") | Q(t750 = "X") | Q(t755 = "X") | Q(t800 = "X") | Q(t805 = "X") | Q(t910 = "X") | Q(t815 = "X") | Q(t820 = "X") | Q(t825 = "X") | Q( t830 = "X") | Q(t835 = "X") | Q(t840 = "X") | Q(t845 = "X") | Q(t850 = "X") | Q(t855 = "X") | Q(t900 = "X") | Q(t905 = "X") | Q(t910 = "X") | Q(t915 = "X") | Q(t920 = "X") | Q(t925 = "X") | Q(t930 = "X") | Q(t935 = "X") | Q(t940 = "X") | Q(t945 = "X") | Q(t950 = "X") | Q(t955 = "X") | Q(t1000 = "X") | Q(t1005 = "X") | Q(t1010 = "X") | Q(t1015 = "X") | Q(t1020 = "X") | Q(t1025 = "X") | Q(t1030 = "X") | Q(t1035 = "X") | Q(t1040 = "X") | Q(t1045 = "X") | Q(t1050 = "X") | Q(t1055 = "X") | Q(t1100 = "X") | Q(t1105 = "X") | Q(t1110 = "X") | Q(t1115 = "X") | Q(t1120 = "X") | Q(t1125 = "X") | Q(t1130 = "X") | Q(t1135 = "X") | Q(t1140 = "X") | Q(t1145 = "X") | Q(t1150 = "X") | Q(t1155 = "X") | Q(t1200 = "X") | Q(t1205 = "X") | Q(t1210 = "X") | Q(t1215 = "X") | Q(t1220 = "X") | Q(t1225 = "X") | Q(t1230 = "X") | Q(t1235 = "X") | Q(t1240 = "X") | Q(t1245 = "X") | Q(t1250 = "X") | Q(t1255 = "X") | Q(t1300 = "X") | Q(t1305 = "X") | Q(t1310 = "X") | Q(t1315 = "X") | Q(t1320 = "X") | Q(t1325 = "X") | Q(t1330 = "X") | Q(t1335 = "X") | Q(t1340 = "X") | Q(t1345 = "X") | Q(t1350 = "X") | Q(t1355 = "X") | Q(t1400 = "X") | Q(t1405 = "X") | Q(t1410 = "X") | Q(t1415 = "X") | Q(t1420 = "X") | Q(t1425 = "X") | Q(t1430 = "X") | Q(t1435 = "X") | Q(t1440 = "X") | Q(t1445 = "X") | Q(t1450 = "X") | Q(t1455 = "X") | Q(t1500 = "X") | Q(t1505 = "X") | Q(t1510 = "X") | Q(t1515 = "X") | Q(t1520 = "X") | Q(t1525 = "X") | Q(t1530 = "X") | Q(t1535 = "X") | Q(t1540 = "X") | Q(t1545 = "X") | Q(t1550 = "X") | Q(t1555 = "X") | Q(t1600 = "X") | Q(t1605 = "X") | Q(t1610 = "X") | Q(t1615 = "X") | Q(t1620 = "X") | Q(t1625 = "X") | Q(t1630 = "X") | Q(t1635 = "X") | Q(t1640 = "X") | Q(t1645 = "X") | Q(t1650 = "X") | Q(t1655 = "X") | Q(t1700 = "X") | Q(t1705 = "X") | Q(t1710 = "X") | Q(t1715 = "X") | Q(t1720 = "X") | Q(t1725 = "X") | Q(t1730 = "X") | Q(t1735 = "X") | Q(t1740 = "X") | Q(t1745 = "X") | Q(t1750 = "X") | Q(t1755 = "X") | Q(t1800 = "X") | Q(t1805 = "X") | Q(t1810 = "X") | Q(t1815 = "X") | Q(t1820 = "X") | Q(t1825 = "X") | Q(t1830 = "X") | Q(t1835 = "X") | Q(t1840 = "X") | Q(t1845 = "X") | Q(t1850 = "X") | Q(t1855 = "X") | Q(t1900 = "X") | Q(t1905 = "X") | Q(t1910 = "X") | Q(t1915 = "X") | Q(t1920 = "X") | Q(t1925 = "X") | Q(t1930 = "X") | Q(t1935 = "X") | Q(t1940 = "X") | Q(t1945 = "X") | Q(t1950 = "X") | Q(t1955 = "X") | Q(t2000 = "X") | Q(t2005 = "X") | Q(t2010 = "X") | Q(t2015 = "X") | Q(t2020 = "X") | Q(t2025 = "X") | Q(t2030 = "X") | Q(t2035 = "X") | Q(t2040 = "X") | Q(t2045 = "X") | Q(t2050 = "X") | Q(t2055 = "X") | Q(t2100 = "X") | Q(t2105 = "X") | Q(t2110 = "X") | Q(t2115 = "X") | Q(t2120 = "X") | Q(t2125 = "X") | Q(t2130 = "X") | Q(t2135 = "X") | Q(t2140 = "X") | Q(t2145 = "X") | Q(t2150 = "X") | Q(t2155 = "X") | Q(t2200 = "X") | Q(t2205 = "X") | Q(t2210 = "X") | Q(t2215 = "X") | Q(t2220 = "X") | Q(t2225 = "X") | Q(t2230 = "X") | Q(t2235 = "X") | Q(t2240 = "X") | Q(t2245 = "X") | Q(t2250 = "X") | Q(t2255 = "X"))
	lstTurnos={}
	for linea in fechas:
		turnos=linea.getTurnos()
		if (turnos != []):
			yearMed, monthMed, dayMed = str(linea.fecha).split("-")
			lstFechas.append(int(dayMed.lstrip("0")))
			for turno in turnos:
				dayMed=int(dayMed)
				if (not lstTurnos.has_key(dayMed)):
					lstTurnos[dayMed]="%s-%s-%s|t%s" % (year, month, dayMed, turno)
				else:
					lstTurnos[dayMed]="%s|t%s" % (lstTurnos[dayMed], turno)
	
	monthList=calendar.monthcalendar(year,month)

	monthTurno=[]	
	for monthObj in monthList:
		weekTurno=[]
		for dayObj in monthObj:
			dayDict={}
			if (dayObj in lstTurnos):
				dayDict[dayObj]=lstTurnos[dayObj]
			else:
				dayDict[dayObj]=""
			weekTurno.append(dayDict)
		monthTurno.append(weekTurno)

	context = locals()
	context["monthTurno"]=monthTurno
	context["avance"]=avance
	context["month"]=month
	context["year"]=year
	context["monthName"]=calendar.month_name[month]

	context["NOMBREPACIENTE"] = nomPaciente
	context["NOMBREDOCTOR"] = nomMedico
	context["NOMBREESPECIALIDAD"] = especialidad
	context["CODMEDICO"] = codMedico
	context["DNIPACIENTE"] = dniPaciente

	return render(request, 'turnosapp/seleccionturno.html', context)

