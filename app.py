from flask import Flask,render_template
from Database import database_main as database




app= Flask(__name__)

db=database.db_connection()


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