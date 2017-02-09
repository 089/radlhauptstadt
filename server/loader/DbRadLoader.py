import json
import requests

from loader.AbstractLoader import AbstractLoader
from loader.Station import Station
from loader.Vehicle import Vehicle

"""
Class DbRadLoader, the loader for retrieving information about the Call A Bike service.
Derived of AbstractLoader.
"""
class DbRadLoader(AbstractLoader):

    # The current API URL.
    __jsonUrl = 'https://www.callabike-interaktiv.de/kundenbuchung/hal2ajax_process.php?callee=getMarker&mapstadt_id=90&requester=bikesuche&ajxmod=hal2map'
    # The provider name
    __provider = 'dbrad'
    # The string for the type of bikes
    __typeBike = 'bike'
    # The string for the type of pedelecs
    __typePedelec = 'pedelec'
    # The list of all vehicles this loader found
    __vehicles = []
    # The list of all stations this loader found
    __stations = []

    def __init__(self, iterationId):

        # HTTP request to the jsonUrl
        """
        Initalizes a new object
        :param iterationId: The current iteration id.
        """
        response = requests.get(self.__jsonUrl)
        # Response text
        jsonData = json.loads(response.text)
        # For an example of the json, check the documentation.
        jsonEntries = jsonData['marker']

        for entry in jsonEntries:
            if entry['hal2option']['bikelist'][0]['isPedelec']:
                currentVehicle = Vehicle(iterationId, self.__provider, entry['lat'], entry['lng'], self.__typePedelec,
                                         entry['hal2option']['bikelist'][0]['Number'])
            else:
                currentVehicle = Vehicle(iterationId, self.__provider, entry['lat'], entry['lng'], self.__typeBike,
                                         entry['hal2option']['bikelist'][0]['Number'])

            self.__vehicles.append(currentVehicle)

    def getVehicles(self):
        return self.__vehicles

    def getStations(self):
        return self.__stations
