from ui import *
from contacts import book


def change(*args, **kwargs):
    if args or kwargs:
        for arg in args:
            if not len(arg):
                print("Enter command again with name and phone please")
            else:
                for key in book.keys():
                    if arg[0] == key.name.casefold():
                        record = book.search_record(key)
                        record[key] = arg[1:]
