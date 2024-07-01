#!/usr/bin/python

from main import *

example_project = {
    1: {'page_type': transition,
        'text': 'Welcome to the Prototype!',
        'clear': True,
        'delay': 0,
        'next': 2},
    2: {'page_type': page,
        'segments': [{'type': 'header'},
                     {'type': 'menu'}],
        'clear': True,
        'next': 0},
}


instance(example_project)






