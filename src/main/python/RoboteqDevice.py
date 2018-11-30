from RoboteqCommand import RoboteqCommander

class RoboteqDevice:
    """Class that encapsulates all RoboteQ Devices
    It should handle all Comms and Microbasic specific functions for roboteQ devices"""
    def __init__(self, _Commander):
        """_Commander should be a RoboteQ commander"""
        if(type(_Commander) == RoboteQCommander)
            self.Commander = _Commander
        else
            except TypeError
