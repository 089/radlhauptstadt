class Station(object):

    def __init__(self, iterationId, provider, latitude, longitude, name, numberOfStation, freeBikes):
        self.__iterationId = iterationId
        self.__provider = provider
        self.__latitude = latitude
        self.__longitude = longitude
        self.__name = name
        self.__numberOfStation = numberOfStation
        self.__freeBikes = freeBikes

    def getIterationId(self):
        return self.__iterationId

    def getProvider(self):
        return self.__provider

    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def getName(self):
        return self.__name

    def getNumberOfStation(self):
        return self.__numberOfStation

    def getFreeBikes(self):
        return self.__freeBikes