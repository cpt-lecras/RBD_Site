from flask import Flask,render_template, request
from Database import requests as req




app= Flask(__name__)




print(req.show_table())



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/orders')
def orders():

    return req.show_orders(6)

@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User Page: " + name + " - " + str(id)

if __name__ == '__main__':
    app.run(debug=True)