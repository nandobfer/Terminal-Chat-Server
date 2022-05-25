from flask import Flask, request, url_for, redirect, render_template, request
from database_handler import *
app = Flask(__name__)

users = []


@app.route('/database.json', methods=['GET'])
def database():
    return getDatabase()


@app.route('/connect/', methods=['POST'])
def connect():
    global users
    user = request.form['user']
    if not user in users:
        users.append(user)
    else:
        return 'user already connected'

    return str(users)


@app.route('/disconnect/', methods=['POST'])
def diconnect():
    global users
    user = request.form['user']
    if user in users:
        users.remove(user)
        return 'disconnected'


@app.route('/signup/', methods=['POST'])
def signup_route():
    text = ''
    if request.method == 'POST':
        if 'signup' in request.form:
            user = request.form['signup']
            # password = request.form['password']
            try:
                print(user)
                signUp(user)
                text = 'user successfully signed up'
            except Exception as error:
                text = 'error when signing user:'
                text += error

        return text


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="80")
