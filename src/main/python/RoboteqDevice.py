
#Class that encapsulates all RoboteQ Devices
#It should handle all Comms and Microbasic specific functions for roboteQ devices.
class RoboteqDevice:
    def __init__(self, _Commander):
        self.Commander = _Commander
