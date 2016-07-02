# sanlucasTurnos
Ultima version de los turnos de San Lucas

#Requerimientos
Django 1.8
apt-get install language-pack-es

Instalar apache 2.0
#apt-get install apache2
Instalar python pip
#apt-get install python-pip
Instalar la versión de Django
#pip install Django==1.8.1
Instalar python mysql
#apt-get install python-mysqldb

Instalar mysql server

#apt-get install mysql-server

Configuracion Apache
/etc/apache2/sites-available/turnosapp.conf

Alias /static/ /home/produccion/sanlucas/turnosapp/templates/turnosapp/resources/

WSGIScriptAlias /turnosapp /home/produccion/sanlucas/sanlucas/wsgi.py
WSGIPythonPath /home/produccion/sanlucas

<Directory /home/produccion/sanlucas/sanlucas>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

<Directory /home/produccion/sanlucas/turnosapp/templates/turnosapp/resources/>
Require all granted
</Directory>


Habilitar sitio
#a2ensite turnosapp.conf

Instalar modulo wsgi
#apt-get install libapache2-mod-wsgi

Habilitar Mysql para visualizarse de afuera
#vi /etc/mysql/my.cf
replazar linea 
bind-address = 127.0.0.1 
por
bind-address = 0.0.0.0
