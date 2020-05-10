from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print('antes de peticion')

@app.after_request
def after_request(response):
    print('Despues de peticion')
    return response

@app.route('/')
def index():
    name = 'Codi'
    is_premium=True
    courses= ['Python', 'Rubi', 'JavaScript']
    return render_template('index.html', userame=name, is_premium=is_premium, courses=courses)

@app.route('/usuario/<username>/<int:age>') #String
def usuario(userame, age):
    return "Hola " + userame + ' ' + age

@app.route('/datos')
def datos():
    nombre = request.args.get('nombre', '') #dict
    return 'Listado de datos: ' + nombre

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)