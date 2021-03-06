# Copyright (C) 2014  SocialCookies @IV/GII

# @anaprados @oskyar @torresj @josemlp91
# @franciscomanuel @rogegg  @pedroag  @melero90

# Aplicacion web, para gestionar pedidos de galletas,
# con fotos de Instagram y Twitter. 

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


from django.shortcuts import render
from django.http import HttpResponse
from socialcookies.forms import ContactForm
from socialcookies.forms import fotosPedido
from djangomako.shortcuts import render_to_response, render_to_string
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from collage import descargaAndPaste

import photos
import os



ficheros = os.listdir('./socialcookies/static/img-slider')	


def index(request):
	fotosE=os.listdir('./socialcookies/static/img/authors')
	fotosE.sort()

	return render_to_response('index.html',
    	{'path':'/static/',
    	'seccion': 'index',
    	'fich':ficheros,
    	'fotos':fotosE
    	})

def twitter(request):
	return render_to_response('index.html',
		{'path':'/static/',
    	'seccion': 'twitter',
    	'fich':ficheros})

    	
def mandaCorreo(titulo, contenido):

	#fromaddr = "socialcookies@gmail.com"
	#toaddr   = "socialcookies@gmail.com"

	#msg = MIMEMultipart ()
	#msg['From']    = fromaddr
	#msg['To']         = toaddr
	#msg['Subject'] = titulo

	#body = contenido
	#msg.attach (MIMEText (body, 'plain'))

	#server = smtplib.SMTP ('smtp.gmail.com', 587)
	#server.ehlo ()
	#server.starttls ()   # Para conexion cifrada
	#server.ehlo ()
	#server.login ("socialcookies", "IVsocialcookies")
	#text = msg.as_string ()
	#server.sendmail(fromaddr, toaddr, text)
	
	email = EmailMessage(titulo, contenido, to=['socialcookiesiv@gmail.com']) 
	email.attach_file('archivoSal.jpg')
	email.send()

tipoGalleta=0

def contacto(request):
	arrayFotos=[]
	

	if 'q' in  request.GET and request.GET['q']:
		get=request.GET['q']
		print (get)

	if request.method=='POST':
		
		formulario= fotosPedido(request.POST)
		formulario2=ContactForm(request.POST)
		galletas=""

		if (get=="1"):
			
				
			if formulario.is_valid(): 

				galletas=request.POST['hidden_field0']
				galletas=galletas.split('|')
				
				#Imprime url
				#print(galletas)
				global tipoGalleta
				tipoGalleta=galletas[-1]
				galletas.pop()

				tipoGalleta=tipoGalleta[-5]

				descargaAndPaste(galletas, "archivoSal.jpg")

		elif (get=="2"):

			print ("Enviar mensaje")
			titulo = 'Mensaje de contacto desde \"Social Cookies\"'
			contenido = request.POST['mensaje'] + "\n"
			contenido += 'Comunicarse a : ' + request.POST['correo'] + "\n"
			contenido += 'A escogido el tipo de galleta: ' "<" + str(tipoGalleta) + ">"

			mandaCorreo(titulo, contenido)
			
			return HttpResponseRedirect('/socialcookies')
		

	else:
			formulario = ContactForm()
			formulario2= fotosPedido()


	return render_to_response('index.html',
		{'path':'/static/',
		'seccion': 'contacto',
		'formulario':formulario,
		'formulario2': formulario2,
		"csrftoken": csrf(request)["csrf_token"],
		'fich':ficheros})
    	
#def pedido(request):
#	if request.method=='POST':
#		formu = PedidoForm(request.POST)
#		if formu.is_valid():
#			titulo = 'Mensaje de contacto desde \"Social Cookies\"'
#			contenido = 'Cliente: ' + formu.cleaned_data['nombre'] + "\n"
#			contenido += 'Direccion' + formu.cleaned_data['direccion'] + "\n"
#			contenido += 'Telefono' + formu.cleaned_data['telefono'] + "\n"
#			contenido += 'Correo' + formu.cleaned_data['correo']
#			mandaCorreo(titulo, contenido)
#			return HttpResponseRedirect('/socialcookies')
#	else:
#		formu = PedidoForm()
#
#	return render_to_response('index.html',
#		{'path':'/static/socialcookies/bootstrap/',
#		'seccion': 'contacto',
#		'formu':formu,
#		"csrftoken": csrf(request)["csrf_token"],
#		'fich':ficheros})
