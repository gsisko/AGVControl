# testing module imports
import unittest
from unittest.mock import MagicMock

from io import StringIO

import RoboPy as rp
from RoboteqCPPimporter import RoboteqCPPImporter as importer
from RoboteqCommand import RoboteqCommander


# class serialTestCommander

class RpFixture(unittest.TestCase):
    """Test Fixture class for testing RoboPy main inteface script."""

    # Function to emulate controller response to given command strings
    def _EvaluateControllerResponse(self, _CommandString):
            return 'Place Holder Controller Response'

    def setUp(self):
        """Set up fixture objects for testing RoboPy."""
        # define controller for testing
        commandList = importer.RoboteqImport('Constants.h')
        self.TestStreamBuffer = StringIO()

        # Mock readline so that controller alwasy returns an incorrect response
        self.TestStreamBuffer.readline = MagicMock(return_value='Place Holder Controller Response')

        self.testController = rp.MotorController()
        self.testController.commander = RoboteqCommander(commandList, self.TestStreamBuffer)

    def test_HeadingCMD(self):
        """
        Test Heading command.

        Test should make sure that proper output is submitted to output stream.
        """
        self.testController.HeadingCMD(500, 250)
        self.assertEqual(self.TestStreamBuffer.getvalue(), '!G 1 500\n!G 2 250\n')

    def test_motorCMD(self):
        """
        Test Motor Command.

        Test should make sure that motor command outputs correct text to buffer stream after
        being called.
        """
        self.testController.motorCMD(1, 250)
        self.assertEqual(self.TestStreamBuffer.getvalue(), '!G 1 250\n')

    def test_setupDiffDrive(self):
        """
        Test Differential Drive setup method.

        Test should make sure that configuration changing commands are output
        to buffer stream after being called.
        """
        self.testController.setupDiffDrive()
        self.assertEqual(self.TestStreamBuffer.getvalue(), '^MXMD 1\n')


if __name__ == '__main__':
    unittest.main()
