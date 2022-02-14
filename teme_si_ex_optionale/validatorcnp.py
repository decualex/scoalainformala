
import datetime

from stdnum.exceptions import *
from stdnum.util import clean, isdigits


def compact(number):
    return clean(number, ' -').strip()


def calc_check_digit(number):
    weights = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    check = sum(w * int(n) for w, n in zip(weights, number)) % 11
    return '1' if check == 10 else str(check)


def get_birth_date(number):

    number = compact(number)
    centuries = {
        '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000}
    year = int(number[1:3]) + centuries.get(number[0], 1900)
    month = int(number[3:5])
    day = int(number[5:7])
    try:
        return datetime.date(year, month, day)
    except ValueError:
        raise InvalidComponent()


def validate(number):
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if number[0] not in '123456789':
        raise InvalidComponent()
    if len(number) != 13:
        raise InvalidLength()
    get_birth_date(number)
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number


def is_valid(number):
    try:
        return bool(validate(number))
    except ValidationError:
        return False