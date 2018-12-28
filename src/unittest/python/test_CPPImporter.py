from __future__ import absolute_import
import sys,os


#testing module imports
import unittest
import CppHeaderParser

from RoboteqCPPimporter import RoboteqCPPImporter
from RoboteqCommand import RoboteqCommand
from io import open


class CPPImportFixture(unittest.TestCase):

    def setUp(self):

        self.testHeader = open(u'test.h',u'w+')

        u"""Defines to test:
        #define _G 0\n#define _A 0\n#define _MMOD 39\n


        """
        self.testHeader.write(u'#define _G 0\n#define _A 0\n#define _MMOD 39\n#endif\n')

        self.testHeader.close()
        self.referenceDict = dict()

        #self.maxDiff = 1000
        self.referenceDict = {u'_G' : RoboteqCommand(u'_G', 0), u'_A' : RoboteqCommand(u'_A', 0), u'_MMOD' : RoboteqCommand(u'_MMOD', 39)}

        self.importer = RoboteqCPPImporter(u'test.h')

    def tearDown(self):

        os.remove(u'test.h')

    def test_CPPImport(self):
        self.assertDictEqual(self.importer.generateCommandDict(), self.referenceDict)


    def test_DirectImport(self):
        self.assertDictEqual(RoboteqCPPImporter.RoboteqImport(u'test.h'), self.referenceDict)

if __name__ == u'__main__':
        unittest.main()
