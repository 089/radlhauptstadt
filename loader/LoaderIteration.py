import time
from mysql.connector import Error as MySQLError

class LoaderIteration(object):

    __queryId = 'SELECT MAX(id) AS max_id FROM loaderiteration'
    __queryTimestmp = 'INSERT INTO loaderiteration (timestmp) VALUES ({})'

    def __init__(self, connection):
        self.__dbconnection=connection

    def createMaxId(self):
        self.__setTimestamp(int(time.time()))

        try:
            cursor = self.__dbconnection.cursor()
            cursor.execute(self.__queryId)
            row = cursor.fetchone()
            print("LoaderIteration.createMaxId row = " + str(row))
        except MySQLError as error:
            print(error)
        finally:
            cursor.close()

        return row["max_id"]

    def __setTimestamp(self, timestmp):
        try:
            cursor = self.__dbconnection.cursor()
            cursor.execute(self.__queryTimestmp.format(timestmp))
        except MySQLError as error:
            print(error)
        finally:
            cursor.close()
