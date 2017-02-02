import time
from mysql.connector import Error as MySQLError

class LoaderIteration(object):

    __queryId = 'SELECT MAX(id) AS max_id FROM loaderiteration'
    __queryTimestmp = 'INSERT INTO loaderiteration (timestmp) VALUES (CURRENT_TIMESTAMP)'

    def __init__(self, connection):
        self.__dbconnection=connection

    def createMaxId(self):
        self.__setTimestamp()

        try:
            cursor = self.__dbconnection.cursor()
            cursor.execute(self.__queryId)
            row = cursor.fetchone()
            print("LoaderIteration.createMaxId row = " + str(row))
        except MySQLError as error:
            print(error)
        finally:
            cursor.close()

        return row[0]

    def __setTimestamp(self):
        try:
            cursor = self.__dbconnection.cursor()
            cursor.execute(
                self.__queryTimestmp)
        except MySQLError as error:
            print(error)
        finally:
            cursor.close()
