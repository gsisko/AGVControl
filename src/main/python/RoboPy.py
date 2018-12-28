from __future__ import absolute_import
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


class MotorController(object):
    u"""class for our Roboteq Motor Controller"""
#controller = DisconnectedController()

    def __init__(self):
        self.commander = None
        self.config = {u'movemode': u'_MMOD',
                       u'maxspeed': u'_MXRPM',
                       u'minspeed': u'_MNRPM',
                       u'acceleration': u'_AC',
                       u'decceleration': u'_DC'}

        self.SpeedandAcceleration = {u'movemode': OperatingMode.Open_Loop,
                                     u'maxspeed': 0,
                                     u'minspeed': 0,
                                     u'acceleration': 0,
                                     u'decceleration': 0}

    # TODO colate all tables automatically

    def ReadConfig(self):
        u"""Reads all the configration settings from various dicts
        """
        for k in self.SpeedandAcceleration.keys():
            self.SpeedandAcceleration[k] = self.commander.getConfig(self.config[k])

        # connect to a Device

    # connect to a Device

    def connect(self,*serialargs):
        try:
            tokenList = RoboteqCPPImporter.RoboteqImport(u'Constants.h')
            self.commander = RoboteqSerialCommander.connectOverRS232(tokenList, *serialargs)
        except serial.SerialException:
            return u'Device not Found'
        return u'Device Connected'
