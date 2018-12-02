from RoboteqCommand import RoboteqCommand, RoboteqCommander, RoboteqCommandLibrary
from RoboteqSerialCommand import RoboteqSerialCommander
from RoboteqCPPimporter import RoboteqCPPImporter
import serial
from enum import Enum
import copy


class OperatingMode(Enum):
    Open_Loop = 0
    Closed_Loop_Speed = 1
    Closed_Loop_Position_Relative = 2
    Closed_Loop_Count_Position = 3
    Closed_Loop_Position_Tracking = 4
    Torque_Mode = 5
    Closed_Loop_Speed_Position = 6


class MotorController():
    """class for our Roboteq Motor Controller"""
#controller = DisconnectedController()

    def __init__(self):
        self.commander = None
        self.config = {'movemode': '_MMOD',
                       'maxspeed': '_MXRPM',
                       'minspeed': '_MNRPM',
                       'acceleration': '_AC',
                       'decceleration': '_DC'}

        self.SpeedandAcceleration = {'movemode': OperatingMode.Open_Loop,
                                     'maxspeed': 0,
                                     'minspeed': 0,
                                     'acceleration': 0,
                                     'decceleration': 0}

    # TODO colate all tables automatically

    def ReadConfig(self):
        """Reads all the configration settings from various dicts
        """
        for k in self.SpeedandAcceleration.keys():
            self.SpeedandAcceleration[k] = self.commander.getConfig(self.config[k])

        # connect to a Device

    controller = RoboteqCommander(RoboteqCommandLibrary())

    # connect to a Device

    def connect(self,*serialargs):
        try:
            tokenList = RoboteqCPPImporter.RoboteqImport('Constants.h')
            self.commander = RoboteqSerialCommander.connectOverRS232(tokenList, *serialargs)
        except serial.SerialException:
            return 'Device not Found'
        return 'Device Connected'
