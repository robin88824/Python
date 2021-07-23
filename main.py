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
