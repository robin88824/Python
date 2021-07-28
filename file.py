# file = open('./data.csv', 'r+')
# # file.write('id, name, email\n')
# # file.write('1, Robin, R@gmail.com')
# # print(file.read())
# print(file.readlines())
# # for line in file:
# #     print(line)
# file.close()

#check if file exists
# import os.path
# filename = 'data.csv'
#
# if os.path.isfile(filename):
#     with open(filename, 'r') as file:
#         print(file.read())
# else:
#     print(f'file {filename} does not exist')

#Ctl _ space for options in package
from urllib import request
import json

url = 'https://official-joke-api.appspot.com/random_ten'
r = request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)
print(type(jsonData))

import requests

r = requests.get(url)
data = r.text

# for j in jsonData:
#     setup = j['setup']
#     print(setup)

class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f'setup {setup}, punchline {punchline}'


jokes = []
for j in jsonData:
    setup = j['setup']
    punchline = j['punchline']
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f'Got {len(jokes)} jokes')


for joke in jokes:
    print(joke)

import pyttsx3