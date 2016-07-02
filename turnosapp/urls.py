from django.conf.urls import url

from . import views
from . import index
from . import validaringreso
from . import elegirTurno
from . import elegirHora
from . import confirmaturno
from . import cierreturno
from . import finalturno

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^validaringreso/$', validaringreso.validaringreso, name='validaringreso'),
    url(r'^elegirTurno/$', elegirTurno.elegirTurno, name='elegirTurno'),
    url(r'^elegirHora/$', elegirHora.elegirHora, name='elegirHora'),
    url(r'^confirmaturno/$', confirmaturno.confirmaturno, name='confirmaturno'),
    url(r'^cierreturno/$', cierreturno.cierreturno, name='cierreturno'),
    url(r'^finalturno/$', finalturno.finalturno, name='finalturno'),
]
