from mysql.connector import Error as MysqlError


class MysqlHandler(object):

    __insertVehicle = "INSERT INTO vehicle (iteration_id, provider, latitude, longitude, type, number_of_vehicle) VALUES ({}, '{}', {}, {}, '{}', {})"
    __insertStation = "INSERT INTO station (iteration_id, provider, latitude, longitude, name, number_of_station, free_bikes) VALUES ({}, '{}', {}, {}, '{}', {}, {})"

    def saveVehicles(self, connection, vehicles):
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
