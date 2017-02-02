class AbstractLoader(object):

    def getVehicles(self):
        raise NotImplementedError( "Should have implemented this" )

    def getStations(self):
        raise NotImplementedError( "Should have implemented this" )
