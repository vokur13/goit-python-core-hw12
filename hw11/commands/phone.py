from ui import *
from contacts import book


def phone(*args, **kwargs):
    if args or kwargs:
        for arg in args:
            if not len(arg):
                print("Enter command and name please")
            else:
                for key in book.keys():
                    if arg[0] == key.name.casefold():
                        book.search_record(key)
