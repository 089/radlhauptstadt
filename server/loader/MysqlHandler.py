from mysql.connector import Error as MysqlError

"""
Class MysqlHandler, used to insert vehicles and stations to the database.
"""


class MysqlHandler(object):

    # The insert vehicle query with placeholders for the values
    __insertVehicle = "INSERT INTO vehicle (iteration_id, provider, latitude, longitude, type, number_of_vehicle) VALUES ({}, '{}', {}, {}, '{}', '{}')"
    # The insert station query with placeholders for the values
    __insertStation = "INSERT INTO station (iteration_id, provider, latitude, longitude, name, number_of_station, free_bikes) VALUES ({}, '{}', {}, {}, '{}', '{}', {})"

    def saveVehicles(self, connection, vehicles):
        """
        Method to save a list of vehicles
        :param connection: The database connection
        :param vehicles: The list of vehicles
        """
        print('MysqlHandler.saveVehicles: ' + str(vehicles))

        connection.autocommit = False
        cursor = connection.cursor()

        try:
            for vehicle in vehicles:
                print(self.__insertVehicle.format(
                    vehicle.getIterationId(),
                    vehicle.getProvider(),
                    vehicle.getLatitude(),
                    vehicle.getLongitude(),
                    vehicle.getType(),
                    vehicle.getNumberOfVehicle()
                ))
                cursor.execute(self.__insertVehicle.format(
                    vehicle.getIterationId(),
                    vehicle.getProvider(),
                    vehicle.getLatitude(),
                    vehicle.getLongitude(),
                    vehicle.getType(),
                    vehicle.getNumberOfVehicle()
                ))
            connection.commit()
        except MysqlError as error:
            connection.rollback()
            print(error)

        finally:
            connection.autocommit = True

    def saveStations(self, connection, stations):
        """
        The method to insert a list of stations.
        :param connection: The database connection
        :param stations: The list of stations
        """
        print('MysqlHandler.saveStations: ' + str(stations))

        connection.autocommit = False
        cursor = connection.cursor()

        try:
            for station in stations:
                print(self.__insertStation.format(
                    station.getIterationId(),
                    station.getProvider(),
                    station.getLatitude(),
                    station.getLongitude(),
                    station.getName(),
                    station.getNumberOfStation(),
                    station.getAvailableBikes()
                ))
                cursor.execute(self.__insertStation.format(
                    station.getIterationId(),
                    station.getProvider(),
                    station.getLatitude(),
                    station.getLongitude(),
                    station.getName(),
                    station.getNumberOfStation(),
                    station.getAvailableBikes()
                ))
            connection.commit()
        except MysqlError as error:
            connection.rollback()
            print(error)

        finally:
            connection.autocommit = True
