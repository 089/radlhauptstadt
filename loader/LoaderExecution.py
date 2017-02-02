import json
import mysql.connector as db

from LoaderIteration import LoaderIteration
from MvgLoader import MvgLoader
from MysqlHandler import MysqlHandler


class LoaderExecution(object):

    def __init__(self, connection):
        self.__dbconnection = connection

def main():
    config_file_name = ('config.json')

    # Step: load config
    with open(config_file_name) as config_file:
        config = json.load(config_file)

    print("LoaderExecution.config: " + config['db.connection']['hostname'])
    dbconnection = db.connect(
        host=config['db.connection']['hostname'],
        user=config['db.connection']['username'],
        password=config['db.connection']['password'],
        db=config['db.connection']['database']
    )

    # Step: create loaderIterationID
    loaderIteration = LoaderIteration(dbconnection)
    id = loaderIteration.createMaxId()

    # Step: execute loaders
    allVehicles = []
    allStations = []

    mvgLoader = MvgLoader(id)
    allVehicles += mvgLoader.getVehicles()
    allStations += mvgLoader.getStations()

    # Step: save objects to database
    mysqlHandler = MysqlHandler()
    mysqlHandler.saveStations(dbconnection, allStations)
    mysqlHandler.saveVehicles(dbconnection, allVehicles)

    dbconnection.close()

# call main on startup
if __name__=='__main__':
    main()