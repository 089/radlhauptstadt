import json
import requests
from AbstractLoader import AbstractLoader
from Station import Station
from Vehicle import Vehicle


class MvgLoader(AbstractLoader):

    __jsonUrl = 'http://mvgrad.nextbike.net/maps/nextbike-live.json?domains=mg&get_biketypes=1'
    __provider = 'mvg'
    __type = 'bike'
    __vehicles = []
    __stations = []

    def __init__(self, iterationId):

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

