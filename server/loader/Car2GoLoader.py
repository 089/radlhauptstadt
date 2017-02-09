import json
import string

import requests

from loader.AbstractLoader import AbstractLoader
from loader.Vehicle import Vehicle


class Car2GoLoader(AbstractLoader):

    # The current API URL.
    __jsonUrl = 'https://www.car2go.com/api/v2.0/vehicles?loc=M%C3%BCnchen&format=json'
    # The provider name
    __provider = 'car2go'
    # The string for the type
    __type = 'car'
    # The list of all vehicles this loader found
    __vehicles = []
    # The list of all stations this loader found
    __stations = []

    def __init__(self, iterationId):
        """
        Initializes a new object
        :param iterationId: The current iteration id.
        """

        response = requests.get(self.__jsonUrl)
        jsonData = json.loads(response.text)
        jsonEntries = jsonData['placemarks']
        for entry in jsonEntries:
            coords = str(entry['coordinates']).strip('[').strip(']')
            self.__vehicles.append(Vehicle(iterationId, self.__provider, coords.split(',')[1], coords.split(',')[0], self.__type, entry['vin']))

    def getVehicles(self):
        return self.__vehicles

    def getStations(self):
        return self.__stations

