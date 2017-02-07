import json
import mysql.connector as db

from loader.LoaderIteration import LoaderIteration
from loader.MvgLoader import MvgLoader
from loader.MysqlHandler import MysqlHandler


class LoaderExecution(object):

    def __init__(self, connection):
        self.__dbconnection = connection

def main():
    config_file_name = ('config.json')

    # Step: load config
    with open(config_file_name) as config_file:
        config = json.load(config_file)

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