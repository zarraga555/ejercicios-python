# import datetime

# print(datetime.date.today())
# print(datetime.timedelta(minutes=70))

from datetime import timedelta, date
# import fmath
from fmath import add, substract

from colorama import Fore, Back, Style, init

add(1,2)
substract(1,2)

print(date.today())

init(convert = True)
print(Fore.RED + 'Hello World')