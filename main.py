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