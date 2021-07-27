# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == '__main__':
    print('test')

class Person:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    def __str__(self) -> str:
        return f"name: {self.name}"

ali = Person("ali")
print(ali)

name = 'Sheldon'


email = """
Hi {},
It was nice to talk to you.
Regards
Robin
"""
print(email.format(name))

email1 = f"""
Hi {name},
It was nice to talk to you.
Regards
Robin
"""
print(email1)

number = 10
if number >0:
    print(f"number {number} is positive")

message = 'positive' if number >0 else 'negative or zero'

print(message)

person = {
    'name': 'Robin',
    'age': 20
}

for key, value in person.items():
    print(f"key: {key}, value: {value}")

# for key in person:
#     print(f"key: {key} with value of {person[key]}")
result = 0
numbers = [1, 3, 5]

for number in numbers:
    result += number

print(f'result = {result}')

def greet(name):
    print(f'hello {name}, how are you')

greet('Robin')

from math import isqrt
print(isqrt(25))

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, number):
        print(f'phone {self.brand} is calling {number}')

    def __str__(self) -> str:
        return f'Brand {self.brand} \nPrice = {self.price}'


iphone = Phone('iphone', 1000)

print(iphone.brand)
print(iphone.price)
iphone.call('999')
print(iphone)

import datetime
now = datetime.date.today()
print(now.strftime('%d-%m-%Y'))
print(now.strftime('%d-%B-%Y'))
print(now.strftime('%d-%b-%Y'))