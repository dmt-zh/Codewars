# Your task is to complete the Cat class which Extends Animal and replace
# the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} meows.'