# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div

app = Flask(__name__)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

# @app.route('/add')
# def return_addition():
#     result = add(request.args.get('a'), request.args.get('b'))
#     return str(result)

# @app.route('/sub')
# def return_subtraction():
#     result = sub(request.args.get('a'), request.args.get('b'))
#     return str(result)

# @app.route('/mult')
# def return_multiplication():
#     result = mult(request.args.get('a'), request.args.get('b'))
#     return str(result)

# @app.route('/div')
# def return_division():
#     result = div(request.args.get('a'), request.args.get('b'))
#     return str(result)

@app.route('/<operation>')
def return_result(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations[operation](a,b))