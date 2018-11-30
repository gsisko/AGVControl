from RoboteqCommand import RoboteqCommand, RoboteqCommander, RoboteqCommandLibrary
from RoboteqSerialCommand import RoboteqSerialCommander
from RoboteqCPPimporter import RoboteqCPPImporter
from enum import Enum


class OperatingMode(Enum):
    Open_Loop = 0
    Closed_Loop_Speed = 1
    Closed_Loop_Position_Relative = 2
    Closed_Loop_Count_Position = 3
    Closed_Loop_Position_Tracking = 4
    Torque_Mode = 5
    Closed - loop speed position = 6


class DiconnectedController(RoboteqCommander)


pass


controller = DisconnectedController()

ConfigDict = {'mode': '_MMOD',
              'maxspeed': '_MXRPM',
              'minspeed': '_MNRPM',
              'acceleration': '_AC',
              'decceleration': '_DC'}


SpeedandAcceleration = {'mode': OperatingMode.Open_Loop,
                        'maxspeed': 0,
                        'minspeed': 0,
                        'acceleration': 0,
                        'decceleration': 0}


def initialize():

    # connect to a Device


def connect():
    try:
        tokenList = RoboteqCPPImport.RoboteqImport('Constants.h')
        controller = RoboteqSerialCommander.connectOverRS232(tokenList)
    except SerialException:
        return 'Device not Found'  # Todo Better Diagnostics
    return 'Device Connected'


def
