#!/usr/local/bin/python3
from flask import Flask, g, jsonify, abort, json
from flask_cors import CORS, cross_origin

import mysql.connector as db

from loader.Station import Station
from loader.Vehicle import Vehicle

app = Flask(__name__)
CORS(app)


def mysqlToVehicle(cursor):
    results = []
    for result in cursor.stored_results():
        for row in result.fetchall():
            results.append(Vehicle(row[0], row[1], row[2], row[3], row[4], row[5]))

    return jsonify(vehicles=[e.serialize() for e in results])


def mysqlToStation(cursor):
    results = []
    for result in cursor.stored_results():
        for row in result.fetchall():
            results.append(Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    return jsonify(stations=[e.serialize() for e in results])


def load_db_config_from_json():
    config_file_name = ('config.json')
    with open(config_file_name) as config_file:
        cfg = json.load(config_file)
    return cfg


@app.before_request
def db_connect():
    global config

    g.mysql_db = db.connect(
        host=config['db.connection']['hostname'],
        user=config['db.connection']['username'],
        password=config['db.connection']['password'],
        db=config['db.connection']['database']
    )


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')


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

    return mysqlToVehicle(cursor)


@app.route('/api/v0.9/provider/<provider>/vehicle', methods=['GET'])
def all_vehicles(provider):
    if provider == '':
        abort(400)

    cursor = g.mysql_db.cursor()

    cursor.callproc('all_vehicles', args=(provider, ))

    return mysqlToVehicle(cursor)


@app.route('/api/v0.9/provider/<provider>/station/<station>', methods=['GET'])
def one_station(provider, station):
    if provider == '':
        abort(400)

    cursor = g.mysql_db.cursor()

    cursor.callproc('one_station', args=(provider, station))

    return mysqlToStation(cursor)


@app.route('/api/v0.9/provider/<provider>/station', methods=['GET'])
def all_stations(provider):
    if provider == '':
        abort(400)

    cursor = g.mysql_db.cursor()

    cursor.callproc('all_stations', args=(provider, ))

    return mysqlToStation(cursor)


@app.route('/api/v0.9/provider/<provider>/area', methods=['GET'])
def get_area(provider):
    abort(501)

if __name__ == '__main__':
    app.run()