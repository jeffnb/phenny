#!/usr/bin/env python
"""
harass.py - Harrass the spring bot
Author: Jeff
About:
"""
import random

targetBot = "spring-sudo-bot"

def harass(phenny, input):
    if input.nick == targetBot:
        msg = random.choice(('/me rolls eyes at '+targetBot, 'STFU ' + targetBot, '/me grumbles',
                             'how many gb of memory do you need to run?', 'Really? Java? In 2012?',
                            'you are the bastard child of C++ and the blob'))
        phenny.say(msg)


harass.rule = r'(.*)'

if __name__ == '__main__':
   print __doc__.strip()
