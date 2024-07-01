import sys
import os
import shutil
import time
from settings import *


def clear():
    print('\n'*shutil.get_terminal_size().lines)
    os.system('cls' if os.name == 'nt' else 'clear')


def instance(book):
    page_no = starting_page
    while page_no > 0:
        page_no = book[page_no]['page_type'](book[page_no])
    pass


def page(cur_page):
    if cur_page['clear']:
        clear()
    return cur_page['next']


def text():
    pass


def header():
    pass


def menu():
    pass


def choice():
    pass


def transition(cur_page):
    columns = shutil.get_terminal_size().columns
    start_line = int(shutil.get_terminal_size().lines/2 - cur_page['text'].count('\n')/2)
    cur_text = cur_page['text']  # .center(columns)
    if cur_page['clear']:
        clear()
    sys.stdout.write('\n'*start_line)
    if cur_page['delay'] > 0:
        for i in range(len(cur_text)-1):
            sys.stdout.write(cur_text[i])
            sys.stdout.flush()
            time.sleep(cur_page['delay'])
    else:
        sys.stdout.write(cur_text)
    sys.stdout.write('\n' * start_line)
    time.sleep(3)
    return cur_page['next']
