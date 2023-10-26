from flask import Flask,render_template
from getpass import getpass
from mysql.connector import connect, Error



app= Flask(__name__)
def db_connection():
    try:
        with connect(
                host="localhost",
                user="root",
                password="root",
                database="test",
        ) as connection:
            print(connection)
    except Error as e:
        print("ERROR BRAT"+e)


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


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User Page: " + name + " - " + str(id)

if __name__ == '__main__':
    db_connection()
    app.run(debug=True)