import sys
import os
import shutil
import time
from settings import *


def clear(cur_page):
    if cur_page['clear']:
        print('\n'*shutil.get_terminal_size().lines)
        os.system('cls' if os.name == 'nt' else 'clear')


def instance(book):
    page_no = starting_page
    while page_no > 0:
        page_no = book[page_no]['page_type'](book[page_no])
    pass


def composite(cur_page):
    clear(cur_page)
    for segment in cur_page['segments']:
        if segment['type'] == menu:
            cur_page['next'] = segment['type'](segment)
        else:
            segment['type'](segment)
        sys.stdout.write('\n')
    return cur_page['next']


def text(segment):
    sys.stdout.write(segment['text'])
    pass


def header(segment):
    columns = shutil.get_terminal_size().columns
    cur_text = segment['text'].center(columns)
    sys.stdout.write(cur_text)
    sys.stdout.write('\n')
    pass


def menu(segment):
    for i in range(len(segment['options'])):
        sys.stdout.write(str(i+1)+') ')
        sys.stdout.write(segment['options'][i]['text']+'\n')
    while True:
        try:
            selection = int(input())
            if int(selection)-1 not in range(len(segment['options'])):
                sys.stdout.write('\nPlease input a valid option')
            else:
                return segment['options'][int(selection)-1]['next']
        except ValueError:
            sys.stdout.write('\nPlease input a valid option')


def choice(segment):
    pass


def transition(cur_page):
    columns = shutil.get_terminal_size().columns
    start_line = int(shutil.get_terminal_size().lines/2 - cur_page['text'].count('\n')/2)
    cur_text = cur_page['text'].center(columns)
    clear(cur_page)
    sys.stdout.write('\n'*start_line)
    if 'delay' in cur_page.keys():
        for i in range(len(cur_text)-1):
            sys.stdout.write(cur_text[i])
            sys.stdout.flush()
            time.sleep(cur_page['delay'])
    else:
        sys.stdout.write(cur_text)
    sys.stdout.write('\n' * start_line)
    time.sleep(cur_page['sleep'])
    return cur_page['next']
