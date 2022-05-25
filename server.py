from flask import Flask, request, url_for, redirect, render_template, request
from database_handler import *
app = Flask(__name__)


@app.route('/database.json', methods=['GET'])
def database():
    return getDatabase()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="80")
