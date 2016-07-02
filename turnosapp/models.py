# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Comprobante(models.Model):
    comp_ord = models.IntegerField(db_column='COMP_ORD', blank=True, null=True)  # Field name made lowercase.
    comp_cod = models.CharField(db_column='COMP_COD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    comp_descri = models.CharField(db_column='COMP_DESCRI', max_length=25, blank=True, null=True)  # Field name made lowercase.
    comp_ulti = models.IntegerField(db_column='COMP_ULTI', blank=True, null=True)  # Field name made lowercase.
    factu = models.CharField(db_column='FACTU', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pago = models.CharField(db_column='PAGO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    comp_descria = models.CharField(db_column='COMP_DESCRIA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    comp_caja = models.CharField(db_column='COMP_CAJA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    comp_signo = models.SmallIntegerField(db_column='COMP_SIGNO', blank=True, null=True)  # Field name made lowercase.
    comp_aplic = models.TextField(db_column='COMP_APLIC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comp_ascod = models.CharField(db_column='COMP_ASCOD', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMPROBANTE'


class Cuentas(models.Model):
    pro_ord = models.IntegerField(db_column='PRO_ORD', blank=True, null=True)  # Field name made lowercase.
    pro_tp = models.CharField(db_column='PRO_TP', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pro_cod = models.CharField(db_column='PRO_COD', max_length=8, blank=True, null=True)  # Field name made lowercase.
    pro_nombre = models.CharField(db_column='PRO_NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pro_vig = models.CharField(db_column='PRO_VIG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pro_obs = models.CharField(db_column='PRO_OBS', max_length=80, blank=True, null=True)  # Field name made lowercase.
    pro_ctasistema = models.CharField(db_column='PRO_CTASISTEMA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pro_planilla = models.CharField(db_column='PRO_PLANILLA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUENTAS'


class Empleado(models.Model):
    epl_ord = models.IntegerField(db_column='EPL_ORD', blank=True, null=True)  # Field name made lowercase.
    epl_legajo = models.FloatField(db_column='EPL_LEGAJO', blank=True, null=True)  # Field name made lowercase.
    epl_nombre = models.CharField(db_column='EPL_NOMBRE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    epl_tdoc = models.CharField(db_column='EPL_TDOC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    epl_ndoc = models.IntegerField(db_column='EPL_NDOC', blank=True, null=True)  # Field name made lowercase.
    epl_cuil = models.CharField(db_column='EPL_CUIL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    epl_tarjeta = models.CharField(db_column='EPL_TARJETA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    epl_horario = models.CharField(db_column='EPL_HORARIO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    epl_exceptuado = models.CharField(db_column='EPL_EXCEPTUADO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    epl_tpcontrat = models.CharField(db_column='EPL_TPCONTRAT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    epl_estcivil = models.CharField(db_column='EPL_ESTCIVIL', max_length=8, blank=True, null=True)  # Field name made lowercase.
    epl_sector = models.CharField(db_column='EPL_SECTOR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    epl_categ = models.CharField(db_column='EPL_CATEG', max_length=8, blank=True, null=True)  # Field name made lowercase.
    epl_fingreso = models.CharField(db_column='EPL_FINGRESO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    epl_fnacim = models.CharField(db_column='EPL_FNACIM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    epl_domicilio = models.CharField(db_column='EPL_DOMICILIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    epl_locali = models.CharField(db_column='EPL_LOCALI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    epl_cp = models.CharField(db_column='EPL_CP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    epl_tel1 = models.CharField(db_column='EPL_TEL1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    epl_email = models.CharField(db_column='EPL_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    epl_obs = models.TextField(db_column='EPL_OBS', blank=True, null=True)  # Field name made lowercase.
    epl_vig = models.CharField(db_column='EPL_VIG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    epl_usuario = models.CharField(db_column='EPL_USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    epl_fechahoy = models.CharField(db_column='EPL_FECHAHOY', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLEADO'


class Account(models.Model):
    accountid = models.AutoField(primary_key=True)
    accountdescription = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class ApplicationLogs(models.Model):
    applicationlogid = models.AutoField(primary_key=True)
    application_name = models.CharField(max_length=50, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    login = models.CharField(max_length=10, blank=True, null=True)
    ip_user = models.CharField(max_length=20, blank=True, null=True)
    action_held = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_logs'


class Archivos(models.Model):
    nom_linux = models.CharField(db_column='NOM_LINUX', max_length=40)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=40)  # Field name made lowercase.
    seudo = models.CharField(db_column='SEUDO', max_length=8)  # Field name made lowercase.
    orden = models.CharField(db_column='ORDEN', max_length=40)  # Field name made lowercase.
    indice = models.CharField(db_column='INDICE', max_length=140)  # Field name made lowercase.
    descri = models.CharField(db_column='DESCRI', max_length=40)  # Field name made lowercase.
    unico = models.CharField(db_column='UNICO', max_length=1)  # Field name made lowercase.
    crea = models.CharField(db_column='CREA', max_length=1)  # Field name made lowercase.
    local = models.CharField(db_column='LOCAL', max_length=1)  # Field name made lowercase.
    nom_loc = models.CharField(db_column='NOM_LOC', max_length=40)  # Field name made lowercase.
    ord_loc = models.CharField(db_column='ORD_LOC', max_length=40)  # Field name made lowercase.
    antx = models.CharField(db_column='ANTX', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'archivos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BarCode(models.Model):
    codabar = models.CharField(max_length=128, blank=True, null=True)
    code11 = models.CharField(max_length=128, blank=True, null=True)
    code39 = models.CharField(max_length=128, blank=True, null=True)
    code39_ext = models.CharField(max_length=128, blank=True, null=True)
    code93 = models.CharField(max_length=128, blank=True, null=True)
    code128 = models.CharField(max_length=128, blank=True, null=True)
    ean8 = models.CharField(max_length=128, blank=True, null=True)
    ean13 = models.CharField(max_length=128, blank=True, null=True)
    gs1_128 = models.CharField(max_length=128, blank=True, null=True)
    isbn_10_isbn_13 = models.CharField(max_length=128, blank=True, null=True)
    interleaved_2_of_5 = models.CharField(max_length=128, blank=True, null=True)
    standard_2_of_5 = models.CharField(max_length=128, blank=True, null=True)
    msi_plessey = models.CharField(max_length=128, blank=True, null=True)
    upc_a = models.CharField(max_length=128, blank=True, null=True)
    upc_e = models.CharField(max_length=128, blank=True, null=True)
    upc_ext_2_dg = models.CharField(max_length=2, blank=True, null=True)
    upc_e_5_dg = models.CharField(max_length=5, blank=True, null=True)
    postnet = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bar_code'


class Categories(models.Model):
    categoryid = models.IntegerField(primary_key=True)
    categoryname = models.CharField(unique=True, max_length=15)
    description = models.TextField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Chc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    acciden = models.CharField(db_column='ACCIDEN', max_length=35)  # Field name made lowercase.
    foto = models.TextField()  # This field type is a guess.
    tip_doc = models.CharField(db_column='TIP_DOC', max_length=3)  # Field name made lowercase.
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=9)  # Field name made lowercase.
    e_civil = models.CharField(db_column='E_CIVIL', max_length=10)  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=1)  # Field name made lowercase.
    domi_par = models.CharField(db_column='DOMI_PAR', max_length=35)  # Field name made lowercase.
    localidad = models.CharField(db_column='LOCALIDAD', max_length=35)  # Field name made lowercase.
    tele = models.CharField(db_column='TELE', max_length=20)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='PROFESSION', max_length=20)  # Field name made lowercase.
    hc = models.CharField(db_column='HC', max_length=10)  # Field name made lowercase.
    fec_nac = models.DateField(db_column='FEC_NAC')  # Field name made lowercase.
    nacional = models.CharField(db_column='NACIONAL', max_length=20)  # Field name made lowercase.
    gs_tipo = models.CharField(db_column='GS_TIPO', max_length=3)  # Field name made lowercase.
    gs_factor = models.CharField(db_column='GS_FACTOR', max_length=3)  # Field name made lowercase.
    gravado = models.CharField(db_column='GRAVADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateTimeField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateTimeField(db_column='FEC_MODI')  # Field name made lowercase.
    lug_fijo = models.CharField(db_column='LUG_FIJO', max_length=10)  # Field name made lowercase.
    sector = models.CharField(db_column='SECTOR', max_length=1)  # Field name made lowercase.
    estruc = models.CharField(db_column='ESTRUC', max_length=3)  # Field name made lowercase.
    estante = models.CharField(db_column='ESTANTE', max_length=2)  # Field name made lowercase.
    sol_secret = models.CharField(db_column='SOL_SECRET', max_length=15)  # Field name made lowercase.
    sol_med = models.CharField(db_column='SOL_MED', max_length=4)  # Field name made lowercase.
    sol_med2 = models.CharField(db_column='SOL_MED2', max_length=30)  # Field name made lowercase.
    sol_ws = models.CharField(db_column='SOL_WS', max_length=3)  # Field name made lowercase.
    sol_lista = models.CharField(db_column='SOL_LISTA', max_length=10)  # Field name made lowercase.
    fec_ent = models.DateField(db_column='FEC_ENT')  # Field name made lowercase.
    hs_ent = models.CharField(db_column='HS_ENT', max_length=5)  # Field name made lowercase.
    fec_devol = models.DateField(db_column='FEC_DEVOL')  # Field name made lowercase.
    hs_devol = models.CharField(db_column='HS_DEVOL', max_length=5)  # Field name made lowercase.
    nom_clie = models.CharField(db_column='NOM_CLIE', max_length=30)  # Field name made lowercase.
    fec_uatt = models.DateField(db_column='FEC_UATT')  # Field name made lowercase.
    tip_clie = models.CharField(db_column='TIP_CLIE', max_length=3)  # Field name made lowercase.
    cod_chc = models.CharField(db_column='COD_CHC', max_length=7)  # Field name made lowercase.
    soc_chc = models.CharField(db_column='SOC_CHC', max_length=22)  # Field name made lowercase.
    bar_chc = models.CharField(db_column='BAR_CHC', max_length=2)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=50)  # Field name made lowercase.
    cuil = models.CharField(db_column='CUIL', max_length=13)  # Field name made lowercase.
    provinc = models.IntegerField(db_column='PROVINC')  # Field name made lowercase.
    splan = models.CharField(db_column='SPLAN', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chc'


class City(models.Model):
    cityid = models.IntegerField(primary_key=True)
    cityname = models.CharField(max_length=254, blank=True, null=True)
    stateid = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Companies(models.Model):
    companyid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Compest(models.Model):
    nro_estu = models.CharField(db_column='NRO_ESTU', max_length=5)  # Field name made lowercase.
    cod_nom = models.CharField(db_column='COD_NOM', max_length=8)  # Field name made lowercase.
    nom_nom = models.CharField(db_column='NOM_NOM', max_length=40)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compest'


class Comseg(models.Model):
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7, blank=True, null=True)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    n_rub = models.CharField(db_column='N_RUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    valfint = models.DecimalField(db_column='VALFINT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valfamb = models.DecimalField(db_column='VALFAMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valpint = models.DecimalField(db_column='VALPINT', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valpamb = models.DecimalField(db_column='VALPAMB', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valpurg = models.DecimalField(db_column='VALPURG', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA', blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI', blank=True, null=True)  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comseg'


class Condidoc(models.Model):
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    detalle = models.CharField(db_column='DETALLE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    detcompl = models.TextField(db_column='DETCOMPL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'condidoc'


class Consul(models.Model):
    cod_consul = models.CharField(db_column='COD_CONSUL', max_length=4)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='UBICACION', max_length=40)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consul'


class Coseg(models.Model):
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=50)  # Field name made lowercase.
    cod_nom = models.CharField(db_column='COD_NOM', max_length=8)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=40)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1)  # Field name made lowercase.
    valfint = models.DecimalField(db_column='VALFINT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    valfamb = models.DecimalField(db_column='VALFAMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    valpint = models.DecimalField(db_column='VALPINT', max_digits=6, decimal_places=2)  # Field name made lowercase.
    valpamb = models.DecimalField(db_column='VALPAMB', max_digits=6, decimal_places=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.
    sec = models.CharField(db_column='SEC', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coseg'


class Country(models.Model):
    iso = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=80)
    printable_name = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    numcode = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Ctrltur(models.Model):
    ws = models.CharField(db_column='WS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    medico = models.CharField(db_column='MEDICO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v1 = models.CharField(db_column='V1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    v2 = models.CharField(db_column='V2', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ctrltur'


class Customers(models.Model):
    customerid = models.CharField(primary_key=True, max_length=5)
    companyname = models.CharField(max_length=40)
    contactname = models.CharField(max_length=50, blank=True, null=True)
    contacttitle = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    regionid = models.IntegerField(blank=True, null=True)
    stateid = models.ForeignKey('States', db_column='stateid', blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    cityid = models.IntegerField(blank=True, null=True)
    creditlimit = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    cardtype = models.CharField(max_length=1, blank=True, null=True)
    cardnumber = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DataEntry(models.Model):
    chave = models.AutoField(primary_key=True)
    cmp_text = models.CharField(max_length=90, blank=True, null=True)
    cmp_email = models.CharField(max_length=30, blank=True, null=True)
    cmp_option = models.CharField(max_length=1, blank=True, null=True)
    cmp_vl_centavos = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_vl_centavos_neg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_vl_centavos_neg_obrig = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_vl_pontodecimal = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_vl_pontodecimal_neg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_vl_pontodecimal_neg_obrig = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_inteiros = models.IntegerField(blank=True, null=True)
    cmp_inteiros_neg = models.IntegerField(blank=True, null=True)
    cmp_inteiros_neg_obrig = models.IntegerField(blank=True, null=True)
    cmp_inteiros_2 = models.IntegerField(blank=True, null=True)
    cmp_inteiros_2_neg = models.IntegerField(blank=True, null=True)
    cmp_inteiros_2_neg_obrig = models.IntegerField(blank=True, null=True)
    cmp_data1 = models.DateField(blank=True, null=True)
    cmp_hora1 = models.TimeField(blank=True, null=True)
    cmp_data2 = models.DateTimeField(blank=True, null=True)
    cmp_data3 = models.DateField(blank=True, null=True)
    cmp_date33 = models.DateField(blank=True, null=True)
    cmp_data4 = models.DateTimeField(blank=True, null=True)
    cmp_money_centavos = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_money_centavos_neg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_money_centavos_neg_obrig = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_money_pontodecimal = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_money_pontodecimal_neg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_money_pontodecimal_neg_obrig = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    cmp_inteiros2 = models.IntegerField(blank=True, null=True)
    cmp_mask1 = models.CharField(max_length=60, blank=True, null=True)
    cmp_mask2 = models.CharField(max_length=60, blank=True, null=True)
    cmp_mask3 = models.CharField(max_length=60, blank=True, null=True)
    cmp_mask4 = models.CharField(max_length=60, blank=True, null=True)
    cmp_mask5 = models.CharField(max_length=60, blank=True, null=True)
    cmp_mask6 = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_entry'


class Departments(models.Model):
    deptid = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Diasemana(models.Model):
    ndia = models.CharField(max_length=1)
    nombre = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'diasemana'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dmodulo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cod_med = models.CharField(db_column='COD_MED', max_length=4)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7)  # Field name made lowercase.
    codmod = models.CharField(db_column='CODMOD', max_length=8)  # Field name made lowercase.
    desc1 = models.CharField(db_column='DESC1', max_length=50)  # Field name made lowercase.
    desc2 = models.CharField(db_column='DESC2', max_length=50)  # Field name made lowercase.
    desc3 = models.CharField(db_column='DESC3', max_length=50)  # Field name made lowercase.
    imp_porc = models.CharField(db_column='IMP_PORC', max_length=1)  # Field name made lowercase.
    hono_por = models.DecimalField(db_column='HONO_POR', max_digits=5, decimal_places=2)  # Field name made lowercase.
    gastos_por = models.DecimalField(db_column='GASTOS_POR', max_digits=5, decimal_places=2)  # Field name made lowercase.
    hono = models.DecimalField(db_column='HONO', max_digits=10, decimal_places=2)  # Field name made lowercase.
    gastos = models.DecimalField(db_column='GASTOS', max_digits=10, decimal_places=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dmodulo'


class Docexce(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cod_med = models.CharField(db_column='COD_MED', max_length=4)  # Field name made lowercase.
    cod_emp = models.IntegerField(db_column='COD_EMP')  # Field name made lowercase.
    cod = models.CharField(db_column='COD', max_length=8)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=40)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1)  # Field name made lowercase.
    cod_hon = models.CharField(db_column='COD_HON', max_length=2)  # Field name made lowercase.
    cod_gas = models.CharField(db_column='COD_GAS', max_length=2)  # Field name made lowercase.
    esp_int = models.DecimalField(db_column='ESP_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu_int = models.DecimalField(db_column='AYU_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu2_int = models.DecimalField(db_column='AYU2_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ane_int = models.DecimalField(db_column='ANE_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    extr_int = models.DecimalField(db_column='EXTR_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gqui_int = models.DecimalField(db_column='GQUI_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gext_int = models.DecimalField(db_column='GEXT_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    esp_amb = models.DecimalField(db_column='ESP_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu_amb = models.DecimalField(db_column='AYU_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu2_amb = models.DecimalField(db_column='AYU2_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ane_amb = models.DecimalField(db_column='ANE_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    extr_amb = models.DecimalField(db_column='EXTR_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gqui_amb = models.DecimalField(db_column='GQUI_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gext_amb = models.DecimalField(db_column='GEXT_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'docexce'


class Dremplan(models.Model):
    cod_med = models.CharField(db_column='COD_MED', max_length=4)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=4)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=40)  # Field name made lowercase.
    modop = models.CharField(db_column='MODOP', max_length=1)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dremplan'


class Dres(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cod_med = models.CharField(db_column='COD_MED', unique=True, max_length=4)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30)  # Field name made lowercase.
    cod_esp = models.SmallIntegerField(db_column='COD_ESP')  # Field name made lowercase.
    cod_esp1 = models.CharField(db_column='COD_ESP1', max_length=4)  # Field name made lowercase.
    mat_nac = models.CharField(db_column='MAT_NAC', max_length=6)  # Field name made lowercase.
    mat_prov = models.CharField(db_column='MAT_PROV', max_length=6)  # Field name made lowercase.
    domicil = models.CharField(db_column='DOMICIL', max_length=30)  # Field name made lowercase.
    localidad = models.CharField(db_column='LOCALIDAD', max_length=20)  # Field name made lowercase.
    nro_cuit = models.CharField(db_column='NRO_CUIT', max_length=13)  # Field name made lowercase.
    cond_iva = models.CharField(db_column='COND_IVA', max_length=2)  # Field name made lowercase.
    por_2 = models.CharField(db_column='POR_2', max_length=1)  # Field name made lowercase.
    alquiler = models.DecimalField(db_column='ALQUILER', max_digits=10, decimal_places=2)  # Field name made lowercase.
    te = models.CharField(db_column='TE', max_length=15)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', max_length=15)  # Field name made lowercase.
    derecho = models.DecimalField(db_column='DERECHO', max_digits=6, decimal_places=2)  # Field name made lowercase.
    honorar = models.DecimalField(db_column='HONORAR', max_digits=6, decimal_places=2)  # Field name made lowercase.
    por_cpsm = models.DecimalField(db_column='POR_CPSM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    por_pret = models.DecimalField(db_column='POR_PRET', max_digits=6, decimal_places=2)  # Field name made lowercase.
    p_h_e_con = models.DecimalField(db_column='P_H_E_CON', max_digits=6, decimal_places=2)  # Field name made lowercase.
    p_h_e_pra = models.DecimalField(db_column='P_H_E_PRA', max_digits=6, decimal_places=2)  # Field name made lowercase.
    p_h_s_con = models.DecimalField(db_column='P_H_S_CON', max_digits=6, decimal_places=2)  # Field name made lowercase.
    p_h_s_pra = models.DecimalField(db_column='P_H_S_PRA', max_digits=6, decimal_places=2)  # Field name made lowercase.
    p_gad_pra = models.DecimalField(db_column='P_GAD_PRA', max_digits=5, decimal_places=2)  # Field name made lowercase.
    p_gad_con = models.DecimalField(db_column='P_GAD_CON', max_digits=5, decimal_places=2)  # Field name made lowercase.
    p_apor_soc = models.DecimalField(db_column='P_APOR_SOC', max_digits=6, decimal_places=2)  # Field name made lowercase.
    p_a_s_cpsm = models.DecimalField(db_column='P_A_S_CPSM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    ib_resp = models.CharField(db_column='IB_RESP', max_length=1)  # Field name made lowercase.
    nro_ib = models.CharField(db_column='NRO_IB', max_length=14)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.
    coefurg = models.DecimalField(db_column='COEFURG', max_digits=6, decimal_places=2)  # Field name made lowercase.
    tex1 = models.CharField(db_column='TEX1', max_length=50)  # Field name made lowercase.
    tex2 = models.CharField(db_column='TEX2', max_length=50)  # Field name made lowercase.
    tex3 = models.CharField(db_column='TEX3', max_length=50)  # Field name made lowercase.
    tex4 = models.CharField(db_column='TEX4', max_length=50)  # Field name made lowercase.
    cod_ssl = models.CharField(db_column='COD_SSL', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dres'


class Ee1(models.Model):
    codigo = models.BigIntegerField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase.
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dia_tur = models.DateField(db_column='DIA_TUR', blank=True, null=True)  # Field name made lowercase.
    hora_tur = models.CharField(db_column='HORA_TUR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    min_tur = models.CharField(db_column='MIN_TUR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pac_tur = models.CharField(db_column='PAC_TUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    o_social = models.CharField(db_column='O_SOCIAL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nro_afil = models.CharField(db_column='NRO_AFIL', max_length=22, blank=True, null=True)  # Field name made lowercase.
    bar_afil = models.CharField(db_column='BAR_AFIL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipo_doc = models.CharField(db_column='TIPO_DOC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    no_doc = models.CharField(db_column='NO_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    his_cli = models.CharField(db_column='HIS_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t_estud = models.CharField(db_column='T_ESTUD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tip_cli = models.CharField(db_column='TIP_CLI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    confir = models.CharField(db_column='CONFIR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    comusu = models.CharField(db_column='COMUSU', max_length=15, blank=True, null=True)  # Field name made lowercase.
    comws = models.CharField(db_column='COMWS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='IMPORTE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tel_tur = models.CharField(db_column='TEL_TUR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    splan = models.CharField(db_column='SPLAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nlist = models.CharField(db_column='NLIST', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fecalta = models.DateField(db_column='FECALTA', blank=True, null=True)  # Field name made lowercase.
    horalta = models.CharField(db_column='HORALTA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    no_bono = models.CharField(db_column='NO_BONO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fo = models.CharField(db_column='FO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    coseg = models.DecimalField(db_column='COSEG', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    instderi = models.CharField(db_column='INSTDERI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    medderi = models.CharField(db_column='MEDDERI', max_length=4, blank=True, null=True)  # Field name made lowercase.
    autoriza = models.CharField(db_column='AUTORIZA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t_expon = models.CharField(db_column='T_EXPON', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pri_vez = models.CharField(db_column='PRI_VEZ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pri_esp = models.CharField(db_column='PRI_ESP', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ee1'


class Employeeprojects(models.Model):
    employeeid = models.ForeignKey('Employees', db_column='employeeid')
    projectid = models.ForeignKey('Project', db_column='projectid')
    pvalue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeeprojects'
        unique_together = (('employeeid', 'projectid'),)


class Employees(models.Model):
    employeeid = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    titleofcourtesy = models.CharField(max_length=25, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    regionid = models.ForeignKey('Region', db_column='regionid', blank=True, null=True)
    stateid = models.ForeignKey('States', db_column='stateid', blank=True, null=True)
    cityid = models.IntegerField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    homephone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reportsto = models.IntegerField(blank=True, null=True)
    photopath = models.CharField(max_length=255, blank=True, null=True)
    ssn = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Employeestate(models.Model):
    employeeid = models.ForeignKey(Employees, db_column='employeeid')
    stateid = models.ForeignKey('States', db_column='stateid')

    class Meta:
        managed = False
        db_table = 'employeestate'
        unique_together = (('employeeid', 'stateid'),)


class Employeeterritories(models.Model):
    employeeid = models.ForeignKey(Employees, db_column='employeeid')
    territoryid = models.ForeignKey('Territories', db_column='territoryid')

    class Meta:
        managed = False
        db_table = 'employeeterritories'
        unique_together = (('employeeid', 'territoryid'),)


class Empresa(models.Model):
    cod_emp = models.CharField(db_column='COD_EMP', max_length=4)  # Field name made lowercase.
    denomin = models.CharField(db_column='DENOMIN', max_length=30)  # Field name made lowercase.
    direcc = models.CharField(db_column='DIRECC', max_length=28)  # Field name made lowercase.
    localid = models.CharField(db_column='LOCALID', max_length=25)  # Field name made lowercase.
    cpost = models.SmallIntegerField(db_column='CPOST')  # Field name made lowercase.
    te_fax = models.CharField(db_column='TE_FAX', max_length=25)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=15)  # Field name made lowercase.
    iva_tipo = models.CharField(db_column='IVA_TIPO', max_length=2)  # Field name made lowercase.
    cod_nom = models.CharField(db_column='COD_NOM', max_length=4)  # Field name made lowercase.
    cod_tarif = models.CharField(db_column='COD_TARIF', max_length=4)  # Field name made lowercase.
    mod_int = models.CharField(db_column='MOD_INT', max_length=1)  # Field name made lowercase.
    mod_amb = models.CharField(db_column='MOD_AMB', max_length=1)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=4)  # Field name made lowercase.
    exc_mod = models.CharField(db_column='EXC_MOD', max_length=1)  # Field name made lowercase.
    mod_fac = models.CharField(db_column='MOD_FAC', max_length=3)  # Field name made lowercase.
    cod_val = models.CharField(db_column='COD_VAL', max_length=4)  # Field name made lowercase.
    cod_activ = models.CharField(db_column='COD_ACTIV', max_length=1)  # Field name made lowercase.
    gas_adm = models.DecimalField(db_column='GAS_ADM', max_digits=6, decimal_places=2)  # Field name made lowercase.
    coefurg = models.DecimalField(db_column='COEFURG', max_digits=5, decimal_places=2)  # Field name made lowercase.
    fac_min = models.DecimalField(db_column='FAC_MIN', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gran = models.CharField(db_column='GRAN', max_length=1)  # Field name made lowercase.
    capita = models.DecimalField(db_column='CAPITA', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ingbrut = models.CharField(db_column='INGBRUT', max_length=11)  # Field name made lowercase.
    ex_rib = models.CharField(db_column='EX_RIB', max_length=10)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.
    suspend = models.CharField(db_column='SUSPEND', max_length=1)  # Field name made lowercase.
    art = models.CharField(db_column='ART', max_length=1)  # Field name made lowercase.
    pyme = models.CharField(db_column='PYME', max_length=1)  # Field name made lowercase.
    ing_brut = models.CharField(db_column='ING_BRUT', max_length=2)  # Field name made lowercase.
    nro_prov = models.CharField(db_column='NRO_PROV', max_length=7)  # Field name made lowercase.
    descartab = models.CharField(db_column='DESCARTAB', max_length=1)  # Field name made lowercase.
    alias = models.CharField(db_column='ALIAS', max_length=30)  # Field name made lowercase.
    urgencoseg = models.CharField(db_column='URGENCOSEG', max_length=1)  # Field name made lowercase.
    liq_fac = models.CharField(db_column='LIQ_FAC', max_length=1)  # Field name made lowercase.
    pideautori = models.CharField(db_column='PIDEAUTORI', max_length=1)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA')  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class Espec(models.Model):
    cod_esp = models.CharField(db_column='COD_ESP', primary_key=True, unique=True, max_length=4)  # Field name made lowercase.
    nom_esp = models.CharField(db_column='NOM_ESP', max_length=40)  # Field name made lowercase.
    estad = models.CharField(db_column='ESTAD', max_length=1)  # Field name made lowercase.
    consosana = models.CharField(db_column='CONSOSANA', max_length=1)  # Field name made lowercase.
    puntuali = models.CharField(db_column='PUNTUALI', max_length=1)  # Field name made lowercase.
    sesiones = models.CharField(db_column='SESIONES', max_length=1)  # Field name made lowercase.
    semanal = models.CharField(db_column='SEMANAL', max_length=1)  # Field name made lowercase.
    detec_pvez = models.CharField(db_column='DETEC_PVEZ', max_length=1)  # Field name made lowercase.
    ctrl_limi = models.CharField(db_column='CTRL_LIMI', max_length=1)  # Field name made lowercase.
    ctrl_cant = models.IntegerField(db_column='CTRL_CANT')  # Field name made lowercase.
    ctrl_peri = models.SmallIntegerField(db_column='CTRL_PERI')  # Field name made lowercase.
    calendar = models.CharField(db_column='CALENDAR', max_length=1)  # Field name made lowercase.
    servcaja = models.CharField(db_column='SERVCAJA', max_length=1)  # Field name made lowercase.
    lugar = models.CharField(db_column='LUGAR', max_length=3)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'espec'


class Estudios(models.Model):
    nro_estu = models.CharField(db_column='NRO_ESTU', unique=True, max_length=5, blank=True, null=True)  # Field name made lowercase.
    nom_estu = models.CharField(db_column='NOM_ESTU', max_length=40, blank=True, null=True)  # Field name made lowercase.
    duracion = models.CharField(db_column='DURACION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    superpone = models.CharField(db_column='SUPERPONE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gen_prot = models.CharField(db_column='GEN_PROT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prot_de = models.CharField(db_column='PROT_DE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    complej = models.CharField(db_column='COMPLEJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA', blank=True, null=True)  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estudios'


class Estudoc(models.Model):
    cod_med = models.CharField(db_column='COD_MED', max_length=4)  # Field name made lowercase.
    nro_estu = models.CharField(db_column='NRO_ESTU', max_length=5)  # Field name made lowercase.
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4)  # Field name made lowercase.
    nom_estu = models.CharField(db_column='NOM_ESTU', max_length=40)  # Field name made lowercase.
    tiempo = models.CharField(db_column='TIEMPO', max_length=3)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estudoc'


class Events(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    recurrent = models.CharField(max_length=1, blank=True, null=True)
    period = models.CharField(max_length=1, blank=True, null=True)
    users = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Excepc(models.Model):
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=5)  # Field name made lowercase.
    cod = models.CharField(db_column='COD', max_length=8)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=40)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1)  # Field name made lowercase.
    cod_hon = models.CharField(db_column='COD_HON', max_length=2)  # Field name made lowercase.
    cod_gas = models.CharField(db_column='COD_GAS', max_length=2)  # Field name made lowercase.
    esp_int = models.DecimalField(db_column='ESP_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu_int = models.DecimalField(db_column='AYU_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu2_int = models.DecimalField(db_column='AYU2_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ane_int = models.DecimalField(db_column='ANE_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    extr_int = models.DecimalField(db_column='EXTR_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gqui_int = models.DecimalField(db_column='GQUI_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gext_int = models.DecimalField(db_column='GEXT_INT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    esp_amb = models.DecimalField(db_column='ESP_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu_amb = models.DecimalField(db_column='AYU_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ayu2_amb = models.DecimalField(db_column='AYU2_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ane_amb = models.DecimalField(db_column='ANE_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    extr_amb = models.DecimalField(db_column='EXTR_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gqui_amb = models.DecimalField(db_column='GQUI_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gext_amb = models.DecimalField(db_column='GEXT_AMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA')  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'excepc'


class Excos(models.Model):
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15)  # Field name made lowercase.
    cod_nom = models.CharField(db_column='COD_NOM', max_length=8)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=40)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1)  # Field name made lowercase.
    valfint = models.DecimalField(db_column='VALFINT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    valfamb = models.DecimalField(db_column='VALFAMB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    valpint = models.DecimalField(db_column='VALPINT', max_digits=6, decimal_places=2)  # Field name made lowercase.
    valpamb = models.DecimalField(db_column='VALPAMB', max_digits=6, decimal_places=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'excos'


class Exsupest(models.Model):
    nro_estu = models.CharField(db_column='NRO_ESTU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nom_estu = models.CharField(db_column='NOM_ESTU', max_length=40, blank=True, null=True)  # Field name made lowercase.
    duracion = models.CharField(db_column='DURACION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    superpone = models.CharField(db_column='SUPERPONE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA', blank=True, null=True)  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exsupest'


class Feriado(models.Model):
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA', blank=True, null=True)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feriado'


class FilesTable(models.Model):
    fileid = models.IntegerField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    binaryvalue = models.TextField(blank=True, null=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    filetype = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files_table'


class Foxuser(models.Model):
    type = models.CharField(db_column='TYPE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=12, blank=True, primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=24, blank=True, null=True)  # Field name made lowercase.
    readonly = models.CharField(db_column='READONLY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ckval = models.IntegerField(db_column='CKVAL', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateField(db_column='UPDATED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foxuser'


class Hexcepc(models.Model):
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7, blank=True, null=True)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cod = models.CharField(db_column='COD', max_length=8, blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_hon = models.CharField(db_column='COD_HON', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_gas = models.CharField(db_column='COD_GAS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    esp_int = models.DecimalField(db_column='ESP_INT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ayu_int = models.DecimalField(db_column='AYU_INT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ayu2_int = models.DecimalField(db_column='AYU2_INT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ane_int = models.DecimalField(db_column='ANE_INT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extr_int = models.DecimalField(db_column='EXTR_INT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gqui_int = models.DecimalField(db_column='GQUI_INT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gext_int = models.DecimalField(db_column='GEXT_INT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    esp_amb = models.DecimalField(db_column='ESP_AMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ayu_amb = models.DecimalField(db_column='AYU_AMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ayu2_amb = models.DecimalField(db_column='AYU2_AMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ane_amb = models.DecimalField(db_column='ANE_AMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extr_amb = models.DecimalField(db_column='EXTR_AMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gqui_amb = models.DecimalField(db_column='GQUI_AMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gext_amb = models.DecimalField(db_column='GEXT_AMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA', blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI', blank=True, null=True)  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hexcepc'


class Hmodulo(models.Model):
    codmod = models.CharField(db_column='CODMOD', max_length=8, blank=True, null=True)  # Field name made lowercase.
    desc1 = models.CharField(db_column='DESC1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='DESC2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desc3 = models.CharField(db_column='DESC3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hono = models.DecimalField(db_column='HONO', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gastos = models.DecimalField(db_column='GASTOS', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA', blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI', blank=True, null=True)  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hmodulo'


class Instituc(models.Model):
    cod_inst = models.CharField(db_column='COD_INST', max_length=2)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30)  # Field name made lowercase.
    aliasmed = models.CharField(db_column='ALIASMED', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instituc'


class Modemp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7)  # Field name made lowercase.
    codmod = models.CharField(db_column='CODMOD', max_length=8)  # Field name made lowercase.
    cdcli = models.CharField(db_column='CDCLI', max_length=8)  # Field name made lowercase.
    hono = models.DecimalField(db_column='HONO', max_digits=10, decimal_places=2)  # Field name made lowercase.
    gastos = models.DecimalField(db_column='GASTOS', max_digits=10, decimal_places=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA')  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modemp'


class Modulo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codmod = models.CharField(db_column='CODMOD', max_length=8)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=50)  # Field name made lowercase.
    hono = models.DecimalField(db_column='HONO', max_digits=10, decimal_places=2)  # Field name made lowercase.
    gastos = models.DecimalField(db_column='GASTOS', max_digits=10, decimal_places=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modulo'


class Modulos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7)  # Field name made lowercase.
    ord_adm = models.CharField(db_column='ORD_ADM', max_length=14)  # Field name made lowercase.
    no_socio = models.CharField(db_column='NO_SOCIO', max_length=17)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    modulo = models.CharField(db_column='MODULO', max_length=8)  # Field name made lowercase.
    nommod = models.CharField(db_column='NOMMOD', max_length=50)  # Field name made lowercase.
    cod_med = models.CharField(db_column='COD_MED', max_length=4)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    fec_proc = models.DateField(db_column='FEC_PROC')  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15)  # Field name made lowercase.
    no_bono = models.CharField(db_column='NO_BONO', max_length=10)  # Field name made lowercase.
    urgencia = models.CharField(db_column='URGENCIA', max_length=1)  # Field name made lowercase.
    cant = models.IntegerField(db_column='CANT')  # Field name made lowercase.
    numero = models.BigIntegerField(db_column='NUMERO')  # Field name made lowercase.
    no_intern = models.BigIntegerField(db_column='NO_INTERN')  # Field name made lowercase.
    ipac_tot = models.DecimalField(db_column='IPAC_TOT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    coseg = models.DecimalField(db_column='COSEG', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tipocos = models.CharField(db_column='TIPOCOS', max_length=1)  # Field name made lowercase.
    tilde = models.CharField(db_column='TILDE', max_length=1)  # Field name made lowercase.
    letra = models.CharField(db_column='LETRA', max_length=1)  # Field name made lowercase.
    sucfac = models.SmallIntegerField(db_column='SUCFAC')  # Field name made lowercase.
    numfac = models.IntegerField(db_column='NUMFAC')  # Field name made lowercase.
    sucreci = models.SmallIntegerField(db_column='SUCRECI')  # Field name made lowercase.
    numreci = models.IntegerField(db_column='NUMRECI')  # Field name made lowercase.
    tipofac = models.CharField(db_column='TIPOFAC', max_length=2)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.
    paga = models.CharField(db_column='PAGA', max_length=1)  # Field name made lowercase.
    prueba = models.CharField(db_column='PRUEBA', max_length=10)  # Field name made lowercase.
    ord_fac = models.CharField(db_column='ORD_FAC', max_length=12)  # Field name made lowercase.
    inter = models.CharField(db_column='INTER', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modulos'


class Nomencla(models.Model):
    cod = models.CharField(db_column='COD', max_length=8)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=40)  # Field name made lowercase.
    detalle1 = models.CharField(db_column='DETALLE1', max_length=60)  # Field name made lowercase.
    detalle2 = models.CharField(db_column='DETALLE2', max_length=60)  # Field name made lowercase.
    hon_esp = models.DecimalField(db_column='HON_ESP', max_digits=12, decimal_places=2)  # Field name made lowercase.
    hon_ayu = models.DecimalField(db_column='HON_AYU', max_digits=12, decimal_places=2)  # Field name made lowercase.
    hon_2ayu = models.DecimalField(db_column='HON_2AYU', max_digits=12, decimal_places=2)  # Field name made lowercase.
    hon_ane = models.DecimalField(db_column='HON_ANE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    hon_extr = models.DecimalField(db_column='HON_EXTR', max_digits=12, decimal_places=2)  # Field name made lowercase.
    cod_hon = models.CharField(db_column='COD_HON', max_length=2)  # Field name made lowercase.
    gas_qui = models.DecimalField(db_column='GAS_QUI', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gas_extr = models.DecimalField(db_column='GAS_EXTR', max_digits=12, decimal_places=2)  # Field name made lowercase.
    cod_gas = models.CharField(db_column='COD_GAS', max_length=2)  # Field name made lowercase.
    cod_nom = models.CharField(db_column='COD_NOM', max_length=4)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.
    agrup = models.CharField(db_column='AGRUP', max_length=2)  # Field name made lowercase.
    pmo = models.CharField(db_column='PMO', max_length=1)  # Field name made lowercase.
    se_hace = models.CharField(db_column='SE_HACE', max_length=1)  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nomencla'


class Notasdres(models.Model):
    prod_ord = models.CharField(db_column='Prod_ord', max_length=4)  # Field name made lowercase.
    np_fdesde = models.DateTimeField(db_column='Np_fdesde')  # Field name made lowercase.
    np_fhasta = models.DateTimeField(db_column='Np_fhasta')  # Field name made lowercase.
    np_descri = models.CharField(db_column='Np_descri', max_length=255)  # Field name made lowercase.
    dia_modi = models.DateField()
    hs_modi = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'notasdres'


class Numtur(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'numtur'


class OrderDetails(models.Model):
    orderdetailsid = models.AutoField(primary_key=True)
    orderid = models.ForeignKey('Orders', db_column='orderid')
    productid = models.ForeignKey('Products', db_column='productid')
    unitprice = models.DecimalField(max_digits=16, decimal_places=4)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=16, decimal_places=2)
    totalprice = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_details'


class Orders(models.Model):
    orderid = models.IntegerField(primary_key=True)
    customerid = models.ForeignKey(Customers, db_column='customerid', blank=True, null=True)
    employeeid = models.ForeignKey(Employees, db_column='employeeid', blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)
    requireddate = models.DateField(blank=True, null=True)
    shippeddate = models.DateField(blank=True, null=True)
    shipvia = models.IntegerField(blank=True, null=True)
    freight = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    priceorder = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    shipcountry = models.CharField(max_length=15, blank=True, null=True)
    shipregion = models.IntegerField(blank=True, null=True)
    shipstate = models.CharField(max_length=2, blank=True, null=True)
    shipcity = models.IntegerField(blank=True, null=True)
    shipname = models.CharField(max_length=40, blank=True, null=True)
    shipaddress = models.CharField(max_length=60, blank=True, null=True)
    shippostalcode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Param(models.Model):
    nom_param = models.CharField(db_column='NOM_PARAM', max_length=38, blank=True, null=True)  # Field name made lowercase.
    valor = models.CharField(db_column='VALOR', max_length=38, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'param'


class Planes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=4)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=50)  # Field name made lowercase.
    fec_susp = models.DateField(db_column='FEC_SUSP')  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.
    tipo_iva = models.CharField(db_column='TIPO_IVA', max_length=3)  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    dia_modi = models.DateField()
    dia_alta = models.DateField()

    class Meta:
        managed = False
        db_table = 'planes'


class Pp(models.Model):
    codigo = models.BigIntegerField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase.
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dia_tur = models.DateField(db_column='DIA_TUR', blank=True, null=True)  # Field name made lowercase.
    hora_tur = models.CharField(db_column='HORA_TUR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    min_tur = models.CharField(db_column='MIN_TUR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pac_tur = models.CharField(db_column='PAC_TUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    o_social = models.CharField(db_column='O_SOCIAL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nro_afil = models.CharField(db_column='NRO_AFIL', max_length=22, blank=True, null=True)  # Field name made lowercase.
    bar_afil = models.CharField(db_column='BAR_AFIL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipo_doc = models.CharField(db_column='TIPO_DOC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    no_doc = models.CharField(db_column='NO_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    his_cli = models.CharField(db_column='HIS_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t_estud = models.CharField(db_column='T_ESTUD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tip_cli = models.CharField(db_column='TIP_CLI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    confir = models.CharField(db_column='CONFIR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    comusu = models.CharField(db_column='COMUSU', max_length=15, blank=True, null=True)  # Field name made lowercase.
    comws = models.CharField(db_column='COMWS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='IMPORTE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tel_tur = models.CharField(db_column='TEL_TUR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    splan = models.CharField(db_column='SPLAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nlist = models.CharField(db_column='NLIST', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fecalta = models.DateField(db_column='FECALTA', blank=True, null=True)  # Field name made lowercase.
    horalta = models.CharField(db_column='HORALTA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    no_bono = models.CharField(db_column='NO_BONO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fo = models.CharField(db_column='FO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    coseg = models.DecimalField(db_column='COSEG', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    instderi = models.CharField(db_column='INSTDERI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    medderi = models.CharField(db_column='MEDDERI', max_length=4, blank=True, null=True)  # Field name made lowercase.
    autoriza = models.CharField(db_column='AUTORIZA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t_expon = models.CharField(db_column='T_EXPON', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pri_vez = models.CharField(db_column='PRI_VEZ', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pp'


class Practica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_turnos = models.IntegerField(db_column='ID_TURNOS', blank=True, null=True)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=7)  # Field name made lowercase.
    ord_adm = models.CharField(db_column='ORD_ADM', max_length=14)  # Field name made lowercase.
    no_socio = models.CharField(db_column='NO_SOCIO', max_length=22)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30)  # Field name made lowercase.
    cod_med = models.CharField(db_column='COD_MED', max_length=4)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA')  # Field name made lowercase.
    fec_proc = models.DateField(db_column='FEC_PROC')  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15)  # Field name made lowercase.
    no_bono = models.CharField(db_column='NO_BONO', max_length=10)  # Field name made lowercase.
    urgencia = models.CharField(db_column='URGENCIA', max_length=1)  # Field name made lowercase.
    cod_nn = models.CharField(db_column='COD_NN', max_length=8)  # Field name made lowercase.
    cod_med1 = models.CharField(db_column='COD_MED1', max_length=4)  # Field name made lowercase.
    cod_med2 = models.CharField(db_column='COD_MED2', max_length=4)  # Field name made lowercase.
    cod_med3 = models.CharField(db_column='COD_MED3', max_length=4)  # Field name made lowercase.
    cod_med4 = models.CharField(db_column='COD_MED4', max_length=4)  # Field name made lowercase.
    cant = models.IntegerField(db_column='CANT')  # Field name made lowercase.
    subcod = models.CharField(db_column='SUBCOD', max_length=6)  # Field name made lowercase.
    cod_extr = models.CharField(db_column='COD_EXTR', max_length=4)  # Field name made lowercase.
    imp_1 = models.DecimalField(db_column='IMP_1', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imp_2 = models.DecimalField(db_column='IMP_2', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imp_3 = models.DecimalField(db_column='IMP_3', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imp_4 = models.DecimalField(db_column='IMP_4', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imp_extr = models.DecimalField(db_column='IMP_EXTR', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imp_gast = models.DecimalField(db_column='IMP_GAST', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imp_g_ex = models.DecimalField(db_column='IMP_G_EX', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imp_tot = models.DecimalField(db_column='IMP_TOT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    numero = models.BigIntegerField(db_column='NUMERO')  # Field name made lowercase.
    porc_1 = models.SmallIntegerField(db_column='PORC_1')  # Field name made lowercase.
    porc_2 = models.SmallIntegerField(db_column='PORC_2')  # Field name made lowercase.
    porc_3 = models.SmallIntegerField(db_column='PORC_3')  # Field name made lowercase.
    porc_4 = models.SmallIntegerField(db_column='PORC_4')  # Field name made lowercase.
    porc_extr = models.SmallIntegerField(db_column='PORC_EXTR')  # Field name made lowercase.
    porc_gast = models.SmallIntegerField(db_column='PORC_GAST')  # Field name made lowercase.
    porc_gext = models.SmallIntegerField(db_column='PORC_GEXT')  # Field name made lowercase.
    cod_gast = models.CharField(db_column='COD_GAST', max_length=4)  # Field name made lowercase.
    cod_gext = models.CharField(db_column='COD_GEXT', max_length=4)  # Field name made lowercase.
    no_intern = models.BigIntegerField(db_column='NO_INTERN')  # Field name made lowercase.
    coseg = models.DecimalField(db_column='COSEG', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tipocos = models.CharField(db_column='TIPOCOS', max_length=1)  # Field name made lowercase.
    tilde = models.CharField(db_column='TILDE', max_length=1)  # Field name made lowercase.
    letra = models.CharField(db_column='LETRA', max_length=1)  # Field name made lowercase.
    sucfac = models.SmallIntegerField(db_column='SUCFAC')  # Field name made lowercase.
    numfac = models.IntegerField(db_column='NUMFAC')  # Field name made lowercase.
    sucreci = models.SmallIntegerField(db_column='SUCRECI')  # Field name made lowercase.
    numreci = models.IntegerField(db_column='NUMRECI')  # Field name made lowercase.
    tipofac = models.CharField(db_column='TIPOFAC', max_length=2)  # Field name made lowercase.
    gravado = models.CharField(db_column='GRAVADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    fec_alta = models.DateTimeField(db_column='FEC_ALTA')  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    fec_modi = models.DateField(db_column='FEC_MODI')  # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1)  # Field name made lowercase.
    paga = models.CharField(db_column='PAGA', max_length=1)  # Field name made lowercase.
    prueba = models.CharField(db_column='PRUEBA', max_length=10)  # Field name made lowercase.
    modif = models.CharField(db_column='MODIF', max_length=1)  # Field name made lowercase.
    hono_1 = models.DecimalField(db_column='HONO_1', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hono_2 = models.DecimalField(db_column='HONO_2', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hono_3 = models.DecimalField(db_column='HONO_3', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hono_4 = models.DecimalField(db_column='HONO_4', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hono_5 = models.DecimalField(db_column='HONO_5', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hon_gas = models.DecimalField(db_column='HON_GAS', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hon_gex = models.DecimalField(db_column='HON_GEX', max_digits=10, decimal_places=2)  # Field name made lowercase.
    ord_fac = models.CharField(db_column='ORD_FAC', max_length=12)  # Field name made lowercase.
    ord2_fac = models.CharField(db_column='ORD2_FAC', max_length=12)  # Field name made lowercase.
    sucdep = models.SmallIntegerField(db_column='SUCDEP')  # Field name made lowercase.
    nrodep = models.IntegerField(db_column='NRODEP')  # Field name made lowercase.
    motdebi = models.CharField(db_column='MOTDEBI', max_length=4)  # Field name made lowercase.
    op1 = models.IntegerField(db_column='OP1')  # Field name made lowercase.
    op2 = models.IntegerField(db_column='OP2')  # Field name made lowercase.
    op3 = models.IntegerField(db_column='OP3')  # Field name made lowercase.
    op4 = models.IntegerField(db_column='OP4')  # Field name made lowercase.
    op5 = models.IntegerField(db_column='OP5')  # Field name made lowercase.
    op6 = models.IntegerField(db_column='OP6')  # Field name made lowercase.
    op7 = models.IntegerField(db_column='OP7')  # Field name made lowercase.
    imput = models.CharField(db_column='IMPUT', max_length=1)  # Field name made lowercase.
    hora_gra = models.CharField(db_column='HORA_GRA', max_length=8)  # Field name made lowercase.
    fec_tras = models.DateField(db_column='FEC_TRAS')  # Field name made lowercase.
    n_sec = models.CharField(db_column='N_SEC', max_length=3)  # Field name made lowercase.
    int_madre = models.CharField(db_column='INT_MADRE', max_length=10)  # Field name made lowercase.
    modop = models.CharField(db_column='MODOP', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'practica'


class Products(models.Model):
    productid = models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=40)
    supplierid = models.ForeignKey('Suppliers', db_column='supplierid', blank=True, null=True)
    categoryid = models.ForeignKey(Categories, db_column='categoryid', blank=True, null=True)
    quantityperunit = models.CharField(max_length=20, blank=True, null=True)
    unitprice = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    totalvalue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unitsinstock = models.IntegerField(blank=True, null=True)
    unitsonorder = models.IntegerField(blank=True, null=True)
    reorderlevel = models.IntegerField(blank=True, null=True)
    discontinued = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'products'


class Project(models.Model):
    projectid = models.IntegerField(primary_key=True)
    projectname = models.CharField(max_length=100, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    percentcomplete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class Reestesp(models.Model):
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4)  # Field name made lowercase.
    nro_estu = models.CharField(db_column='NRO_ESTU', max_length=5)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA')  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    nom_estu = models.CharField(db_column='NOM_ESTU', max_length=40)  # Field name made lowercase.
    dura_estu = models.CharField(db_column='DURA_ESTU', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reestesp'


class Region(models.Model):
    regionid = models.AutoField(primary_key=True)
    regiondescription = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class Releases(models.Model):
    releaseid = models.IntegerField(primary_key=True)
    companyid = models.ForeignKey(Companies, db_column='companyid', blank=True, null=True)
    deptid = models.ForeignKey(Departments, db_column='deptid', blank=True, null=True)
    accountid = models.ForeignKey(Account, db_column='accountid', blank=True, null=True)
    userlogin = models.CharField(max_length=10, blank=True, null=True)
    daterelease = models.DateField(blank=True, null=True)
    valuerelease = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'releases'


class SecApplication(models.Model):
    application_name = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_application'


class SecGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_groups'


class SecGroupsApplications(models.Model):
    group_id = models.IntegerField()
    application_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'sec_groups_applications'
        unique_together = (('group_id', 'application_name'),)


class SecUsers(models.Model):
    login = models.CharField(primary_key=True, max_length=30)
    pswd = models.CharField(max_length=30)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_users'


class SecUsersApplications(models.Model):
    login_user = models.CharField(max_length=30)
    application_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sec_users_applications'
        unique_together = (('login_user', 'application_name'),)


class SecUsersGroups(models.Model):
    login_user = models.CharField(max_length=100)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sec_users_groups'
        unique_together = (('login_user', 'group_id'),)


class Shippers(models.Model):
    shipperid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shippers'


class Sisturno(models.Model):
    usuario = models.CharField(db_column='USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='NIVEL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sisturno'


class States(models.Model):
    stateid = models.CharField(primary_key=True, max_length=2)
    statename = models.CharField(max_length=150, blank=True, null=True)
    regionid = models.ForeignKey(Region, db_column='regionid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class Suppliers(models.Model):
    supplierid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=40)
    contactname = models.CharField(max_length=30, blank=True, null=True)
    contacttitle = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    region = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class Tampstru(models.Model):
    field_name = models.CharField(db_column='FIELD_NAME', max_length=10)  # Field name made lowercase.
    field_type = models.CharField(db_column='FIELD_TYPE', max_length=1)  # Field name made lowercase.
    field_len = models.SmallIntegerField(db_column='FIELD_LEN')  # Field name made lowercase.
    field_dec = models.SmallIntegerField(db_column='FIELD_DEC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tampstru'


class Tasks(models.Model):
    taskid = models.AutoField(primary_key=True)
    projectid = models.IntegerField(blank=True, null=True)
    projectphase = models.CharField(max_length=100, blank=True, null=True)
    taskname = models.CharField(max_length=200, blank=True, null=True)
    milestone = models.CharField(max_length=1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    finishdate = models.DateField(blank=True, null=True)
    daysoverdue = models.IntegerField(blank=True, null=True)
    taskstatus = models.CharField(max_length=100, blank=True, null=True)
    percentcomplete = models.IntegerField(blank=True, null=True)
    taskpriority = models.CharField(max_length=100, blank=True, null=True)
    assignedto = models.IntegerField(blank=True, null=True)
    historynote = models.TextField(blank=True, null=True)
    datecreated = models.DateField(blank=True, null=True)
    datemodified = models.DateField(blank=True, null=True)
    recordowner = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.IntegerField(blank=True, null=True)
    taskpredecessor = models.CharField(max_length=200, blank=True, null=True)
    actualfinishdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class Tbajas(models.Model):
    codigo = models.BigIntegerField(db_column='CODIGO')  # Field name made lowercase.
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=4)  # Field name made lowercase.
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4)  # Field name made lowercase.
    dia_tur = models.DateField(db_column='DIA_TUR')  # Field name made lowercase.
    hora_tur = models.CharField(db_column='HORA_TUR', max_length=2)  # Field name made lowercase.
    min_tur = models.CharField(db_column='MIN_TUR', max_length=2)  # Field name made lowercase.
    pac_tur = models.CharField(db_column='PAC_TUR', max_length=30)  # Field name made lowercase.
    o_social = models.CharField(db_column='O_SOCIAL', max_length=15)  # Field name made lowercase.
    nro_afil = models.CharField(db_column='NRO_AFIL', max_length=22)  # Field name made lowercase.
    tipo_doc = models.CharField(db_column='TIPO_DOC', max_length=3)  # Field name made lowercase.
    no_doc = models.CharField(db_column='NO_DOC', max_length=9)  # Field name made lowercase.
    his_cli = models.CharField(db_column='HIS_CLI', max_length=10)  # Field name made lowercase.
    t_estud = models.CharField(db_column='T_ESTUD', max_length=20)  # Field name made lowercase.
    tip_cli = models.CharField(db_column='TIP_CLI', max_length=15)  # Field name made lowercase.
    confir = models.CharField(db_column='CONFIR', max_length=1)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC')  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    comusu = models.CharField(db_column='COMUSU', max_length=15)  # Field name made lowercase.
    comws = models.CharField(db_column='COMWS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    t_expon = models.CharField(db_column='T_EXPON', max_length=1)  # Field name made lowercase.
    pri_vez = models.CharField(db_column='PRI_VEZ', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbajas'


class Tbhora(models.Model):
    hora = models.CharField(db_column='HORA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v1 = models.CharField(db_column='V1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    v2 = models.CharField(db_column='V2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbhora'


class Tblfcon(models.Model):
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=1)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    t700 = models.CharField(db_column='T700', max_length=1)  # Field name made lowercase.
    t705 = models.CharField(db_column='T705', max_length=1)  # Field name made lowercase.
    t710 = models.CharField(db_column='T710', max_length=1)  # Field name made lowercase.
    t715 = models.CharField(db_column='T715', max_length=1)  # Field name made lowercase.
    t720 = models.CharField(db_column='T720', max_length=1)  # Field name made lowercase.
    t725 = models.CharField(db_column='T725', max_length=1)  # Field name made lowercase.
    t730 = models.CharField(db_column='T730', max_length=1)  # Field name made lowercase.
    t735 = models.CharField(db_column='T735', max_length=1)  # Field name made lowercase.
    t740 = models.CharField(db_column='T740', max_length=1)  # Field name made lowercase.
    t745 = models.CharField(db_column='T745', max_length=1)  # Field name made lowercase.
    t750 = models.CharField(db_column='T750', max_length=1)  # Field name made lowercase.
    t755 = models.CharField(db_column='T755', max_length=1)  # Field name made lowercase.
    t800 = models.CharField(db_column='T800', max_length=1)  # Field name made lowercase.
    t805 = models.CharField(db_column='T805', max_length=1)  # Field name made lowercase.
    t810 = models.CharField(db_column='T810', max_length=1)  # Field name made lowercase.
    t815 = models.CharField(db_column='T815', max_length=1)  # Field name made lowercase.
    t820 = models.CharField(db_column='T820', max_length=1)  # Field name made lowercase.
    t825 = models.CharField(db_column='T825', max_length=1)  # Field name made lowercase.
    t830 = models.CharField(db_column='T830', max_length=1)  # Field name made lowercase.
    t835 = models.CharField(db_column='T835', max_length=1)  # Field name made lowercase.
    t840 = models.CharField(db_column='T840', max_length=1)  # Field name made lowercase.
    t845 = models.CharField(db_column='T845', max_length=1)  # Field name made lowercase.
    t850 = models.CharField(db_column='T850', max_length=1)  # Field name made lowercase.
    t855 = models.CharField(db_column='T855', max_length=1)  # Field name made lowercase.
    t900 = models.CharField(db_column='T900', max_length=1)  # Field name made lowercase.
    t905 = models.CharField(db_column='T905', max_length=1)  # Field name made lowercase.
    t910 = models.CharField(db_column='T910', max_length=1)  # Field name made lowercase.
    t915 = models.CharField(db_column='T915', max_length=1)  # Field name made lowercase.
    t920 = models.CharField(db_column='T920', max_length=1)  # Field name made lowercase.
    t925 = models.CharField(db_column='T925', max_length=1)  # Field name made lowercase.
    t930 = models.CharField(db_column='T930', max_length=1)  # Field name made lowercase.
    t935 = models.CharField(db_column='T935', max_length=1)  # Field name made lowercase.
    t940 = models.CharField(db_column='T940', max_length=1)  # Field name made lowercase.
    t945 = models.CharField(db_column='T945', max_length=1)  # Field name made lowercase.
    t950 = models.CharField(db_column='T950', max_length=1)  # Field name made lowercase.
    t955 = models.CharField(db_column='T955', max_length=1)  # Field name made lowercase.
    t1000 = models.CharField(db_column='T1000', max_length=1)  # Field name made lowercase.
    t1005 = models.CharField(db_column='T1005', max_length=1)  # Field name made lowercase.
    t1010 = models.CharField(db_column='T1010', max_length=1)  # Field name made lowercase.
    t1015 = models.CharField(db_column='T1015', max_length=1)  # Field name made lowercase.
    t1020 = models.CharField(db_column='T1020', max_length=1)  # Field name made lowercase.
    t1025 = models.CharField(db_column='T1025', max_length=1)  # Field name made lowercase.
    t1030 = models.CharField(db_column='T1030', max_length=1)  # Field name made lowercase.
    t1035 = models.CharField(db_column='T1035', max_length=1)  # Field name made lowercase.
    t1040 = models.CharField(db_column='T1040', max_length=1)  # Field name made lowercase.
    t1045 = models.CharField(db_column='T1045', max_length=1)  # Field name made lowercase.
    t1050 = models.CharField(db_column='T1050', max_length=1)  # Field name made lowercase.
    t1055 = models.CharField(db_column='T1055', max_length=1)  # Field name made lowercase.
    t1100 = models.CharField(db_column='T1100', max_length=1)  # Field name made lowercase.
    t1105 = models.CharField(db_column='T1105', max_length=1)  # Field name made lowercase.
    t1110 = models.CharField(db_column='T1110', max_length=1)  # Field name made lowercase.
    t1115 = models.CharField(db_column='T1115', max_length=1)  # Field name made lowercase.
    t1120 = models.CharField(db_column='T1120', max_length=1)  # Field name made lowercase.
    t1125 = models.CharField(db_column='T1125', max_length=1)  # Field name made lowercase.
    t1130 = models.CharField(db_column='T1130', max_length=1)  # Field name made lowercase.
    t1135 = models.CharField(db_column='T1135', max_length=1)  # Field name made lowercase.
    t1140 = models.CharField(db_column='T1140', max_length=1)  # Field name made lowercase.
    t1145 = models.CharField(db_column='T1145', max_length=1)  # Field name made lowercase.
    t1150 = models.CharField(db_column='T1150', max_length=1)  # Field name made lowercase.
    t1155 = models.CharField(db_column='T1155', max_length=1)  # Field name made lowercase.
    t1200 = models.CharField(db_column='T1200', max_length=1)  # Field name made lowercase.
    t1205 = models.CharField(db_column='T1205', max_length=1)  # Field name made lowercase.
    t1210 = models.CharField(db_column='T1210', max_length=1)  # Field name made lowercase.
    t1215 = models.CharField(db_column='T1215', max_length=1)  # Field name made lowercase.
    t1220 = models.CharField(db_column='T1220', max_length=1)  # Field name made lowercase.
    t1225 = models.CharField(db_column='T1225', max_length=1)  # Field name made lowercase.
    t1230 = models.CharField(db_column='T1230', max_length=1)  # Field name made lowercase.
    t1235 = models.CharField(db_column='T1235', max_length=1)  # Field name made lowercase.
    t1240 = models.CharField(db_column='T1240', max_length=1)  # Field name made lowercase.
    t1245 = models.CharField(db_column='T1245', max_length=1)  # Field name made lowercase.
    t1250 = models.CharField(db_column='T1250', max_length=1)  # Field name made lowercase.
    t1255 = models.CharField(db_column='T1255', max_length=1)  # Field name made lowercase.
    t1300 = models.CharField(db_column='T1300', max_length=1)  # Field name made lowercase.
    t1305 = models.CharField(db_column='T1305', max_length=1)  # Field name made lowercase.
    t1310 = models.CharField(db_column='T1310', max_length=1)  # Field name made lowercase.
    t1315 = models.CharField(db_column='T1315', max_length=1)  # Field name made lowercase.
    t1320 = models.CharField(db_column='T1320', max_length=1)  # Field name made lowercase.
    t1325 = models.CharField(db_column='T1325', max_length=1)  # Field name made lowercase.
    t1330 = models.CharField(db_column='T1330', max_length=1)  # Field name made lowercase.
    t1335 = models.CharField(db_column='T1335', max_length=1)  # Field name made lowercase.
    t1340 = models.CharField(db_column='T1340', max_length=1)  # Field name made lowercase.
    t1345 = models.CharField(db_column='T1345', max_length=1)  # Field name made lowercase.
    t1350 = models.CharField(db_column='T1350', max_length=1)  # Field name made lowercase.
    t1355 = models.CharField(db_column='T1355', max_length=1)  # Field name made lowercase.
    t1400 = models.CharField(db_column='T1400', max_length=1)  # Field name made lowercase.
    t1405 = models.CharField(db_column='T1405', max_length=1)  # Field name made lowercase.
    t1410 = models.CharField(db_column='T1410', max_length=1)  # Field name made lowercase.
    t1415 = models.CharField(db_column='T1415', max_length=1)  # Field name made lowercase.
    t1420 = models.CharField(db_column='T1420', max_length=1)  # Field name made lowercase.
    t1425 = models.CharField(db_column='T1425', max_length=1)  # Field name made lowercase.
    t1430 = models.CharField(db_column='T1430', max_length=1)  # Field name made lowercase.
    t1435 = models.CharField(db_column='T1435', max_length=1)  # Field name made lowercase.
    t1440 = models.CharField(db_column='T1440', max_length=1)  # Field name made lowercase.
    t1445 = models.CharField(db_column='T1445', max_length=1)  # Field name made lowercase.
    t1450 = models.CharField(db_column='T1450', max_length=1)  # Field name made lowercase.
    t1455 = models.CharField(db_column='T1455', max_length=1)  # Field name made lowercase.
    t1500 = models.CharField(db_column='T1500', max_length=1)  # Field name made lowercase.
    t1505 = models.CharField(db_column='T1505', max_length=1)  # Field name made lowercase.
    t1510 = models.CharField(db_column='T1510', max_length=1)  # Field name made lowercase.
    t1515 = models.CharField(db_column='T1515', max_length=1)  # Field name made lowercase.
    t1520 = models.CharField(db_column='T1520', max_length=1)  # Field name made lowercase.
    t1525 = models.CharField(db_column='T1525', max_length=1)  # Field name made lowercase.
    t1530 = models.CharField(db_column='T1530', max_length=1)  # Field name made lowercase.
    t1535 = models.CharField(db_column='T1535', max_length=1)  # Field name made lowercase.
    t1540 = models.CharField(db_column='T1540', max_length=1)  # Field name made lowercase.
    t1545 = models.CharField(db_column='T1545', max_length=1)  # Field name made lowercase.
    t1550 = models.CharField(db_column='T1550', max_length=1)  # Field name made lowercase.
    t1555 = models.CharField(db_column='T1555', max_length=1)  # Field name made lowercase.
    t1600 = models.CharField(db_column='T1600', max_length=1)  # Field name made lowercase.
    t1605 = models.CharField(db_column='T1605', max_length=1)  # Field name made lowercase.
    t1610 = models.CharField(db_column='T1610', max_length=1)  # Field name made lowercase.
    t1615 = models.CharField(db_column='T1615', max_length=1)  # Field name made lowercase.
    t1620 = models.CharField(db_column='T1620', max_length=1)  # Field name made lowercase.
    t1625 = models.CharField(db_column='T1625', max_length=1)  # Field name made lowercase.
    t1630 = models.CharField(db_column='T1630', max_length=1)  # Field name made lowercase.
    t1635 = models.CharField(db_column='T1635', max_length=1)  # Field name made lowercase.
    t1640 = models.CharField(db_column='T1640', max_length=1)  # Field name made lowercase.
    t1645 = models.CharField(db_column='T1645', max_length=1)  # Field name made lowercase.
    t1650 = models.CharField(db_column='T1650', max_length=1)  # Field name made lowercase.
    t1655 = models.CharField(db_column='T1655', max_length=1)  # Field name made lowercase.
    t1700 = models.CharField(db_column='T1700', max_length=1)  # Field name made lowercase.
    t1705 = models.CharField(db_column='T1705', max_length=1)  # Field name made lowercase.
    t1710 = models.CharField(db_column='T1710', max_length=1)  # Field name made lowercase.
    t1715 = models.CharField(db_column='T1715', max_length=1)  # Field name made lowercase.
    t1720 = models.CharField(db_column='T1720', max_length=1)  # Field name made lowercase.
    t1725 = models.CharField(db_column='T1725', max_length=1)  # Field name made lowercase.
    t1730 = models.CharField(db_column='T1730', max_length=1)  # Field name made lowercase.
    t1735 = models.CharField(db_column='T1735', max_length=1)  # Field name made lowercase.
    t1740 = models.CharField(db_column='T1740', max_length=1)  # Field name made lowercase.
    t1745 = models.CharField(db_column='T1745', max_length=1)  # Field name made lowercase.
    t1750 = models.CharField(db_column='T1750', max_length=1)  # Field name made lowercase.
    t1755 = models.CharField(db_column='T1755', max_length=1)  # Field name made lowercase.
    t1800 = models.CharField(db_column='T1800', max_length=1)  # Field name made lowercase.
    t1805 = models.CharField(db_column='T1805', max_length=1)  # Field name made lowercase.
    t1810 = models.CharField(db_column='T1810', max_length=1)  # Field name made lowercase.
    t1815 = models.CharField(db_column='T1815', max_length=1)  # Field name made lowercase.
    t1820 = models.CharField(db_column='T1820', max_length=1)  # Field name made lowercase.
    t1825 = models.CharField(db_column='T1825', max_length=1)  # Field name made lowercase.
    t1830 = models.CharField(db_column='T1830', max_length=1)  # Field name made lowercase.
    t1835 = models.CharField(db_column='T1835', max_length=1)  # Field name made lowercase.
    t1840 = models.CharField(db_column='T1840', max_length=1)  # Field name made lowercase.
    t1845 = models.CharField(db_column='T1845', max_length=1)  # Field name made lowercase.
    t1850 = models.CharField(db_column='T1850', max_length=1)  # Field name made lowercase.
    t1855 = models.CharField(db_column='T1855', max_length=1)  # Field name made lowercase.
    t1900 = models.CharField(db_column='T1900', max_length=1)  # Field name made lowercase.
    t1905 = models.CharField(db_column='T1905', max_length=1)  # Field name made lowercase.
    t1910 = models.CharField(db_column='T1910', max_length=1)  # Field name made lowercase.
    t1915 = models.CharField(db_column='T1915', max_length=1)  # Field name made lowercase.
    t1920 = models.CharField(db_column='T1920', max_length=1)  # Field name made lowercase.
    t1925 = models.CharField(db_column='T1925', max_length=1)  # Field name made lowercase.
    t1930 = models.CharField(db_column='T1930', max_length=1)  # Field name made lowercase.
    t1935 = models.CharField(db_column='T1935', max_length=1)  # Field name made lowercase.
    t1940 = models.CharField(db_column='T1940', max_length=1)  # Field name made lowercase.
    t1945 = models.CharField(db_column='T1945', max_length=1)  # Field name made lowercase.
    t1950 = models.CharField(db_column='T1950', max_length=1)  # Field name made lowercase.
    t1955 = models.CharField(db_column='T1955', max_length=1)  # Field name made lowercase.
    t2000 = models.CharField(db_column='T2000', max_length=1)  # Field name made lowercase.
    t2005 = models.CharField(db_column='T2005', max_length=1)  # Field name made lowercase.
    t2010 = models.CharField(db_column='T2010', max_length=1)  # Field name made lowercase.
    t2015 = models.CharField(db_column='T2015', max_length=1)  # Field name made lowercase.
    t2020 = models.CharField(db_column='T2020', max_length=1)  # Field name made lowercase.
    t2025 = models.CharField(db_column='T2025', max_length=1)  # Field name made lowercase.
    t2030 = models.CharField(db_column='T2030', max_length=1)  # Field name made lowercase.
    t2035 = models.CharField(db_column='T2035', max_length=1)  # Field name made lowercase.
    t2040 = models.CharField(db_column='T2040', max_length=1)  # Field name made lowercase.
    t2045 = models.CharField(db_column='T2045', max_length=1)  # Field name made lowercase.
    t2050 = models.CharField(db_column='T2050', max_length=1)  # Field name made lowercase.
    t2055 = models.CharField(db_column='T2055', max_length=1)  # Field name made lowercase.
    t2100 = models.CharField(db_column='T2100', max_length=1)  # Field name made lowercase.
    t2105 = models.CharField(db_column='T2105', max_length=1)  # Field name made lowercase.
    t2110 = models.CharField(db_column='T2110', max_length=1)  # Field name made lowercase.
    t2115 = models.CharField(db_column='T2115', max_length=1)  # Field name made lowercase.
    t2120 = models.CharField(db_column='T2120', max_length=1)  # Field name made lowercase.
    t2125 = models.CharField(db_column='T2125', max_length=1)  # Field name made lowercase.
    t2130 = models.CharField(db_column='T2130', max_length=1)  # Field name made lowercase.
    t2135 = models.CharField(db_column='T2135', max_length=1)  # Field name made lowercase.
    t2140 = models.CharField(db_column='T2140', max_length=1)  # Field name made lowercase.
    t2145 = models.CharField(db_column='T2145', max_length=1)  # Field name made lowercase.
    t2150 = models.CharField(db_column='T2150', max_length=1)  # Field name made lowercase.
    t2155 = models.CharField(db_column='T2155', max_length=1)  # Field name made lowercase.
    t2200 = models.CharField(db_column='T2200', max_length=1)  # Field name made lowercase.
    t2205 = models.CharField(db_column='T2205', max_length=1)  # Field name made lowercase.
    t2210 = models.CharField(db_column='T2210', max_length=1)  # Field name made lowercase.
    t2215 = models.CharField(db_column='T2215', max_length=1)  # Field name made lowercase.
    t2220 = models.CharField(db_column='T2220', max_length=1)  # Field name made lowercase.
    t2225 = models.CharField(db_column='T2225', max_length=1)  # Field name made lowercase.
    t2230 = models.CharField(db_column='T2230', max_length=1)  # Field name made lowercase.
    t2235 = models.CharField(db_column='T2235', max_length=1)  # Field name made lowercase.
    t2240 = models.CharField(db_column='T2240', max_length=1)  # Field name made lowercase.
    t2245 = models.CharField(db_column='T2245', max_length=1)  # Field name made lowercase.
    t2250 = models.CharField(db_column='T2250', max_length=1)  # Field name made lowercase.
    t2255 = models.CharField(db_column='T2255', max_length=1)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblfcon'


class Tblfmed(models.Model):
    medico = models.CharField(db_column='MEDICO', max_length=4)  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=1)  # Field name made lowercase.
    espec = models.CharField(db_column='ESPEC', max_length=4)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    t700 = models.CharField(db_column='T700', max_length=1)  # Field name made lowercase.
    t705 = models.CharField(db_column='T705', max_length=1)  # Field name made lowercase.
    t710 = models.CharField(db_column='T710', max_length=1)  # Field name made lowercase.
    t715 = models.CharField(db_column='T715', max_length=1)  # Field name made lowercase.
    t720 = models.CharField(db_column='T720', max_length=1)  # Field name made lowercase.
    t725 = models.CharField(db_column='T725', max_length=1)  # Field name made lowercase.
    t730 = models.CharField(db_column='T730', max_length=1)  # Field name made lowercase.
    t735 = models.CharField(db_column='T735', max_length=1)  # Field name made lowercase.
    t740 = models.CharField(db_column='T740', max_length=1)  # Field name made lowercase.
    t745 = models.CharField(db_column='T745', max_length=1)  # Field name made lowercase.
    t750 = models.CharField(db_column='T750', max_length=1)  # Field name made lowercase.
    t755 = models.CharField(db_column='T755', max_length=1)  # Field name made lowercase.
    t800 = models.CharField(db_column='T800', max_length=1)  # Field name made lowercase.
    t805 = models.CharField(db_column='T805', max_length=1)  # Field name made lowercase.
    t810 = models.CharField(db_column='T810', max_length=1)  # Field name made lowercase.
    t815 = models.CharField(db_column='T815', max_length=1)  # Field name made lowercase.
    t820 = models.CharField(db_column='T820', max_length=1)  # Field name made lowercase.
    t825 = models.CharField(db_column='T825', max_length=1)  # Field name made lowercase.
    t830 = models.CharField(db_column='T830', max_length=1)  # Field name made lowercase.
    t835 = models.CharField(db_column='T835', max_length=1)  # Field name made lowercase.
    t840 = models.CharField(db_column='T840', max_length=1)  # Field name made lowercase.
    t845 = models.CharField(db_column='T845', max_length=1)  # Field name made lowercase.
    t850 = models.CharField(db_column='T850', max_length=1)  # Field name made lowercase.
    t855 = models.CharField(db_column='T855', max_length=1)  # Field name made lowercase.
    t900 = models.CharField(db_column='T900', max_length=1)  # Field name made lowercase.
    t905 = models.CharField(db_column='T905', max_length=1)  # Field name made lowercase.
    t910 = models.CharField(db_column='T910', max_length=1)  # Field name made lowercase.
    t915 = models.CharField(db_column='T915', max_length=1)  # Field name made lowercase.
    t920 = models.CharField(db_column='T920', max_length=1)  # Field name made lowercase.
    t925 = models.CharField(db_column='T925', max_length=1)  # Field name made lowercase.
    t930 = models.CharField(db_column='T930', max_length=1)  # Field name made lowercase.
    t935 = models.CharField(db_column='T935', max_length=1)  # Field name made lowercase.
    t940 = models.CharField(db_column='T940', max_length=1)  # Field name made lowercase.
    t945 = models.CharField(db_column='T945', max_length=1)  # Field name made lowercase.
    t950 = models.CharField(db_column='T950', max_length=1)  # Field name made lowercase.
    t955 = models.CharField(db_column='T955', max_length=1)  # Field name made lowercase.
    t1000 = models.CharField(db_column='T1000', max_length=1)  # Field name made lowercase.
    t1005 = models.CharField(db_column='T1005', max_length=1)  # Field name made lowercase.
    t1010 = models.CharField(db_column='T1010', max_length=1)  # Field name made lowercase.
    t1015 = models.CharField(db_column='T1015', max_length=1)  # Field name made lowercase.
    t1020 = models.CharField(db_column='T1020', max_length=1)  # Field name made lowercase.
    t1025 = models.CharField(db_column='T1025', max_length=1)  # Field name made lowercase.
    t1030 = models.CharField(db_column='T1030', max_length=1)  # Field name made lowercase.
    t1035 = models.CharField(db_column='T1035', max_length=1)  # Field name made lowercase.
    t1040 = models.CharField(db_column='T1040', max_length=1)  # Field name made lowercase.
    t1045 = models.CharField(db_column='T1045', max_length=1)  # Field name made lowercase.
    t1050 = models.CharField(db_column='T1050', max_length=1)  # Field name made lowercase.
    t1055 = models.CharField(db_column='T1055', max_length=1)  # Field name made lowercase.
    t1100 = models.CharField(db_column='T1100', max_length=1)  # Field name made lowercase.
    t1105 = models.CharField(db_column='T1105', max_length=1)  # Field name made lowercase.
    t1110 = models.CharField(db_column='T1110', max_length=1)  # Field name made lowercase.
    t1115 = models.CharField(db_column='T1115', max_length=1)  # Field name made lowercase.
    t1120 = models.CharField(db_column='T1120', max_length=1)  # Field name made lowercase.
    t1125 = models.CharField(db_column='T1125', max_length=1)  # Field name made lowercase.
    t1130 = models.CharField(db_column='T1130', max_length=1)  # Field name made lowercase.
    t1135 = models.CharField(db_column='T1135', max_length=1)  # Field name made lowercase.
    t1140 = models.CharField(db_column='T1140', max_length=1)  # Field name made lowercase.
    t1145 = models.CharField(db_column='T1145', max_length=1)  # Field name made lowercase.
    t1150 = models.CharField(db_column='T1150', max_length=1)  # Field name made lowercase.
    t1155 = models.CharField(db_column='T1155', max_length=1)  # Field name made lowercase.
    t1200 = models.CharField(db_column='T1200', max_length=1)  # Field name made lowercase.
    t1205 = models.CharField(db_column='T1205', max_length=1)  # Field name made lowercase.
    t1210 = models.CharField(db_column='T1210', max_length=1)  # Field name made lowercase.
    t1215 = models.CharField(db_column='T1215', max_length=1)  # Field name made lowercase.
    t1220 = models.CharField(db_column='T1220', max_length=1)  # Field name made lowercase.
    t1225 = models.CharField(db_column='T1225', max_length=1)  # Field name made lowercase.
    t1230 = models.CharField(db_column='T1230', max_length=1)  # Field name made lowercase.
    t1235 = models.CharField(db_column='T1235', max_length=1)  # Field name made lowercase.
    t1240 = models.CharField(db_column='T1240', max_length=1)  # Field name made lowercase.
    t1245 = models.CharField(db_column='T1245', max_length=1)  # Field name made lowercase.
    t1250 = models.CharField(db_column='T1250', max_length=1)  # Field name made lowercase.
    t1255 = models.CharField(db_column='T1255', max_length=1)  # Field name made lowercase.
    t1300 = models.CharField(db_column='T1300', max_length=1)  # Field name made lowercase.
    t1305 = models.CharField(db_column='T1305', max_length=1)  # Field name made lowercase.
    t1310 = models.CharField(db_column='T1310', max_length=1)  # Field name made lowercase.
    t1315 = models.CharField(db_column='T1315', max_length=1)  # Field name made lowercase.
    t1320 = models.CharField(db_column='T1320', max_length=1)  # Field name made lowercase.
    t1325 = models.CharField(db_column='T1325', max_length=1)  # Field name made lowercase.
    t1330 = models.CharField(db_column='T1330', max_length=1)  # Field name made lowercase.
    t1335 = models.CharField(db_column='T1335', max_length=1)  # Field name made lowercase.
    t1340 = models.CharField(db_column='T1340', max_length=1)  # Field name made lowercase.
    t1345 = models.CharField(db_column='T1345', max_length=1)  # Field name made lowercase.
    t1350 = models.CharField(db_column='T1350', max_length=1)  # Field name made lowercase.
    t1355 = models.CharField(db_column='T1355', max_length=1)  # Field name made lowercase.
    t1400 = models.CharField(db_column='T1400', max_length=1)  # Field name made lowercase.
    t1405 = models.CharField(db_column='T1405', max_length=1)  # Field name made lowercase.
    t1410 = models.CharField(db_column='T1410', max_length=1)  # Field name made lowercase.
    t1415 = models.CharField(db_column='T1415', max_length=1)  # Field name made lowercase.
    t1420 = models.CharField(db_column='T1420', max_length=1)  # Field name made lowercase.
    t1425 = models.CharField(db_column='T1425', max_length=1)  # Field name made lowercase.
    t1430 = models.CharField(db_column='T1430', max_length=1)  # Field name made lowercase.
    t1435 = models.CharField(db_column='T1435', max_length=1)  # Field name made lowercase.
    t1440 = models.CharField(db_column='T1440', max_length=1)  # Field name made lowercase.
    t1445 = models.CharField(db_column='T1445', max_length=1)  # Field name made lowercase.
    t1450 = models.CharField(db_column='T1450', max_length=1)  # Field name made lowercase.
    t1455 = models.CharField(db_column='T1455', max_length=1)  # Field name made lowercase.
    t1500 = models.CharField(db_column='T1500', max_length=1)  # Field name made lowercase.
    t1505 = models.CharField(db_column='T1505', max_length=1)  # Field name made lowercase.
    t1510 = models.CharField(db_column='T1510', max_length=1)  # Field name made lowercase.
    t1515 = models.CharField(db_column='T1515', max_length=1)  # Field name made lowercase.
    t1520 = models.CharField(db_column='T1520', max_length=1)  # Field name made lowercase.
    t1525 = models.CharField(db_column='T1525', max_length=1)  # Field name made lowercase.
    t1530 = models.CharField(db_column='T1530', max_length=1)  # Field name made lowercase.
    t1535 = models.CharField(db_column='T1535', max_length=1)  # Field name made lowercase.
    t1540 = models.CharField(db_column='T1540', max_length=1)  # Field name made lowercase.
    t1545 = models.CharField(db_column='T1545', max_length=1)  # Field name made lowercase.
    t1550 = models.CharField(db_column='T1550', max_length=1)  # Field name made lowercase.
    t1555 = models.CharField(db_column='T1555', max_length=1)  # Field name made lowercase.
    t1600 = models.CharField(db_column='T1600', max_length=1)  # Field name made lowercase.
    t1605 = models.CharField(db_column='T1605', max_length=1)  # Field name made lowercase.
    t1610 = models.CharField(db_column='T1610', max_length=1)  # Field name made lowercase.
    t1615 = models.CharField(db_column='T1615', max_length=1)  # Field name made lowercase.
    t1620 = models.CharField(db_column='T1620', max_length=1)  # Field name made lowercase.
    t1625 = models.CharField(db_column='T1625', max_length=1)  # Field name made lowercase.
    t1630 = models.CharField(db_column='T1630', max_length=1)  # Field name made lowercase.
    t1635 = models.CharField(db_column='T1635', max_length=1)  # Field name made lowercase.
    t1640 = models.CharField(db_column='T1640', max_length=1)  # Field name made lowercase.
    t1645 = models.CharField(db_column='T1645', max_length=1)  # Field name made lowercase.
    t1650 = models.CharField(db_column='T1650', max_length=1)  # Field name made lowercase.
    t1655 = models.CharField(db_column='T1655', max_length=1)  # Field name made lowercase.
    t1700 = models.CharField(db_column='T1700', max_length=1)  # Field name made lowercase.
    t1705 = models.CharField(db_column='T1705', max_length=1)  # Field name made lowercase.
    t1710 = models.CharField(db_column='T1710', max_length=1)  # Field name made lowercase.
    t1715 = models.CharField(db_column='T1715', max_length=1)  # Field name made lowercase.
    t1720 = models.CharField(db_column='T1720', max_length=1)  # Field name made lowercase.
    t1725 = models.CharField(db_column='T1725', max_length=1)  # Field name made lowercase.
    t1730 = models.CharField(db_column='T1730', max_length=1)  # Field name made lowercase.
    t1735 = models.CharField(db_column='T1735', max_length=1)  # Field name made lowercase.
    t1740 = models.CharField(db_column='T1740', max_length=1)  # Field name made lowercase.
    t1745 = models.CharField(db_column='T1745', max_length=1)  # Field name made lowercase.
    t1750 = models.CharField(db_column='T1750', max_length=1)  # Field name made lowercase.
    t1755 = models.CharField(db_column='T1755', max_length=1)  # Field name made lowercase.
    t1800 = models.CharField(db_column='T1800', max_length=1)  # Field name made lowercase.
    t1805 = models.CharField(db_column='T1805', max_length=1)  # Field name made lowercase.
    t1810 = models.CharField(db_column='T1810', max_length=1)  # Field name made lowercase.
    t1815 = models.CharField(db_column='T1815', max_length=1)  # Field name made lowercase.
    t1820 = models.CharField(db_column='T1820', max_length=1)  # Field name made lowercase.
    t1825 = models.CharField(db_column='T1825', max_length=1)  # Field name made lowercase.
    t1830 = models.CharField(db_column='T1830', max_length=1)  # Field name made lowercase.
    t1835 = models.CharField(db_column='T1835', max_length=1)  # Field name made lowercase.
    t1840 = models.CharField(db_column='T1840', max_length=1)  # Field name made lowercase.
    t1845 = models.CharField(db_column='T1845', max_length=1)  # Field name made lowercase.
    t1850 = models.CharField(db_column='T1850', max_length=1)  # Field name made lowercase.
    t1855 = models.CharField(db_column='T1855', max_length=1)  # Field name made lowercase.
    t1900 = models.CharField(db_column='T1900', max_length=1)  # Field name made lowercase.
    t1905 = models.CharField(db_column='T1905', max_length=1)  # Field name made lowercase.
    t1910 = models.CharField(db_column='T1910', max_length=1)  # Field name made lowercase.
    t1915 = models.CharField(db_column='T1915', max_length=1)  # Field name made lowercase.
    t1920 = models.CharField(db_column='T1920', max_length=1)  # Field name made lowercase.
    t1925 = models.CharField(db_column='T1925', max_length=1)  # Field name made lowercase.
    t1930 = models.CharField(db_column='T1930', max_length=1)  # Field name made lowercase.
    t1935 = models.CharField(db_column='T1935', max_length=1)  # Field name made lowercase.
    t1940 = models.CharField(db_column='T1940', max_length=1)  # Field name made lowercase.
    t1945 = models.CharField(db_column='T1945', max_length=1)  # Field name made lowercase.
    t1950 = models.CharField(db_column='T1950', max_length=1)  # Field name made lowercase.
    t1955 = models.CharField(db_column='T1955', max_length=1)  # Field name made lowercase.
    t2000 = models.CharField(db_column='T2000', max_length=1)  # Field name made lowercase.
    t2005 = models.CharField(db_column='T2005', max_length=1)  # Field name made lowercase.
    t2010 = models.CharField(db_column='T2010', max_length=1)  # Field name made lowercase.
    t2015 = models.CharField(db_column='T2015', max_length=1)  # Field name made lowercase.
    t2020 = models.CharField(db_column='T2020', max_length=1)  # Field name made lowercase.
    t2025 = models.CharField(db_column='T2025', max_length=1)  # Field name made lowercase.
    t2030 = models.CharField(db_column='T2030', max_length=1)  # Field name made lowercase.
    t2035 = models.CharField(db_column='T2035', max_length=1)  # Field name made lowercase.
    t2040 = models.CharField(db_column='T2040', max_length=1)  # Field name made lowercase.
    t2045 = models.CharField(db_column='T2045', max_length=1)  # Field name made lowercase.
    t2050 = models.CharField(db_column='T2050', max_length=1)  # Field name made lowercase.
    t2055 = models.CharField(db_column='T2055', max_length=1)  # Field name made lowercase.
    t2100 = models.CharField(db_column='T2100', max_length=1)  # Field name made lowercase.
    t2105 = models.CharField(db_column='T2105', max_length=1)  # Field name made lowercase.
    t2110 = models.CharField(db_column='T2110', max_length=1)  # Field name made lowercase.
    t2115 = models.CharField(db_column='T2115', max_length=1)  # Field name made lowercase.
    t2120 = models.CharField(db_column='T2120', max_length=1)  # Field name made lowercase.
    t2125 = models.CharField(db_column='T2125', max_length=1)  # Field name made lowercase.
    t2130 = models.CharField(db_column='T2130', max_length=1)  # Field name made lowercase.
    t2135 = models.CharField(db_column='T2135', max_length=1)  # Field name made lowercase.
    t2140 = models.CharField(db_column='T2140', max_length=1)  # Field name made lowercase.
    t2145 = models.CharField(db_column='T2145', max_length=1)  # Field name made lowercase.
    t2150 = models.CharField(db_column='T2150', max_length=1)  # Field name made lowercase.
    t2155 = models.CharField(db_column='T2155', max_length=1)  # Field name made lowercase.
    t2200 = models.CharField(db_column='T2200', max_length=1)  # Field name made lowercase.
    t2205 = models.CharField(db_column='T2205', max_length=1)  # Field name made lowercase.
    t2210 = models.CharField(db_column='T2210', max_length=1)  # Field name made lowercase.
    t2215 = models.CharField(db_column='T2215', max_length=1)  # Field name made lowercase.
    t2220 = models.CharField(db_column='T2220', max_length=1)  # Field name made lowercase.
    t2225 = models.CharField(db_column='T2225', max_length=1)  # Field name made lowercase.
    t2230 = models.CharField(db_column='T2230', max_length=1)  # Field name made lowercase.
    t2235 = models.CharField(db_column='T2235', max_length=1)  # Field name made lowercase.
    t2240 = models.CharField(db_column='T2240', max_length=1)  # Field name made lowercase.
    t2245 = models.CharField(db_column='T2245', max_length=1)  # Field name made lowercase.
    t2250 = models.CharField(db_column='T2250', max_length=1)  # Field name made lowercase.
    t2255 = models.CharField(db_column='T2255', max_length=1)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblfmed'


class Tblhcon(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t700 = models.CharField(db_column='T700', max_length=1)  # Field name made lowercase.
    t705 = models.CharField(db_column='T705', max_length=1)  # Field name made lowercase.
    t710 = models.CharField(db_column='T710', max_length=1)  # Field name made lowercase.
    t715 = models.CharField(db_column='T715', max_length=1)  # Field name made lowercase.
    t720 = models.CharField(db_column='T720', max_length=1)  # Field name made lowercase.
    t725 = models.CharField(db_column='T725', max_length=1)  # Field name made lowercase.
    t730 = models.CharField(db_column='T730', max_length=1)  # Field name made lowercase.
    t735 = models.CharField(db_column='T735', max_length=1)  # Field name made lowercase.
    t740 = models.CharField(db_column='T740', max_length=1)  # Field name made lowercase.
    t745 = models.CharField(db_column='T745', max_length=1)  # Field name made lowercase.
    t750 = models.CharField(db_column='T750', max_length=1)  # Field name made lowercase.
    t755 = models.CharField(db_column='T755', max_length=1)  # Field name made lowercase.
    t800 = models.CharField(db_column='T800', max_length=1)  # Field name made lowercase.
    t805 = models.CharField(db_column='T805', max_length=1)  # Field name made lowercase.
    t810 = models.CharField(db_column='T810', max_length=1)  # Field name made lowercase.
    t815 = models.CharField(db_column='T815', max_length=1)  # Field name made lowercase.
    t820 = models.CharField(db_column='T820', max_length=1)  # Field name made lowercase.
    t825 = models.CharField(db_column='T825', max_length=1)  # Field name made lowercase.
    t830 = models.CharField(db_column='T830', max_length=1)  # Field name made lowercase.
    t835 = models.CharField(db_column='T835', max_length=1)  # Field name made lowercase.
    t840 = models.CharField(db_column='T840', max_length=1)  # Field name made lowercase.
    t845 = models.CharField(db_column='T845', max_length=1)  # Field name made lowercase.
    t850 = models.CharField(db_column='T850', max_length=1)  # Field name made lowercase.
    t855 = models.CharField(db_column='T855', max_length=1)  # Field name made lowercase.
    t900 = models.CharField(db_column='T900', max_length=1)  # Field name made lowercase.
    t905 = models.CharField(db_column='T905', max_length=1)  # Field name made lowercase.
    t910 = models.CharField(db_column='T910', max_length=1)  # Field name made lowercase.
    t915 = models.CharField(db_column='T915', max_length=1)  # Field name made lowercase.
    t920 = models.CharField(db_column='T920', max_length=1)  # Field name made lowercase.
    t925 = models.CharField(db_column='T925', max_length=1)  # Field name made lowercase.
    t930 = models.CharField(db_column='T930', max_length=1)  # Field name made lowercase.
    t935 = models.CharField(db_column='T935', max_length=1)  # Field name made lowercase.
    t940 = models.CharField(db_column='T940', max_length=1)  # Field name made lowercase.
    t945 = models.CharField(db_column='T945', max_length=1)  # Field name made lowercase.
    t950 = models.CharField(db_column='T950', max_length=1)  # Field name made lowercase.
    t955 = models.CharField(db_column='T955', max_length=1)  # Field name made lowercase.
    t1000 = models.CharField(db_column='T1000', max_length=1)  # Field name made lowercase.
    t1005 = models.CharField(db_column='T1005', max_length=1)  # Field name made lowercase.
    t1010 = models.CharField(db_column='T1010', max_length=1)  # Field name made lowercase.
    t1015 = models.CharField(db_column='T1015', max_length=1)  # Field name made lowercase.
    t1020 = models.CharField(db_column='T1020', max_length=1)  # Field name made lowercase.
    t1025 = models.CharField(db_column='T1025', max_length=1)  # Field name made lowercase.
    t1030 = models.CharField(db_column='T1030', max_length=1)  # Field name made lowercase.
    t1035 = models.CharField(db_column='T1035', max_length=1)  # Field name made lowercase.
    t1040 = models.CharField(db_column='T1040', max_length=1)  # Field name made lowercase.
    t1045 = models.CharField(db_column='T1045', max_length=1)  # Field name made lowercase.
    t1050 = models.CharField(db_column='T1050', max_length=1)  # Field name made lowercase.
    t1055 = models.CharField(db_column='T1055', max_length=1)  # Field name made lowercase.
    t1100 = models.CharField(db_column='T1100', max_length=1)  # Field name made lowercase.
    t1105 = models.CharField(db_column='T1105', max_length=1)  # Field name made lowercase.
    t1110 = models.CharField(db_column='T1110', max_length=1)  # Field name made lowercase.
    t1115 = models.CharField(db_column='T1115', max_length=1)  # Field name made lowercase.
    t1120 = models.CharField(db_column='T1120', max_length=1)  # Field name made lowercase.
    t1125 = models.CharField(db_column='T1125', max_length=1)  # Field name made lowercase.
    t1130 = models.CharField(db_column='T1130', max_length=1)  # Field name made lowercase.
    t1135 = models.CharField(db_column='T1135', max_length=1)  # Field name made lowercase.
    t1140 = models.CharField(db_column='T1140', max_length=1)  # Field name made lowercase.
    t1145 = models.CharField(db_column='T1145', max_length=1)  # Field name made lowercase.
    t1150 = models.CharField(db_column='T1150', max_length=1)  # Field name made lowercase.
    t1155 = models.CharField(db_column='T1155', max_length=1)  # Field name made lowercase.
    t1200 = models.CharField(db_column='T1200', max_length=1)  # Field name made lowercase.
    t1205 = models.CharField(db_column='T1205', max_length=1)  # Field name made lowercase.
    t1210 = models.CharField(db_column='T1210', max_length=1)  # Field name made lowercase.
    t1215 = models.CharField(db_column='T1215', max_length=1)  # Field name made lowercase.
    t1220 = models.CharField(db_column='T1220', max_length=1)  # Field name made lowercase.
    t1225 = models.CharField(db_column='T1225', max_length=1)  # Field name made lowercase.
    t1230 = models.CharField(db_column='T1230', max_length=1)  # Field name made lowercase.
    t1235 = models.CharField(db_column='T1235', max_length=1)  # Field name made lowercase.
    t1240 = models.CharField(db_column='T1240', max_length=1)  # Field name made lowercase.
    t1245 = models.CharField(db_column='T1245', max_length=1)  # Field name made lowercase.
    t1250 = models.CharField(db_column='T1250', max_length=1)  # Field name made lowercase.
    t1255 = models.CharField(db_column='T1255', max_length=1)  # Field name made lowercase.
    t1300 = models.CharField(db_column='T1300', max_length=1)  # Field name made lowercase.
    t1305 = models.CharField(db_column='T1305', max_length=1)  # Field name made lowercase.
    t1310 = models.CharField(db_column='T1310', max_length=1)  # Field name made lowercase.
    t1315 = models.CharField(db_column='T1315', max_length=1)  # Field name made lowercase.
    t1320 = models.CharField(db_column='T1320', max_length=1)  # Field name made lowercase.
    t1325 = models.CharField(db_column='T1325', max_length=1)  # Field name made lowercase.
    t1330 = models.CharField(db_column='T1330', max_length=1)  # Field name made lowercase.
    t1335 = models.CharField(db_column='T1335', max_length=1)  # Field name made lowercase.
    t1340 = models.CharField(db_column='T1340', max_length=1)  # Field name made lowercase.
    t1345 = models.CharField(db_column='T1345', max_length=1)  # Field name made lowercase.
    t1350 = models.CharField(db_column='T1350', max_length=1)  # Field name made lowercase.
    t1355 = models.CharField(db_column='T1355', max_length=1)  # Field name made lowercase.
    t1400 = models.CharField(db_column='T1400', max_length=1)  # Field name made lowercase.
    t1405 = models.CharField(db_column='T1405', max_length=1)  # Field name made lowercase.
    t1410 = models.CharField(db_column='T1410', max_length=1)  # Field name made lowercase.
    t1415 = models.CharField(db_column='T1415', max_length=1)  # Field name made lowercase.
    t1420 = models.CharField(db_column='T1420', max_length=1)  # Field name made lowercase.
    t1425 = models.CharField(db_column='T1425', max_length=1)  # Field name made lowercase.
    t1430 = models.CharField(db_column='T1430', max_length=1)  # Field name made lowercase.
    t1435 = models.CharField(db_column='T1435', max_length=1)  # Field name made lowercase.
    t1440 = models.CharField(db_column='T1440', max_length=1)  # Field name made lowercase.
    t1445 = models.CharField(db_column='T1445', max_length=1)  # Field name made lowercase.
    t1450 = models.CharField(db_column='T1450', max_length=1)  # Field name made lowercase.
    t1455 = models.CharField(db_column='T1455', max_length=1)  # Field name made lowercase.
    t1500 = models.CharField(db_column='T1500', max_length=1)  # Field name made lowercase.
    t1505 = models.CharField(db_column='T1505', max_length=1)  # Field name made lowercase.
    t1510 = models.CharField(db_column='T1510', max_length=1)  # Field name made lowercase.
    t1515 = models.CharField(db_column='T1515', max_length=1)  # Field name made lowercase.
    t1520 = models.CharField(db_column='T1520', max_length=1)  # Field name made lowercase.
    t1525 = models.CharField(db_column='T1525', max_length=1)  # Field name made lowercase.
    t1530 = models.CharField(db_column='T1530', max_length=1)  # Field name made lowercase.
    t1535 = models.CharField(db_column='T1535', max_length=1)  # Field name made lowercase.
    t1540 = models.CharField(db_column='T1540', max_length=1)  # Field name made lowercase.
    t1545 = models.CharField(db_column='T1545', max_length=1)  # Field name made lowercase.
    t1550 = models.CharField(db_column='T1550', max_length=1)  # Field name made lowercase.
    t1555 = models.CharField(db_column='T1555', max_length=1)  # Field name made lowercase.
    t1600 = models.CharField(db_column='T1600', max_length=1)  # Field name made lowercase.
    t1605 = models.CharField(db_column='T1605', max_length=1)  # Field name made lowercase.
    t1610 = models.CharField(db_column='T1610', max_length=1)  # Field name made lowercase.
    t1615 = models.CharField(db_column='T1615', max_length=1)  # Field name made lowercase.
    t1620 = models.CharField(db_column='T1620', max_length=1)  # Field name made lowercase.
    t1625 = models.CharField(db_column='T1625', max_length=1)  # Field name made lowercase.
    t1630 = models.CharField(db_column='T1630', max_length=1)  # Field name made lowercase.
    t1635 = models.CharField(db_column='T1635', max_length=1)  # Field name made lowercase.
    t1640 = models.CharField(db_column='T1640', max_length=1)  # Field name made lowercase.
    t1645 = models.CharField(db_column='T1645', max_length=1)  # Field name made lowercase.
    t1650 = models.CharField(db_column='T1650', max_length=1)  # Field name made lowercase.
    t1655 = models.CharField(db_column='T1655', max_length=1)  # Field name made lowercase.
    t1700 = models.CharField(db_column='T1700', max_length=1)  # Field name made lowercase.
    t1705 = models.CharField(db_column='T1705', max_length=1)  # Field name made lowercase.
    t1710 = models.CharField(db_column='T1710', max_length=1)  # Field name made lowercase.
    t1715 = models.CharField(db_column='T1715', max_length=1)  # Field name made lowercase.
    t1720 = models.CharField(db_column='T1720', max_length=1)  # Field name made lowercase.
    t1725 = models.CharField(db_column='T1725', max_length=1)  # Field name made lowercase.
    t1730 = models.CharField(db_column='T1730', max_length=1)  # Field name made lowercase.
    t1735 = models.CharField(db_column='T1735', max_length=1)  # Field name made lowercase.
    t1740 = models.CharField(db_column='T1740', max_length=1)  # Field name made lowercase.
    t1745 = models.CharField(db_column='T1745', max_length=1)  # Field name made lowercase.
    t1750 = models.CharField(db_column='T1750', max_length=1)  # Field name made lowercase.
    t1755 = models.CharField(db_column='T1755', max_length=1)  # Field name made lowercase.
    t1800 = models.CharField(db_column='T1800', max_length=1)  # Field name made lowercase.
    t1805 = models.CharField(db_column='T1805', max_length=1)  # Field name made lowercase.
    t1810 = models.CharField(db_column='T1810', max_length=1)  # Field name made lowercase.
    t1815 = models.CharField(db_column='T1815', max_length=1)  # Field name made lowercase.
    t1820 = models.CharField(db_column='T1820', max_length=1)  # Field name made lowercase.
    t1825 = models.CharField(db_column='T1825', max_length=1)  # Field name made lowercase.
    t1830 = models.CharField(db_column='T1830', max_length=1)  # Field name made lowercase.
    t1835 = models.CharField(db_column='T1835', max_length=1)  # Field name made lowercase.
    t1840 = models.CharField(db_column='T1840', max_length=1)  # Field name made lowercase.
    t1845 = models.CharField(db_column='T1845', max_length=1)  # Field name made lowercase.
    t1850 = models.CharField(db_column='T1850', max_length=1)  # Field name made lowercase.
    t1855 = models.CharField(db_column='T1855', max_length=1)  # Field name made lowercase.
    t1900 = models.CharField(db_column='T1900', max_length=1)  # Field name made lowercase.
    t1905 = models.CharField(db_column='T1905', max_length=1)  # Field name made lowercase.
    t1910 = models.CharField(db_column='T1910', max_length=1)  # Field name made lowercase.
    t1915 = models.CharField(db_column='T1915', max_length=1)  # Field name made lowercase.
    t1920 = models.CharField(db_column='T1920', max_length=1)  # Field name made lowercase.
    t1925 = models.CharField(db_column='T1925', max_length=1)  # Field name made lowercase.
    t1930 = models.CharField(db_column='T1930', max_length=1)  # Field name made lowercase.
    t1935 = models.CharField(db_column='T1935', max_length=1)  # Field name made lowercase.
    t1940 = models.CharField(db_column='T1940', max_length=1)  # Field name made lowercase.
    t1945 = models.CharField(db_column='T1945', max_length=1)  # Field name made lowercase.
    t1950 = models.CharField(db_column='T1950', max_length=1)  # Field name made lowercase.
    t1955 = models.CharField(db_column='T1955', max_length=1)  # Field name made lowercase.
    t2000 = models.CharField(db_column='T2000', max_length=1)  # Field name made lowercase.
    t2005 = models.CharField(db_column='T2005', max_length=1)  # Field name made lowercase.
    t2010 = models.CharField(db_column='T2010', max_length=1)  # Field name made lowercase.
    t2015 = models.CharField(db_column='T2015', max_length=1)  # Field name made lowercase.
    t2020 = models.CharField(db_column='T2020', max_length=1)  # Field name made lowercase.
    t2025 = models.CharField(db_column='T2025', max_length=1)  # Field name made lowercase.
    t2030 = models.CharField(db_column='T2030', max_length=1)  # Field name made lowercase.
    t2035 = models.CharField(db_column='T2035', max_length=1)  # Field name made lowercase.
    t2040 = models.CharField(db_column='T2040', max_length=1)  # Field name made lowercase.
    t2045 = models.CharField(db_column='T2045', max_length=1)  # Field name made lowercase.
    t2050 = models.CharField(db_column='T2050', max_length=1)  # Field name made lowercase.
    t2055 = models.CharField(db_column='T2055', max_length=1)  # Field name made lowercase.
    t2100 = models.CharField(db_column='T2100', max_length=1)  # Field name made lowercase.
    t2105 = models.CharField(db_column='T2105', max_length=1)  # Field name made lowercase.
    t2110 = models.CharField(db_column='T2110', max_length=1)  # Field name made lowercase.
    t2115 = models.CharField(db_column='T2115', max_length=1)  # Field name made lowercase.
    t2120 = models.CharField(db_column='T2120', max_length=1)  # Field name made lowercase.
    t2125 = models.CharField(db_column='T2125', max_length=1)  # Field name made lowercase.
    t2130 = models.CharField(db_column='T2130', max_length=1)  # Field name made lowercase.
    t2135 = models.CharField(db_column='T2135', max_length=1)  # Field name made lowercase.
    t2140 = models.CharField(db_column='T2140', max_length=1)  # Field name made lowercase.
    t2145 = models.CharField(db_column='T2145', max_length=1)  # Field name made lowercase.
    t2150 = models.CharField(db_column='T2150', max_length=1)  # Field name made lowercase.
    t2155 = models.CharField(db_column='T2155', max_length=1)  # Field name made lowercase.
    t2200 = models.CharField(db_column='T2200', max_length=1)  # Field name made lowercase.
    t2205 = models.CharField(db_column='T2205', max_length=1)  # Field name made lowercase.
    t2210 = models.CharField(db_column='T2210', max_length=1)  # Field name made lowercase.
    t2215 = models.CharField(db_column='T2215', max_length=1)  # Field name made lowercase.
    t2220 = models.CharField(db_column='T2220', max_length=1)  # Field name made lowercase.
    t2225 = models.CharField(db_column='T2225', max_length=1)  # Field name made lowercase.
    t2230 = models.CharField(db_column='T2230', max_length=1)  # Field name made lowercase.
    t2235 = models.CharField(db_column='T2235', max_length=1)  # Field name made lowercase.
    t2240 = models.CharField(db_column='T2240', max_length=1)  # Field name made lowercase.
    t2245 = models.CharField(db_column='T2245', max_length=1)  # Field name made lowercase.
    t2250 = models.CharField(db_column='T2250', max_length=1)  # Field name made lowercase.
    t2255 = models.CharField(db_column='T2255', max_length=1)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblhcon'


class Tblhmed(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    medico = models.CharField(db_column='MEDICO', max_length=4)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    espec = models.CharField(db_column='ESPEC', max_length=4)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.
    t700 = models.CharField(db_column='T700', max_length=1)  # Field name made lowercase.
    t705 = models.CharField(db_column='T705', max_length=1)  # Field name made lowercase.
    t710 = models.CharField(db_column='T710', max_length=1)  # Field name made lowercase.
    t715 = models.CharField(db_column='T715', max_length=1)  # Field name made lowercase.
    t720 = models.CharField(db_column='T720', max_length=1)  # Field name made lowercase.
    t725 = models.CharField(db_column='T725', max_length=1)  # Field name made lowercase.
    t730 = models.CharField(db_column='T730', max_length=1)  # Field name made lowercase.
    t735 = models.CharField(db_column='T735', max_length=1)  # Field name made lowercase.
    t740 = models.CharField(db_column='T740', max_length=1)  # Field name made lowercase.
    t745 = models.CharField(db_column='T745', max_length=1)  # Field name made lowercase.
    t750 = models.CharField(db_column='T750', max_length=1)  # Field name made lowercase.
    t755 = models.CharField(db_column='T755', max_length=1)  # Field name made lowercase.
    t800 = models.CharField(db_column='T800', max_length=1)  # Field name made lowercase.
    t805 = models.CharField(db_column='T805', max_length=1)  # Field name made lowercase.
    t810 = models.CharField(db_column='T810', max_length=1)  # Field name made lowercase.
    t815 = models.CharField(db_column='T815', max_length=1)  # Field name made lowercase.
    t820 = models.CharField(db_column='T820', max_length=1)  # Field name made lowercase.
    t825 = models.CharField(db_column='T825', max_length=1)  # Field name made lowercase.
    t830 = models.CharField(db_column='T830', max_length=1)  # Field name made lowercase.
    t835 = models.CharField(db_column='T835', max_length=1)  # Field name made lowercase.
    t840 = models.CharField(db_column='T840', max_length=1)  # Field name made lowercase.
    t845 = models.CharField(db_column='T845', max_length=1)  # Field name made lowercase.
    t850 = models.CharField(db_column='T850', max_length=1)  # Field name made lowercase.
    t855 = models.CharField(db_column='T855', max_length=1)  # Field name made lowercase.
    t900 = models.CharField(db_column='T900', max_length=1)  # Field name made lowercase.
    t905 = models.CharField(db_column='T905', max_length=1)  # Field name made lowercase.
    t910 = models.CharField(db_column='T910', max_length=1)  # Field name made lowercase.
    t915 = models.CharField(db_column='T915', max_length=1)  # Field name made lowercase.
    t920 = models.CharField(db_column='T920', max_length=1)  # Field name made lowercase.
    t925 = models.CharField(db_column='T925', max_length=1)  # Field name made lowercase.
    t930 = models.CharField(db_column='T930', max_length=1)  # Field name made lowercase.
    t935 = models.CharField(db_column='T935', max_length=1)  # Field name made lowercase.
    t940 = models.CharField(db_column='T940', max_length=1)  # Field name made lowercase.
    t945 = models.CharField(db_column='T945', max_length=1)  # Field name made lowercase.
    t950 = models.CharField(db_column='T950', max_length=1)  # Field name made lowercase.
    t955 = models.CharField(db_column='T955', max_length=1)  # Field name made lowercase.
    t1000 = models.CharField(db_column='T1000', max_length=1)  # Field name made lowercase.
    t1005 = models.CharField(db_column='T1005', max_length=1)  # Field name made lowercase.
    t1010 = models.CharField(db_column='T1010', max_length=1)  # Field name made lowercase.
    t1015 = models.CharField(db_column='T1015', max_length=1)  # Field name made lowercase.
    t1020 = models.CharField(db_column='T1020', max_length=1)  # Field name made lowercase.
    t1025 = models.CharField(db_column='T1025', max_length=1)  # Field name made lowercase.
    t1030 = models.CharField(db_column='T1030', max_length=1)  # Field name made lowercase.
    t1035 = models.CharField(db_column='T1035', max_length=1)  # Field name made lowercase.
    t1040 = models.CharField(db_column='T1040', max_length=1)  # Field name made lowercase.
    t1045 = models.CharField(db_column='T1045', max_length=1)  # Field name made lowercase.
    t1050 = models.CharField(db_column='T1050', max_length=1)  # Field name made lowercase.
    t1055 = models.CharField(db_column='T1055', max_length=1)  # Field name made lowercase.
    t1100 = models.CharField(db_column='T1100', max_length=1)  # Field name made lowercase.
    t1105 = models.CharField(db_column='T1105', max_length=1)  # Field name made lowercase.
    t1110 = models.CharField(db_column='T1110', max_length=1)  # Field name made lowercase.
    t1115 = models.CharField(db_column='T1115', max_length=1)  # Field name made lowercase.
    t1120 = models.CharField(db_column='T1120', max_length=1)  # Field name made lowercase.
    t1125 = models.CharField(db_column='T1125', max_length=1)  # Field name made lowercase.
    t1130 = models.CharField(db_column='T1130', max_length=1)  # Field name made lowercase.
    t1135 = models.CharField(db_column='T1135', max_length=1)  # Field name made lowercase.
    t1140 = models.CharField(db_column='T1140', max_length=1)  # Field name made lowercase.
    t1145 = models.CharField(db_column='T1145', max_length=1)  # Field name made lowercase.
    t1150 = models.CharField(db_column='T1150', max_length=1)  # Field name made lowercase.
    t1155 = models.CharField(db_column='T1155', max_length=1)  # Field name made lowercase.
    t1200 = models.CharField(db_column='T1200', max_length=1)  # Field name made lowercase.
    t1205 = models.CharField(db_column='T1205', max_length=1)  # Field name made lowercase.
    t1210 = models.CharField(db_column='T1210', max_length=1)  # Field name made lowercase.
    t1215 = models.CharField(db_column='T1215', max_length=1)  # Field name made lowercase.
    t1220 = models.CharField(db_column='T1220', max_length=1)  # Field name made lowercase.
    t1225 = models.CharField(db_column='T1225', max_length=1)  # Field name made lowercase.
    t1230 = models.CharField(db_column='T1230', max_length=1)  # Field name made lowercase.
    t1235 = models.CharField(db_column='T1235', max_length=1)  # Field name made lowercase.
    t1240 = models.CharField(db_column='T1240', max_length=1)  # Field name made lowercase.
    t1245 = models.CharField(db_column='T1245', max_length=1)  # Field name made lowercase.
    t1250 = models.CharField(db_column='T1250', max_length=1)  # Field name made lowercase.
    t1255 = models.CharField(db_column='T1255', max_length=1)  # Field name made lowercase.
    t1300 = models.CharField(db_column='T1300', max_length=1)  # Field name made lowercase.
    t1305 = models.CharField(db_column='T1305', max_length=1)  # Field name made lowercase.
    t1310 = models.CharField(db_column='T1310', max_length=1)  # Field name made lowercase.
    t1315 = models.CharField(db_column='T1315', max_length=1)  # Field name made lowercase.
    t1320 = models.CharField(db_column='T1320', max_length=1)  # Field name made lowercase.
    t1325 = models.CharField(db_column='T1325', max_length=1)  # Field name made lowercase.
    t1330 = models.CharField(db_column='T1330', max_length=1)  # Field name made lowercase.
    t1335 = models.CharField(db_column='T1335', max_length=1)  # Field name made lowercase.
    t1340 = models.CharField(db_column='T1340', max_length=1)  # Field name made lowercase.
    t1345 = models.CharField(db_column='T1345', max_length=1)  # Field name made lowercase.
    t1350 = models.CharField(db_column='T1350', max_length=1)  # Field name made lowercase.
    t1355 = models.CharField(db_column='T1355', max_length=1)  # Field name made lowercase.
    t1400 = models.CharField(db_column='T1400', max_length=1)  # Field name made lowercase.
    t1405 = models.CharField(db_column='T1405', max_length=1)  # Field name made lowercase.
    t1410 = models.CharField(db_column='T1410', max_length=1)  # Field name made lowercase.
    t1415 = models.CharField(db_column='T1415', max_length=1)  # Field name made lowercase.
    t1420 = models.CharField(db_column='T1420', max_length=1)  # Field name made lowercase.
    t1425 = models.CharField(db_column='T1425', max_length=1)  # Field name made lowercase.
    t1430 = models.CharField(db_column='T1430', max_length=1)  # Field name made lowercase.
    t1435 = models.CharField(db_column='T1435', max_length=1)  # Field name made lowercase.
    t1440 = models.CharField(db_column='T1440', max_length=1)  # Field name made lowercase.
    t1445 = models.CharField(db_column='T1445', max_length=1)  # Field name made lowercase.
    t1450 = models.CharField(db_column='T1450', max_length=1)  # Field name made lowercase.
    t1455 = models.CharField(db_column='T1455', max_length=1)  # Field name made lowercase.
    t1500 = models.CharField(db_column='T1500', max_length=1)  # Field name made lowercase.
    t1505 = models.CharField(db_column='T1505', max_length=1)  # Field name made lowercase.
    t1510 = models.CharField(db_column='T1510', max_length=1)  # Field name made lowercase.
    t1515 = models.CharField(db_column='T1515', max_length=1)  # Field name made lowercase.
    t1520 = models.CharField(db_column='T1520', max_length=1)  # Field name made lowercase.
    t1525 = models.CharField(db_column='T1525', max_length=1)  # Field name made lowercase.
    t1530 = models.CharField(db_column='T1530', max_length=1)  # Field name made lowercase.
    t1535 = models.CharField(db_column='T1535', max_length=1)  # Field name made lowercase.
    t1540 = models.CharField(db_column='T1540', max_length=1)  # Field name made lowercase.
    t1545 = models.CharField(db_column='T1545', max_length=1)  # Field name made lowercase.
    t1550 = models.CharField(db_column='T1550', max_length=1)  # Field name made lowercase.
    t1555 = models.CharField(db_column='T1555', max_length=1)  # Field name made lowercase.
    t1600 = models.CharField(db_column='T1600', max_length=1)  # Field name made lowercase.
    t1605 = models.CharField(db_column='T1605', max_length=1)  # Field name made lowercase.
    t1610 = models.CharField(db_column='T1610', max_length=1)  # Field name made lowercase.
    t1615 = models.CharField(db_column='T1615', max_length=1)  # Field name made lowercase.
    t1620 = models.CharField(db_column='T1620', max_length=1)  # Field name made lowercase.
    t1625 = models.CharField(db_column='T1625', max_length=1)  # Field name made lowercase.
    t1630 = models.CharField(db_column='T1630', max_length=1)  # Field name made lowercase.
    t1635 = models.CharField(db_column='T1635', max_length=1)  # Field name made lowercase.
    t1640 = models.CharField(db_column='T1640', max_length=1)  # Field name made lowercase.
    t1645 = models.CharField(db_column='T1645', max_length=1)  # Field name made lowercase.
    t1650 = models.CharField(db_column='T1650', max_length=1)  # Field name made lowercase.
    t1655 = models.CharField(db_column='T1655', max_length=1)  # Field name made lowercase.
    t1700 = models.CharField(db_column='T1700', max_length=1)  # Field name made lowercase.
    t1705 = models.CharField(db_column='T1705', max_length=1)  # Field name made lowercase.
    t1710 = models.CharField(db_column='T1710', max_length=1)  # Field name made lowercase.
    t1715 = models.CharField(db_column='T1715', max_length=1)  # Field name made lowercase.
    t1720 = models.CharField(db_column='T1720', max_length=1)  # Field name made lowercase.
    t1725 = models.CharField(db_column='T1725', max_length=1)  # Field name made lowercase.
    t1730 = models.CharField(db_column='T1730', max_length=1)  # Field name made lowercase.
    t1735 = models.CharField(db_column='T1735', max_length=1)  # Field name made lowercase.
    t1740 = models.CharField(db_column='T1740', max_length=1)  # Field name made lowercase.
    t1745 = models.CharField(db_column='T1745', max_length=1)  # Field name made lowercase.
    t1750 = models.CharField(db_column='T1750', max_length=1)  # Field name made lowercase.
    t1755 = models.CharField(db_column='T1755', max_length=1)  # Field name made lowercase.
    t1800 = models.CharField(db_column='T1800', max_length=1)  # Field name made lowercase.
    t1805 = models.CharField(db_column='T1805', max_length=1)  # Field name made lowercase.
    t1810 = models.CharField(db_column='T1810', max_length=1)  # Field name made lowercase.
    t1815 = models.CharField(db_column='T1815', max_length=1)  # Field name made lowercase.
    t1820 = models.CharField(db_column='T1820', max_length=1)  # Field name made lowercase.
    t1825 = models.CharField(db_column='T1825', max_length=1)  # Field name made lowercase.
    t1830 = models.CharField(db_column='T1830', max_length=1)  # Field name made lowercase.
    t1835 = models.CharField(db_column='T1835', max_length=1)  # Field name made lowercase.
    t1840 = models.CharField(db_column='T1840', max_length=1)  # Field name made lowercase.
    t1845 = models.CharField(db_column='T1845', max_length=1)  # Field name made lowercase.
    t1850 = models.CharField(db_column='T1850', max_length=1)  # Field name made lowercase.
    t1855 = models.CharField(db_column='T1855', max_length=1)  # Field name made lowercase.
    t1900 = models.CharField(db_column='T1900', max_length=1)  # Field name made lowercase.
    t1905 = models.CharField(db_column='T1905', max_length=1)  # Field name made lowercase.
    t1910 = models.CharField(db_column='T1910', max_length=1)  # Field name made lowercase.
    t1915 = models.CharField(db_column='T1915', max_length=1)  # Field name made lowercase.
    t1920 = models.CharField(db_column='T1920', max_length=1)  # Field name made lowercase.
    t1925 = models.CharField(db_column='T1925', max_length=1)  # Field name made lowercase.
    t1930 = models.CharField(db_column='T1930', max_length=1)  # Field name made lowercase.
    t1935 = models.CharField(db_column='T1935', max_length=1)  # Field name made lowercase.
    t1940 = models.CharField(db_column='T1940', max_length=1)  # Field name made lowercase.
    t1945 = models.CharField(db_column='T1945', max_length=1)  # Field name made lowercase.
    t1950 = models.CharField(db_column='T1950', max_length=1)  # Field name made lowercase.
    t1955 = models.CharField(db_column='T1955', max_length=1)  # Field name made lowercase.
    t2000 = models.CharField(db_column='T2000', max_length=1)  # Field name made lowercase.
    t2005 = models.CharField(db_column='T2005', max_length=1)  # Field name made lowercase.
    t2010 = models.CharField(db_column='T2010', max_length=1)  # Field name made lowercase.
    t2015 = models.CharField(db_column='T2015', max_length=1)  # Field name made lowercase.
    t2020 = models.CharField(db_column='T2020', max_length=1)  # Field name made lowercase.
    t2025 = models.CharField(db_column='T2025', max_length=1)  # Field name made lowercase.
    t2030 = models.CharField(db_column='T2030', max_length=1)  # Field name made lowercase.
    t2035 = models.CharField(db_column='T2035', max_length=1)  # Field name made lowercase.
    t2040 = models.CharField(db_column='T2040', max_length=1)  # Field name made lowercase.
    t2045 = models.CharField(db_column='T2045', max_length=1)  # Field name made lowercase.
    t2050 = models.CharField(db_column='T2050', max_length=1)  # Field name made lowercase.
    t2055 = models.CharField(db_column='T2055', max_length=1)  # Field name made lowercase.
    t2100 = models.CharField(db_column='T2100', max_length=1)  # Field name made lowercase.
    t2105 = models.CharField(db_column='T2105', max_length=1)  # Field name made lowercase.
    t2110 = models.CharField(db_column='T2110', max_length=1)  # Field name made lowercase.
    t2115 = models.CharField(db_column='T2115', max_length=1)  # Field name made lowercase.
    t2120 = models.CharField(db_column='T2120', max_length=1)  # Field name made lowercase.
    t2125 = models.CharField(db_column='T2125', max_length=1)  # Field name made lowercase.
    t2130 = models.CharField(db_column='T2130', max_length=1)  # Field name made lowercase.
    t2135 = models.CharField(db_column='T2135', max_length=1)  # Field name made lowercase.
    t2140 = models.CharField(db_column='T2140', max_length=1)  # Field name made lowercase.
    t2145 = models.CharField(db_column='T2145', max_length=1)  # Field name made lowercase.
    t2150 = models.CharField(db_column='T2150', max_length=1)  # Field name made lowercase.
    t2155 = models.CharField(db_column='T2155', max_length=1)  # Field name made lowercase.
    t2200 = models.CharField(db_column='T2200', max_length=1)  # Field name made lowercase.
    t2205 = models.CharField(db_column='T2205', max_length=1)  # Field name made lowercase.
    t2210 = models.CharField(db_column='T2210', max_length=1)  # Field name made lowercase.
    t2215 = models.CharField(db_column='T2215', max_length=1)  # Field name made lowercase.
    t2220 = models.CharField(db_column='T2220', max_length=1)  # Field name made lowercase.
    t2225 = models.CharField(db_column='T2225', max_length=1)  # Field name made lowercase.
    t2230 = models.CharField(db_column='T2230', max_length=1)  # Field name made lowercase.
    t2235 = models.CharField(db_column='T2235', max_length=1)  # Field name made lowercase.
    t2240 = models.CharField(db_column='T2240', max_length=1)  # Field name made lowercase.
    t2245 = models.CharField(db_column='T2245', max_length=1)  # Field name made lowercase.
    t2250 = models.CharField(db_column='T2250', max_length=1)  # Field name made lowercase.
    t2255 = models.CharField(db_column='T2255', max_length=1)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    def getTurnos(self):
	lista=[]
	columnas=self.__dict__.keys()
	
	for col in columnas:
		if (col[0] == "t") and (self.__dict__[col] == "X"):
			lista.append(int(col[1:]))
	return sorted(lista)
			
		

    class Meta:
        managed = False
        db_table = 'tblhmed'


class Territories(models.Model):
    territoryid = models.CharField(primary_key=True, max_length=20)
    territorydescription = models.CharField(max_length=50)
    regionid = models.ForeignKey(Region, db_column='regionid')

    class Meta:
        managed = False
        db_table = 'territories'


class TurObs(models.Model):
    cod_tur = models.BigIntegerField(db_column='COD_TUR')  # Field name made lowercase.
    med_aut = models.CharField(db_column='MED_AUT', max_length=10)  # Field name made lowercase.
    diag_aut = models.CharField(db_column='DIAG_AUT', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tur_obs'


class TurResum(models.Model):
    codigo = models.BigIntegerField(db_column='CODIGO')  # Field name made lowercase.
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=4)  # Field name made lowercase.
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4)  # Field name made lowercase.
    dia_tur = models.DateField(db_column='DIA_TUR')  # Field name made lowercase.
    hora_tur = models.CharField(db_column='HORA_TUR', max_length=5)  # Field name made lowercase.
    min_tur = models.CharField(db_column='MIN_TUR', max_length=2)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tur_resum'


class Turcons(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    doctor = models.CharField(db_column='DOCTOR', max_length=4)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    espec = models.CharField(db_column='ESPEC', max_length=4)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC')  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=1)  # Field name made lowercase.
    h1 = models.CharField(db_column='H1', max_length=5)  # Field name made lowercase.
    h2 = models.CharField(db_column='H2', max_length=5)  # Field name made lowercase.
    h3 = models.CharField(db_column='H3', max_length=5)  # Field name made lowercase.
    h4 = models.CharField(db_column='H4', max_length=5)  # Field name made lowercase.
    h5 = models.CharField(db_column='H5', max_length=5)  # Field name made lowercase.
    h6 = models.CharField(db_column='H6', max_length=5)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    bajusu = models.CharField(db_column='BAJUSU', max_length=15)  # Field name made lowercase.
    bajws = models.CharField(db_column='BAJWS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turcons'


class Turconsdel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    doctor = models.CharField(db_column='DOCTOR', max_length=4)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    espec = models.CharField(db_column='ESPEC', max_length=4)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC')  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=1)  # Field name made lowercase.
    h1 = models.CharField(db_column='H1', max_length=5)  # Field name made lowercase.
    h2 = models.CharField(db_column='H2', max_length=5)  # Field name made lowercase.
    h3 = models.CharField(db_column='H3', max_length=5)  # Field name made lowercase.
    h4 = models.CharField(db_column='H4', max_length=5)  # Field name made lowercase.
    h5 = models.CharField(db_column='H5', max_length=5)  # Field name made lowercase.
    h6 = models.CharField(db_column='H6', max_length=5)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    bajusu = models.CharField(db_column='BAJUSU', max_length=15)  # Field name made lowercase.
    bajws = models.CharField(db_column='BAJWS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turconsdel'


class Turestu(models.Model):
    id_turno = models.IntegerField(db_column='ID_TURNO', blank=True, null=True)  # Field name made lowercase.
    nro_estu = models.CharField(db_column='NRO_ESTU', unique=True, max_length=5, blank=True, null=True)  # Field name made lowercase.
    usu_alta = models.CharField(db_column='USU_ALTA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_alta = models.CharField(db_column='WS_ALTA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_alta = models.DateField(db_column='DIA_ALTA', blank=True, null=True)  # Field name made lowercase.
    hs_alta = models.CharField(db_column='HS_ALTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turestu'


class Turmed(models.Model):
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    doctor = models.CharField(db_column='DOCTOR', max_length=4)  # Field name made lowercase.
    espec = models.CharField(db_column='ESPEC', max_length=4)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC')  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=1)  # Field name made lowercase.
    h1 = models.CharField(db_column='H1', max_length=5)  # Field name made lowercase.
    h2 = models.CharField(db_column='H2', max_length=5)  # Field name made lowercase.
    h3 = models.CharField(db_column='H3', max_length=5)  # Field name made lowercase.
    h4 = models.CharField(db_column='H4', max_length=5)  # Field name made lowercase.
    h5 = models.CharField(db_column='H5', max_length=5)  # Field name made lowercase.
    h6 = models.CharField(db_column='H6', max_length=5)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmed'


class Turmeddel(models.Model):
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    doctor = models.CharField(db_column='DOCTOR', max_length=4)  # Field name made lowercase.
    espec = models.CharField(db_column='ESPEC', max_length=4)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC')  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=1)  # Field name made lowercase.
    h1 = models.CharField(db_column='H1', max_length=5)  # Field name made lowercase.
    h2 = models.CharField(db_column='H2', max_length=5)  # Field name made lowercase.
    h3 = models.CharField(db_column='H3', max_length=5)  # Field name made lowercase.
    h4 = models.CharField(db_column='H4', max_length=5)  # Field name made lowercase.
    h5 = models.CharField(db_column='H5', max_length=5)  # Field name made lowercase.
    h6 = models.CharField(db_column='H6', max_length=5)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmeddel'


class Turnos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=9)  # Field name made lowercase.
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4)  # Field name made lowercase.
    dia_tur = models.DateField(db_column='DIA_TUR')  # Field name made lowercase.
    hora_tur = models.CharField(db_column='HORA_TUR', max_length=5)  # Field name made lowercase.
    min_tur = models.CharField(db_column='MIN_TUR', max_length=2)  # Field name made lowercase.
    dhm_tur = models.DateTimeField(db_column='DHM_TUR')  # Field name made lowercase.
    id_chc = models.IntegerField(db_column='ID_CHC')  # Field name made lowercase.
    o_social = models.CharField(db_column='O_SOCIAL', max_length=15)  # Field name made lowercase.
    nro_afil = models.CharField(db_column='NRO_AFIL', max_length=22)  # Field name made lowercase.
    bar_afil = models.CharField(db_column='BAR_AFIL', max_length=2)  # Field name made lowercase.
    tipo_doc = models.CharField(db_column='TIPO_DOC', max_length=3)  # Field name made lowercase.
    no_doc = models.CharField(db_column='NO_DOC', max_length=9)  # Field name made lowercase.
    t_estud = models.CharField(db_column='T_ESTUD', max_length=5)  # Field name made lowercase.
    tip_cli = models.CharField(db_column='TIP_CLI', max_length=3)  # Field name made lowercase.
    confir = models.CharField(db_column='CONFIR', max_length=1)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC')  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    comusu = models.CharField(db_column='COMUSU', max_length=15)  # Field name made lowercase.
    comws = models.CharField(db_column='COMWS', max_length=3)  # Field name made lowercase.
    importe = models.DecimalField(db_column='IMPORTE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tel_tur = models.CharField(db_column='TEL_TUR', max_length=20)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15)  # Field name made lowercase.
    splan = models.CharField(db_column='SPLAN', max_length=15)  # Field name made lowercase.
    nlist = models.CharField(db_column='NLIST', max_length=10)  # Field name made lowercase.
    fecalta = models.DateField(db_column='FECALTA')  # Field name made lowercase.
    horalta = models.CharField(db_column='HORALTA', max_length=8)  # Field name made lowercase.
    no_bono = models.CharField(db_column='NO_BONO', max_length=10)  # Field name made lowercase.
    fo = models.CharField(db_column='FO', max_length=1)  # Field name made lowercase.
    coseg = models.DecimalField(db_column='COSEG', max_digits=7, decimal_places=2)  # Field name made lowercase.
    instderi = models.CharField(db_column='INSTDERI', max_length=2)  # Field name made lowercase.
    medderi = models.CharField(db_column='MEDDERI', max_length=4)  # Field name made lowercase.
    autoriza = models.CharField(db_column='AUTORIZA', max_length=10)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    t_expon = models.CharField(db_column='T_EXPON', max_length=1)  # Field name made lowercase.
    pri_vez = models.CharField(db_column='PRI_VEZ', max_length=1)  # Field name made lowercase.
    pri_esp = models.CharField(db_column='PRI_ESP', max_length=1)  # Field name made lowercase.
    pri_vezat = models.CharField(db_column='PRI_VEZAT', max_length=1)  # Field name made lowercase.
    pri_espat = models.CharField(db_column='PRI_ESPAT', max_length=1)  # Field name made lowercase.
    insertado = models.CharField(db_column='INSERTADO', max_length=1)  # Field name made lowercase.
    gravado = models.CharField(db_column='GRAVADO', max_length=2)  # Field name made lowercase.
    observ = models.CharField(db_column='Observ', max_length=240)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnos'


class Turnosdel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=9)  # Field name made lowercase.
    cod_esp = models.CharField(db_column='COD_ESP', max_length=4)  # Field name made lowercase.
    dia_tur = models.DateField(db_column='DIA_TUR')  # Field name made lowercase.
    hora_tur = models.CharField(db_column='HORA_TUR', max_length=5)  # Field name made lowercase.
    min_tur = models.CharField(db_column='MIN_TUR', max_length=2)  # Field name made lowercase.
    dhm_tur = models.DateTimeField(db_column='DHM_TUR')  # Field name made lowercase.
    id_chc = models.IntegerField(db_column='ID_CHC')  # Field name made lowercase.
    o_social = models.CharField(db_column='O_SOCIAL', max_length=15)  # Field name made lowercase.
    nro_afil = models.CharField(db_column='NRO_AFIL', max_length=22)  # Field name made lowercase.
    bar_afil = models.CharField(db_column='BAR_AFIL', max_length=2)  # Field name made lowercase.
    tipo_doc = models.CharField(db_column='TIPO_DOC', max_length=3)  # Field name made lowercase.
    no_doc = models.CharField(db_column='NO_DOC', max_length=9)  # Field name made lowercase.
    t_estud = models.CharField(db_column='T_ESTUD', max_length=20)  # Field name made lowercase.
    tip_cli = models.CharField(db_column='TIP_CLI', max_length=3)  # Field name made lowercase.
    confir = models.CharField(db_column='CONFIR', max_length=1)  # Field name made lowercase.
    consult = models.CharField(db_column='CONSULT', max_length=4)  # Field name made lowercase.
    frec = models.SmallIntegerField(db_column='FREC')  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3)  # Field name made lowercase.
    comusu = models.CharField(db_column='COMUSU', max_length=15)  # Field name made lowercase.
    comws = models.CharField(db_column='COMWS', max_length=3)  # Field name made lowercase.
    importe = models.DecimalField(db_column='IMPORTE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tel_tur = models.CharField(db_column='TEL_TUR', max_length=20)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=15)  # Field name made lowercase.
    splan = models.CharField(db_column='SPLAN', max_length=15)  # Field name made lowercase.
    nlist = models.CharField(db_column='NLIST', max_length=10)  # Field name made lowercase.
    fecalta = models.DateField(db_column='FECALTA')  # Field name made lowercase.
    horalta = models.CharField(db_column='HORALTA', max_length=8)  # Field name made lowercase.
    no_bono = models.CharField(db_column='NO_BONO', max_length=10)  # Field name made lowercase.
    fo = models.CharField(db_column='FO', max_length=1)  # Field name made lowercase.
    coseg = models.DecimalField(db_column='COSEG', max_digits=7, decimal_places=2)  # Field name made lowercase.
    instderi = models.CharField(db_column='INSTDERI', max_length=2)  # Field name made lowercase.
    medderi = models.CharField(db_column='MEDDERI', max_length=4)  # Field name made lowercase.
    autoriza = models.CharField(db_column='AUTORIZA', max_length=10)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI')  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5)  # Field name made lowercase.
    t_expon = models.CharField(db_column='T_EXPON', max_length=1)  # Field name made lowercase.
    pri_vez = models.CharField(db_column='PRI_VEZ', max_length=1)  # Field name made lowercase.
    pri_esp = models.CharField(db_column='PRI_ESP', max_length=1)  # Field name made lowercase.
    pri_vezat = models.CharField(db_column='PRI_VEZAT', max_length=1)  # Field name made lowercase.
    pri_espat = models.CharField(db_column='PRI_ESPAT', max_length=1)  # Field name made lowercase.
    insertado = models.CharField(db_column='INSERTADO', max_length=1)  # Field name made lowercase.
    gravado = models.CharField(db_column='GRAVADO', max_length=2)  # Field name made lowercase.
    observ = models.CharField(db_column='Observ', max_length=240)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnosdel'


class Usuario(models.Model):
    usuario = models.CharField(db_column='USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='NIVEL', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    consosana = models.CharField(db_column='CONSOSANA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'


class Wscon(models.Model):
    terminal = models.CharField(db_column='TERMINAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    consul = models.CharField(db_column='CONSUL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nom_con = models.CharField(db_column='NOM_CON', max_length=40, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws = models.CharField(db_column='WS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    usu_modi = models.CharField(db_column='USU_MODI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ws_modi = models.CharField(db_column='WS_MODI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dia_modi = models.DateField(db_column='DIA_MODI', blank=True, null=True)  # Field name made lowercase.
    hs_modi = models.CharField(db_column='HS_MODI', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wscon'


class Wstelef(models.Model):
    ws = models.CharField(db_column='WS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    semap = models.CharField(db_column='SEMAP', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wstelef'


class Youtube(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    video = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youtube'





class Entry(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    remind = models.BooleanField(default=False)

    def __unicode__(self):
        if self.title:
            return unicode(self.creator) + u" - " + self.title
        else:
            return unicode(self.creator) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return "<i>%s</i> - %s" % (self.title, self.snippet)
        else:
            return self.title
    short.allow_tags = True

    class Meta:
        verbose_name_plural = "entries"



### Admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ["creator", "date", "title", "snippet"]
    list_filter = ["creator"]

admin.site.register(Entry, EntryAdmin)
