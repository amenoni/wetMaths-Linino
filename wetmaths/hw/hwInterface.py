#!/usr/bin/python
from sendMailbox import sendMailbox

def sweepMode():
    sendMailbox("sweep")

def waitingMode():
    sendMailbox("wait")

def shootPlayer(playerNr):
    sendMailbox("shoot %s" % playerNr)

def shootAll():
    sendMailbox("shootAll")
