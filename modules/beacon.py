#!/usr/bin/env python
"""
beacon.py - Finds someone to answer questions
Author: Jeff
About:
"""
import ConfigParser
import os
import time
import sys
from twilio.rest import TwilioRestClient

threshold = 15 * 60
quietStart = 20
quietEnd = 9
quietDays = ["Saturday","Sunday"]

def setup(self):
    loadDefaultConfig(self)

def beacon(phenny, input):

    if not hasattr(phenny.bot, "lastBeacon"):
        phenny.bot.lastBeacon = 0

    diff = time.time() - phenny.lastBeacon

    #If enough time has passed then send a becon
    if diff < threshold:
        nextBeacon = threshold - diff
        phenny.reply("Beacon sent already.  Next one can be sent in " + str(round(nextBeacon, 0)) + " seconds")
    elif int(time.strftime("%H")) > quietStart or int(time.strftime("%H")) < quietEnd:
        phenny.reply("Shhhhhhh, time to let the group sleep.")
    elif time.strftime("%A") in quietDays:
        phenny.reply("Weekend baby! They are all out partying")
    else:
        phenny.bot.lastBeacon = time.time()
        phenny.reply("Beaconning now.  Please be patient while we find someone...")

        sendBeacon(phenny,input)

beacon.commands = ["beacon"]

def sendBeacon(phenny, input):

    if len(phenny.beaconers) < 1:
        phenny.reply("Sorry I can't find anyone for you")
        return

    client = TwilioRestClient(account=phenny.aSid, token=phenny.authToken)

    for number in phenny.beaconers:
        client.sms.messages.create(to=number, from_="+17028002427", body="Sudo user " + input.nick + " requesting chat presence")


def loadDefaultConfig(self):
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('~/.phenny/beacon.cfg')])


    #Lets load the twilio info
    if not config.has_option("default","aSid") or not config.has_option("default","authToken"):
        print >> sys.stderr, "No valid aSid/authToken found"
    else:
        self.aSid = config.get("default","aSid")
        self.authToken = config.get("default","authToken")

    #Now lets load the beaconers
    if not config.has_option("beacon","beaconers"):
        self.beaconers = []
    else:
        self.beaconers = config.get("beacon","beaconers").split(",")

    return



