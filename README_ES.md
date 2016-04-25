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

