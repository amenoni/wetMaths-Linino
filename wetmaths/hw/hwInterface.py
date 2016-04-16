#!/usr/bin/python
from sendMailbox import sendMailbox

#Change to false to avoid hardware actions, insted send console messages
active = False


def sweepMode():
    if active:
        sendMailbox("sweep")
    else:
        print "Sweep MODE"

def waitingMode():
    if active:
        sendMailbox("wait")
    else:
        print "Wait Mode"

def shootPlayer(playerNr):
    if active:
        sendMailbox("shoot %s" % playerNr)
    else:
        print "Shoot player %d" % playerNr

def shootAll():
    if active:
        sendMailbox("shootAll")
    else:
        print "Shoot All"
