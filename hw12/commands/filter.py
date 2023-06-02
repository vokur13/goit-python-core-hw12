from ui import *
from contacts import book


def handle_filter(*args, **kwargs):
    if args or kwargs:
        for arg in args:
            if not len(arg):
                print("Enter 'filter' and keys to find for")
            else:
                key = arg[0].casefold()
                book.find_filter(key)
