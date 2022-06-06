# Refactor the following code so that it belongs to a Person class/object.

# def greet(my_name, your_name):
#     return "Hello %s, my name is %s" % (your_name, my_name)

# Each Person instance will have a greet method. The Person instance should be instantiated with a name so that
# it no longer has to be passed into each greet method call.

# Here is how the final refactored code would be used:
# joe = Person('Joe')
# joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
# joe.name          # should == 'Joe'

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other):
        return f'Hello {other}, my name is {self.name}'