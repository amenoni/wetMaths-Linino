# wetMaths-Linino

###WetMaths is an educational app to learn the multiplication tables. ###

3 Players using an Android App and a Arduino Based device that will launch a little party foam spray to the player that loses

# ADD LINK TO YOUTUBE

In this repo you will find the code for the Django app that runs in the Linux side of the Arduino Yun.

The repo for the Android App:

  https://github.com/amenoni/wetMaths-Android

The Arduino side code and the files for the 3D printed parts of the hardware is in:

https://github.com/amenoni/wetMaths-Arduino

**Installing the django server in the Yun.**

Install dependencies.
```
opkg update
opkg install python-sqlite3, python-expat, python-openssl, distribute
```
We use [Gunicorn](http://gunicorn.org/) to serve the Django app, we need to install it via python PIP, due to the restricted disk space
in the yun we need to manually download it in the SD card and then install it via easy_install.

Copy in the sdcard root the lastest version of Python Pip
https://pypi.python.org/pypi/pip#downloads

Create an *arduino* folder in the SD card and copy the contents of this repo *wetmaths* folder.

```
easy_install path_to_pip.tar.gz  --build-directory /mnt/sda1/
pip install gunicorn
```

We send messages to the Android Apps using [Firebase](https://www.firebase.com/), sign up and create a new database, edit *game/fire.py* file
and modify the URL to conect to your database.
```
firebase = firebase.FirebaseApplication('https://resplendent-torch-6152.firebaseio.com', None)
```

Edit *hw/hwInterface.py* file to activate the hardware. *active = True*
```
#Change to false to avoid hardware actions, insted send console messages
active = False
```

Edit *gunicorn_srv* file, in the first line put the path to your python compiler. 
```
#!/Users/amenoni/Desarrollo/WetMaths/WETENV2/bin/python2.7
```

Create or modify */etc/rc.local* file to launch the django app when the Yun starts.

```
./mnt/sda1/arduino/gunicorn_srv wetmaths.wsgi --bind 0.0.0.0:8000
```

***Open the Android App and set the device URL to your Yun ip adress in the 8000 port***
