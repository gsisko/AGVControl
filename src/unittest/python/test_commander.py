#system imports to provide proper test execution
from __future__ import absolute_import
import sys, os
from io import StringIO
#for pre build tests
#sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir) + "\\commanders"))

#testing module imports
import unittest
try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

#import Commander for testing
from RoboteqCommand import RoboteqCommand, RoboteqCommandLibrary, RoboteqCommander, RuntimeCommand, RuntimeQuery, ConfigSetting



class RoboteqCommanderFixture(unittest.TestCase):


    #Function to emulate controller response to given command strings
    def EvaluateControllerResponse(self, _CommandString):
            return u'Place Holder Controller Response'

    TestStreamBuffer = StringIO()

    #Mock readline so that controller alwasy returns an incorrect response
    TestStreamBuffer.readline = MagicMock(return_value = u'Place Holder Controller Response')

    def setUp(self):
        self.gocommand = RuntimeCommand(u'G', 0)
        self.ampsquery = RuntimeQuery(u'A', 0)
        self.operatingconfig = ConfigSetting(u'MMOD', 0)
        self.commander = RoboteqCommander(RoboteqCommandLibrary({u'_G': self.gocommand , u'_A': self.ampsquery, u'_MMOD': self.operatingconfig}), self.TestStreamBuffer)


class TestRoboteqCommanderMethods(RoboteqCommanderFixture):

    def test_SubmitCommand(self):

        #test Cases for command cosntruction
        self.assertEqual(self.commander._ConstructOutput(u'!',u'_G', 1, 300), (u'!', u'G', 1, 300))
        #test sending a normal motor CommandDictionary
        self.assertEqual(self.commander._FormatOutput((u"!",u'G', 1, 300)), u'!G 1 300')
        #test multiple arguments case
        self.assertEqual(self.commander._FormatOutput((u"!",u'G', 1, 300, 300)), u'!G 1 300 300')


    #test output of Getcommand
    #TODO: Implement context manager to clear TestStreamBuffer between tests


    def test_getValue(self):
        self.assertEqual(self.commander.getValue(u'_A', 1), self.EvaluateControllerResponse(u'?A 1'))
        self.assertEqual(self.TestStreamBuffer.getvalue().splitlines().pop(), u'?A 1')


    def test_setCommand(self):
        self.assertEqual(self.commander.setCommand(u'_G', 1, 300), self.EvaluateControllerResponse(u'!G 1 300'))
        self.assertEqual(self.TestStreamBuffer.getvalue().splitlines().pop(),u'!G 1 300')


    def test_setConfig(self):
        self.assertEqual(self.commander.setConfig(u'_MMOD', 1), self.EvaluateControllerResponse(u'^MMOD 1'))
        self.assertEqual(self.TestStreamBuffer.getvalue().splitlines().pop(), u'^MMOD 1')

    def test_getConfig(self):
        self.assertEqual(self.commander.getConfig(u'_MMOD'), self.EvaluateControllerResponse(u'~MMOD'))
        self.assertEqual(self.TestStreamBuffer.getvalue().splitlines().pop(), u'~MMOD')

#TODO add sections for each type of serial commander

if __name__ == u'__main__':
        unittest.main()
