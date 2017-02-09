import time
from mysql.connector import Error as MySQLError

"""
Class LoaderIteration, creates a new Timestamp for the iteration in the database and returns the new maximum Id.
"""


class LoaderIteration(object):

    #The query for selecting the max id
    __queryId = 'SELECT MAX(id) AS max_id FROM loaderiteration'
    # The query for creating a new timestamp
    __queryTimestmp = 'INSERT INTO loaderiteration (timestmp) VALUES (CURRENT_TIMESTAMP)'

    def __init__(self, connection):
        self.__dbconnection=connection

    def createMaxId(self):
        """
         Create a new timestamp and return the resulting id.
        :return: The current max id
        """
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
        """
        Creates a new row in the loaderiteration table with the current timestamp.
        """
        try:
            cursor = self.__dbconnection.cursor()
            cursor.execute(
                self.__queryTimestmp)
        except MySQLError as error:
            print(error)
        finally:
            cursor.close()
