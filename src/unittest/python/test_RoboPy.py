import sys,os
from io import StringIO

#testing module imports
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from RoboteqCPPimporter import RoboteqCPPImporter as importer
from RoboteqCommand import RoboteqCommander
import RoboPy as rp

#class serialTestCommander

class RpFixture(unittest.TestCase):
    
    #Function to emulate controller response to given command strings
    def EvaluateControllerResponse(self, _CommandString):
            return 'Place Holder Controller Response'

    def setUp(self):
        #define controller for testing
        commandList = importer.RoboteqImport('Constants.h')
        self.TestStreamBuffer = StringIO()

        #Mock readline so that controller alwasy returns an incorrect response
        self.TestStreamBuffer.readline = MagicMock(return_value = 'Place Holder Controller Response')

        self.testController = rp.MotorController()
        self.testController.commander = RoboteqCommander(commandList, self.TestStreamBuffer)
 
    def test_HeadingCMD(self):
        self.testController.HeadingCMD(500,250)
        self.assertEqual(self.TestStreamBuffer.getvalue(),'!G 1 500\n!G 2 250\n')

    def test_motorCMD(self):
        pass

if __name__ == '__main__':
    unittest.main()
