class Vehicle(object):

    def __init__(self, iterationId, provider, latitude, longitude, type, numberOfVehicle):
        self.__iterationId = iterationId
        self.__provider = provider
        self.__latitude = latitude
        self.__longitude = longitude
        self.__type = type
        self.__numberOfVehicle = numberOfVehicle

    def getIterationId(self):
        return self.__iterationId

    def getProvider(self):
        return self.__provider

    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def getType(self):
        return self.__type

    def getNumberOfVehicle(self):
        return self.__numberOfVehicle

    def serialize(self):
        return {
            'provider': self.getProvider(),
            'latitude': self.getLatitude(),
            'longitude': self.getLongitude(),
            'type': self.getType(),
            'number': self.getNumberOfVehicle(),
        }