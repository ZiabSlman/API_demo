from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
import model

database_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_dir
app.config['DEBUG'] = True

db = SQLAlchemy(app)


@app.route('/')
def main_url():
    return jsonify(message="This is the main URL for students grades API"), 200


@app.route('/describe')
def describe():
    return "Hello there! \n This is an API for manging students records, hello"


if __name__ == '__main__':
    app.run()
