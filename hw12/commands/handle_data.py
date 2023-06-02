from contacts import book


def save_data(*args, **kwargs):
    book.save_to_file()


def recovery_data(*args, **kwargs):
    book.read_from_file()
