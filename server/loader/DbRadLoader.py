import json
import requests

from loader.AbstractLoader import AbstractLoader
from loader.Station import Station
from loader.Vehicle import Vehicle


class DbRadLoader(AbstractLoader):
    __jsonUrl = 'https://www.callabike-interaktiv.de/kundenbuchung/hal2ajax_process.php?callee=getMarker&mapstadt_id=90&requester=bikesuche&ajxmod=hal2map'
    __provider = 'dbrad'
    __typeBike = 'bike'
    __typePedelec = 'pedelec'
    __vehicles = []
    __stations = []

    def __init__(self, iterationId):

        response = requests.get(self.__jsonUrl)
        jsonData = json.loads(response.text)
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
