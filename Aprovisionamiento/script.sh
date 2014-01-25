#!/bin/bash


#Actualizamos la maquina
sudo apt-get update
sudo apt-get upgrade

#Instalamos git
sudo apt-get install git -y

#instalamos python
sudo apt-get install python -y

#instalamos el gestor de modulos de python
sudo apt-get install python-pip -y

#Configuración e instalación de django
sudo pip install django

#instalacion de modulos de python
sudo pip install tweepy

#Clonamos el repositorio de GitHub
git clone https://github.com/IV-GII/SocialCookies.git

#nos movemos a la carpeta y lo lanzamos

cd SocialCookies/ENV1
source bin/activate
cd webcookies
sudo python manage.py runserver 80

