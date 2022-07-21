from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
import seeds
from extensions import db, app

database_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(database_dir + 'Information-System.db')
app.config['DEBUG'] = True

db.init_app(app)


@app.route('/')
def main_url():
    return jsonify(message="This is the main URL for students grades API"), 200


@app.route('/describe')
def describe():
    return "Hello there! \n This is an API for manging students records, hello"


if __name__ == '__main__':
    app.run()
