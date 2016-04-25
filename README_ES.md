# wetMaths-Linino

###WetMaths es una aplicación educativa para aprender las tablas de multiplicaciones.

Consiste en 3 jugadores usando una aplicación Android y un dispositivo basado en arduino Yun el cual 
disparara un poco de espuma de cotillon a los jugadores que pierdan la partida en el juego.

#LINK A YOUTUBE

En este repositorio encontramos el codigo del servidor web que corre dentro del Linino del dispositivo Arduino Yun.

En este repositorio encontramos el codigo de la aplicación Android.


  https://github.com/amenoni/wetMaths-Android

Y en este otro el codigo del arduino que corre dentro del Arduino Yun, en este mismo repositorio tambien encontramos 
el diseño de las piezas impresas en 3D para el harware.

https://github.com/amenoni/wetMaths-Arduino

**Pasos para instalar el servidor web en el arduino Yun.**

Instalar dependencias.
```
opkg update
opkg install python-sqlite3, python-expat, python-openssl, distribute

```
Usamos [Gunicorn](http://gunicorn.org/) para servir la aplicación djando para poder instalarlo precisamos python Pip, debido a la 
restriccion de disco que tenemos en el Yun debemos descargarlo manualmente en la tarjeta SD para luego instalarlo en Yun

Copiar en la raiz de la tarjeta sd el archivo tar.gz de la ultima version de PIP
https://pypi.python.org/pypi/pip#downloads

crear una carpeta *arduino* y copiar el contenido de la carpeta wetmaths de este repositiorio

```
easy_install path_to_pip.tar.gz  --build-directory /mnt/sda1/
pip install gunicorn
```

La aplicación envia mensajes a los telefonos mediante [Firebase](https://www.firebase.com/), registrarse y crear una base, editar el archivo *game/fire.py* para modificar la url a tu aplicación firebase
```
firebase = firebase.FirebaseApplication('https://resplendent-torch-6152.firebaseio.com', None)
```

Editar el archivo *hw/hwInterface.py* para activar el hardware active = True
```
#Change to false to avoid hardware actions, insted send console messages
active = False
```

Editar el archivo *gunicorn_srv*, colocar en la primer linea el path hacia tu complilador de python
```
#!/Users/amenoni/Desarrollo/WetMaths/WETENV2/bin/python2.7
```

Crear o modificar el archivo */etc/rc.local* para lanzar automaticamente el servidor en el inicio del dispositivo.

```
./mnt/sda1/arduino/gunicorn_srv wetmaths.wsgi --bind 0.0.0.0:8000
```

***Abrir la aplicación Android y conectarla a la dirección del Yun en el puerto 8000***




