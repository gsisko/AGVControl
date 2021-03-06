import sys,os


#testing module imports
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import CppHeaderParser

from RoboteqCPPimporter import RoboteqCPPImporter
from RoboteqCommand import RoboteqCommand


class CPPImportFixture(unittest.TestCase):

    def setUp(self):

        self.testHeader = open('test.h','w+')

        """Defines to test:
        #define _G 0\n#define _A 0\n#define _MMOD 39\n


        """
        self.testHeader.write('#define _G 0\n#define _A 0\n#define _MMOD 39\n#endif\n')

        self.testHeader.close()
        self.referenceDict = dict()

        #self.maxDiff = 1000
        self.referenceDict = {'_G' : RoboteqCommand('_G', 0), '_A' : RoboteqCommand('_A', 0), '_MMOD' : RoboteqCommand('_MMOD', 39)}

        self.importer = RoboteqCPPImporter('test.h')

    def tearDown(self):

        os.remove('test.h')

    def test_CPPImport(self):
        self.assertDictEqual(self.importer.generateCommandDict(), self.referenceDict)


    def test_DirectImport(self):
        self.assertDictEqual(RoboteqCPPImporter.RoboteqImport('test.h'), self.referenceDict)

if __name__ == '__main__':
        unittest.main()
