from app import app

from modules.calculator import *

@app.route ('/add/<num1>/<num2>')
def browser_add(num1, num2):
    return add(num1, num2)

@app.route ('/subtract/<num1>/<num2>')
def browser_subtract(num1, num2):
    return subtract(num1, num2)

@app.route ('/muliply/<num1>/<num2>')
def browser_muliply(num1, num2):
    return muliply(num1, num2)

@app.route ('/divide/<num1>/<num2>')
def browser_divide(num1, num2):
    return divide(num1, num2)

# THE ABOVE WORKS HOWEVER THE DECORATORS ARE NOT REALLY "DECORATING", I SHOULD HAVE LET THE 
# DECORATOR ADD THE STRING OF TEXT, AND THE CALCULATOR SHOULD HAVE JUST RETURNED A NUMBER.

# decorator: decorator is a function that takes another function as a parameter and extends 
# the behavior of the latter function without explicitly modifying it. Once the decorator 
# function is defined, we can use the @ symbol along with the name of the decorator function and 
# place it above the definition of the function to be decorated.