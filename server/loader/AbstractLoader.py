"""
The Class AbstractLoader, providing the necessary methods that a loader has to implement.
"""


class AbstractLoader(object):

    def getVehicles(self):
        """
        Method getVehicles(self), returns a list of Vehicle.py objects.
        """
        raise NotImplementedError( "Should have implemented this" )

    def getStations(self):
        """
        Method getStations(self), returns a list of Sation.py objects.
        """
        raise NotImplementedError( "Should have implemented this" )
