class Station(object):

    def __init__(self, iterationId, provider, latitude, longitude, name, numberOfStation, availableBikes):
        self.__iterationId = iterationId
        self.__provider = provider
        self.__latitude = latitude
        self.__longitude = longitude
        self.__name = name
        self.__numberOfStation = numberOfStation
        self.__availableBikes = availableBikes

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

    def getAvailableBikes(self):
        return self.__availableBikes

    def serialize(self):
        return {
            'provider': self.getProvider(),
            'latitude': self.getLatitude(),
            'longitude': self.getLongitude(),
            'name': self.getName(),
            'number': self.getNumberOfStation(),
            'availableBikes': self.getAvailableBikes(),
        }