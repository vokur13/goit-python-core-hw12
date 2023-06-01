from contacts import book


def iterate(*args, **kwargs):
    for arg in args:
        book.iterator(int(arg[0]))
