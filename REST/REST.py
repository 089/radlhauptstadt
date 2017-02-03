#!/usr/local/bin/python3
from flask import Flask, g ,jsonify

import mysql.connector as db
import json


app = Flask(__name__)

is_db_config_loaded = False

@app.route('/radlhauptstadt/api/v0.9/provider/mvg/vehicle')
def hello_world():
    return 'Hello World!'

def load_db_config_from_json():
    config_file_name = ('config.json')
    with open(config_file_name) as config_file:
        config = json.load(config_file)
    is_db_config_loaded = True
    return config


def get_db():
    if is_db_config_loaded == False:
        config = load_db_config_from_json()

    if not hasattr(g, 'mysql_db'):
        print("LoaderExecution.config: " + config['db.connection']['hostname'])
        g.mysql_db = db.connect(
            host=config['db.connection']['hostname'],
            user=config['db.connection']['username'],
            password=config['db.connection']['password'],
            db=config['db.connection']['database']
        )

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()


if __name__ == '__main__':
    app.run()
