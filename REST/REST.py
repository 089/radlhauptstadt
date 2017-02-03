#!/usr/local/bin/python3
from flask import Flask, g, jsonify

import mysql.connector as db
import json

from flask import abort

app = Flask(__name__)


def load_db_config_from_json():
    global is_db_config_loaded
    config_file_name = ('config.json')
    with open(config_file_name) as config_file:
        cfg = json.load(config_file)
    return cfg


@app.before_request
def db_connect():
    global is_db_config_loaded, config

    print("LoaderExecution.config: " + config['db.connection']['hostname'])
    g.mysql_db = db.connect(
        host=config['db.connection']['hostname'],
        user=config['db.connection']['username'],
        password=config['db.connection']['password'],
        db=config['db.connection']['database']
    )


@app.teardown_request
def close_db(exception=None):
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()


# load config once
config = load_db_config_from_json()


########################################################################################################################

@app.route('/', methods=['GET'])
def index():
    return '{}'


@app.route('/api/v0.9/provider/<provider>/vehicle/<vehicle>', methods=['GET'])
def one_vehicle(provider, vehicle):
    if provider == '':
        abort(400)

    cursor = g.mysql_db.cursor()

    cursor.callproc('one_vehicle', args=(provider, vehicle))

    results = []
    for result in cursor.stored_results():
        results += result.fetchall()

    #return app.response_class(
    #    response=results,
    #    status=200,
    #    mimetype='application/json'
    #    )

    return results

@app.route('/api/v0.9/provider/<provider>/vehicle', methods=['GET'])
def all_vehicles(provider):
    if provider == '':
        abort(400)

    cursor = g.mysql_db.cursor()

    cursor.callproc('all_vehicles', args=provider)

    results = []
    for result in cursor.stored_results():
        results += result.fetchall()

    return results

if __name__ == '__main__':
    app.run()
