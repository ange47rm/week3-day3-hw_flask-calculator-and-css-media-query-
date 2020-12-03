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