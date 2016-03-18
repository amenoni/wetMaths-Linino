#!/usr/bin/python

import socket
import json

#usage
#from sendMailbox import sendMailbox
#sendMailbox('message')

def sendMailbox(msg):
    m = {'command':'raw'}
    m['data'] = str(msg)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 5700))
    s.sendall(json.dumps(m))
    s.close()
