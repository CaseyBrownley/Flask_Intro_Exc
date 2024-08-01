# Put your app in here.
from flask import Flask
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_a_b():
    """Adds a and b values"""
    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route('/subtract')
def subtract_a_b():
    """Subtracts a and b values"""
    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result = sub(a,b)
    
    return str(result)

@app.route('/multiply')
def multiply_a_b():
    """Multiplies a and b values"""
    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result = mult(a,b)
    
    return str(result)

@app.route('/divide')
def divide_a_b():
    """Multiplies a and b values"""
    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result = div(a,b)
    
    return str(result)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result