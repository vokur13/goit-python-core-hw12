from ui import Name, Record
from contacts import book


def add(*args, **kwargs):
    if args or kwargs:
        for arg in args:
            if not len(arg) > 1:
                print("Enter command again with name and phone please")
            else:
                name = Name(arg[0].capitalize())
                record = Record(name)
                if arg[1:]:
                    record.add_phone(" ".join(arg[1:]))
                book.add_record(record)
