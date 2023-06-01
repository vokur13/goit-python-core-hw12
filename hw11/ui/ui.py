from collections import UserDict
from datetime import datetime, timedelta
import re


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.NUMBER_RECORDS = None
        self.value = 0

    def __next__(self):
        if self.value >= self.NUMBER_RECORDS:
            raise StopIteration
        self.value += 1
        return self.value

    def __iter__(self):
        return self

    def iterator(self, n):
        self.NUMBER_RECORDS = n
        if self.data:
            data_list = list(self.data)[:n]
            for key in data_list:
                print(key, self.data.get(key))
        else:
            print('No records found')

    def get_records(self):
        for key, value in self.data.items():
            print(key.name, value)

    def search_record(self, key):
        print(self.data.get(key))
        return self.data

    def add_record(self, record):
        self.data[record.name] = record.phone


class Record:
    def __init__(self, name, phone=None, b_day=None):
        if phone is None:
            phone = []
        if b_day is None:
            b_day = ''
        self.name = name
        self.phone = phone
        self.b_day = b_day

    def add_phone(self, item):
        if item not in self.phone:
            self.phone.append(item)
        else:
            print(f"Phone number {item} already in list")

    def remove_phone(self, item):
        if item in self.phone:
            self.phone.remove(item)
        else:
            print(f"Phone number {item} is not in list")

    def edit_phone(self, item):
        self.phone.clear()
        self.phone.append(item)

    def days_to_birthday(self):
        now = datetime.now()
        ts_now = now.timestamp()
        one_year_interval = timedelta(weeks=52)
        bd = datetime.strptime(self.b_day, '%d-%m-%Y').date()
        ts_bd_0 = datetime(year=now.year, month=bd.month, day=bd.day).timestamp()
        delta = (ts_bd_0 - ts_now) // (24 * 3600) + 1
        if delta > 0:
            print(f'Days until next birthday: {int(delta)}')
        elif delta < 0:
            print(f'Days until next birthday: {int(delta + one_year_interval.days + 1)}')
        else:
            print('Say Happy Birthday to contact today!')


class Field:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ', ' + str(value)
        return result


class Name(Field):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name


class Phone(Field):
    def __init__(self):
        super().__init__()
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone):
        if phone.isdigit():
            self.__value = phone
        else:
            print('Only digits are accepted')

    def __str__(self):
        return self.__value


class Birthday(Field):
    def __init__(self):
        super().__init__()
        self.__value = None
        self.data = {}

    def __setitem__(self, _, value):
        self.data[0] = [value]

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, b_day):
        regex = r'(\d\d)-(\d\d)-(\d\d\d\d)'
        if re.search(regex, b_day):
            self.__value = b_day
        else:
            raise ValueError('Only date in format DD-MM-YYYY is accepted')

    def __str__(self):
        return self.__value


record = Record('Boris')

phone = Phone()
phone[0] = '123456789'
phone[1] = '876544567'
print(phone[0], phone[1])

birthday = Birthday()
birthday[0] = '27-05-2000'
print(birthday[0])
record.b_day = birthday[0]
record.days_to_birthday()
