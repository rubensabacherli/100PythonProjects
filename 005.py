""""Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters"""

class StringControl(object):
    def __init__(text):
        text.s = ""

    def getString(text):
        text.s = input('Digite algo: ')

    def printString(text):
        print(text.s.upper())
        
string = StringControl()
string.getString()
string.printString()