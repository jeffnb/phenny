#!/usr/bin/env python
"""
intro.py - Used to private message new users on announcements
Author: Jeff
About:
"""
import os
import random

managers = ['opus', 'mistergecko', 'nglorioso', 'mrogers']
harass = ['spring-sudo-bot']

def setup(self):
    fn = self.nick + '-' + self.config.host + '.intro.db'
    self.tell_filename = os.path.join(os.path.expanduser('~/.phenny'), fn)
    if not os.path.exists(self.tell_filename):
        try: f = open(self.tell_filename, 'w')
        except OSError: pass
        else:
            f.write('')
            f.close()


def intro(phenny, input):
    if input.nick in managers:
        return
    if input.nick in harass:
        phenny.reply(random.choice(['Oh lord','didn\'t I tell you to go away?','*sighs*','Your mom says hi', 'Your girlfriend says hi',
                                    'Seriously? Why do you keep coming back?']))
        return

    #Check to see if we have an intro and create it if not
    if not hasattr(phenny.bot, 'intro'):
        phenny.bot.intro = []

    #Now make sure we haven't intro'd since startup
    if not input.nick in phenny.bot.intro:
        phenny.msg(input.nick, "Welcome to " + input.sender)
        phenny.msg(input.nick, "Sudo is a group of computer science students at UNLV. The leaders are coders from the community dedicated to help out in the education system.")
        phenny.bot.intro.append(input.nick.lower())
    else:
        phenny.reply("Welcome back")


intro.rule = r'(.*)'
intro.event = 'JOIN'