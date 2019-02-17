import sys,os
from io import StringIO

#testing module imports
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

import RoboteqCPPImporter from Robtoeq as importer
import RoboteqCommander from RoboteqCommand
import RoboPy as rp

class serialTestCommander
    ``

class RpFixture(unittest.TestCase):

    def setUp(self):
        #define controller for testing
        commandList = importer.RoboteqImport('Constants.h')
        TestStreamBuffer = StringIO()

        self.testController = rp.MotorController()
        self.testController.commander = RoboteqCommand.RoboteqCommander(commandList, TestStreamBuffer)

    def test_HeadingCMD(self):
        pass

    def test_motorCMD(self):
        pass

    def test_setMode(self):
        pass


if __name__ == '__main__'
    unittest.main()
