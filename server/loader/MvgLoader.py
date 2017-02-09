import json
import requests

from loader.AbstractLoader import AbstractLoader
from loader.Station import Station
from loader.Vehicle import Vehicle


class MvgLoader(AbstractLoader):

    # The current API URL.
    __jsonUrl = 'http://mvgrad.nextbike.net/maps/nextbike-live.json?domains=mg&get_biketypes=1'
    # The provider name
    __provider = 'mvg'
    # The string for the type
    __type = 'bike'
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
        jsonEntries = jsonData['countries'][0]['cities'][0]['places']

        for entry in jsonEntries:
            if entry['bike']:
                currentVehicle = Vehicle(iterationId, self.__provider, entry['lat'], entry['lng'], self.__type, entry['bike_numbers'])
                self.__vehicles.append(currentVehicle)
            else:
                currentStation = Station(iterationId, self.__provider, entry['lat'], entry['lng'], entry['name'], entry['number'], entry['bikes'])
                self.__stations.append(currentStation)

    def getVehicles(self):
        return self.__vehicles

    def getStations(self):
        return self.__stations

