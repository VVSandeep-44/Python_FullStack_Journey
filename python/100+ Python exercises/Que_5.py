'''
Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters
'''
# Solution:

class StringIO:
    def getString(self):
        self.Input = input('enter a string: ')
    def printString(self):
        print(self.Input.upper())
s= StringIO()
s.getString()
s.printString()

#[or]
'''
class InputOutString(object):

#  better to use contructor to avoid crashing by simply printing empty string when the printString() method is called before the getString() method.

    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
'''