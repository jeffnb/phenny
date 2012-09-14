#!/usr/bin/env python
"""
becon.py - Finds someone to answer questions
Author: Jeff
About:
"""
import time

threshold = 15 * 60
lastBecon = 0

def becon(phenny, input):
    diff = time.time() - lastBecon

    #If enough time has passed then send a becon
    if diff > threshold:

        phenny.reply("Beconning now...")
    else:
        nextBecon = threshold - diff
        phenny.reply("Becon sent already.  Next one can be sent in " + nextBecon + "s")

becon.commands = ["becon"]
