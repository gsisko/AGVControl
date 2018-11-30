from RoboteqCommand import RoboteqCommand, RoboteqCommander, RoboteqCommandLibrary
from RoboteqSerialCommand import RoboteqSerialCommander
from RoboteqCPPimporter import RoboteqCPPImporter
from enum import Enum
import copy


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

Config = {'mode': '_MMOD',
          'maxspeed': '_MXRPM',
          'minspeed': '_MNRPM',
          'acceleration': '_AC',
          'decceleration': '_DC'}


SpeedandAcceleration = {'mode': OperatingMode.Open_Loop,
                        'maxspeed': 0,
                        'minspeed': 0,
                        'acceleration': 0,
                        'decceleration': 0}


Channel1 = SpeedandAcceleration

#TODO colate all tables automatically

def ReadConfig():
    """Reads all the configration settings from various dicts
    """
    for k in SpeedandAcceleration.keys():
        SpeedandAcceleration[k] = controller.getConfig(Config[k])

    # connect to a Device


controller = RoboteqCommander(RoboteqCommandLibrary())

# connect to a Device

def connect():
    try:
        tokenList = RoboteqCPPImport.RoboteqImport('Constants.h')
        controller = RoboteqSerialCommander.connectOverRS232(tokenList)
    except SerialException:
        return 'Device not Found'
    return 'Device Connected'
