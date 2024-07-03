#!/usr/bin/python

from main import *

example_project = {
    1: {'page_type': transition,
        'text': 'Welcome to the Prototype!',
        'clear': True,
        'sleep': 2.5,
        'next': 2},
    2: {'page_type': composite,
        'segments': [{'type': header,
                      'text': 'Example Project'},
                     {'type': menu,
                      'options': [
                          {'text': 'New Game',
                           'next': 0},
                          {'text': 'Load Game',
                           'next': 0},
                          {'text': 'Settings',
                           'next': 0},
                          {'text': 'Quit',
                           'next': 0},
                      ]}],
        'clear': True,
        'next': 0},
}


instance(example_project)







