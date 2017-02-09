import json
import mysql.connector as db

from loader.DbRadLoader import DbRadLoader
from loader.LoaderIteration import LoaderIteration
from loader.MvgLoader import MvgLoader
from loader.MysqlHandler import MysqlHandler

class LoaderExecution(object):

    def __init__(self, connection):
        self.__dbconnection = connection


def main():
    """
    Main Function for the LoaderExecution, connects to the database and calls the loaders.
    After that, the results are handed over to MysqlHandler
    """
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
    print('starting LoaderIteration')
    loaderIteration = LoaderIteration(dbconnection)
    id = loaderIteration.createMaxId()
    print('LoaderIteration finished')

    # Step: execute loaders
    allVehicles = []
    allStations = []

    # MVG
    print('starting MvgLoader')
    mvgLoader = MvgLoader(id)
    allVehicles += mvgLoader.getVehicles()
    allStations += mvgLoader.getStations()
    print('MvgLoader finished')

    # DB-Rad
    print('starting DbLoader')
    dbRadLoader = DbRadLoader(id)
    allVehicles += dbRadLoader.getVehicles()
    print('DbLoader finished')

    # Step: save objects to database
    print('starting MysqlHandler')
    mysqlHandler = MysqlHandler()
    mysqlHandler.saveStations(dbconnection, allStations)
    mysqlHandler.saveVehicles(dbconnection, allVehicles)
    print('MysqlHandler finished')

    dbconnection.close()

# call main on startup
if __name__=='__main__':
    main()