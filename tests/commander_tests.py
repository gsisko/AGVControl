import sys, os
from io import StringIO

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir) + "\\commanders"))

import unittest


from RoboteQCommandInterface import RoboteqCommander



class RoboteqCommanderFixture(unittest.TestCase):

    TestStreamBuffer = StringIO()

    def setUp(self):
        self.commander = RoboteqCommander({'_G':'G', '_M':'M'}, {'_A':'A'}, None, self.TestStreamBuffer)


class TestRoboteqCommanderMethods(RoboteqCommanderFixture):

    def test_SubmitCommand(self):
        #test sending a normal motor CommandDictionary
        self.assertEquals(self.commander.CreateCommand("!",{'_G':'G'},'_G', 1, 300), '!G 1 300')
        #test multiple arguments case
        self.assertEquals(self.commander.CreateCommand("!",{'_G':'G'},'_G', 1, 300, 300), '!G 1 300 300')

    #test output of Getcommand
    #TODO: Implement context manager to clear TestStreamBuffer between tests

    def test_getValue(self):
        self.commander.getValue('_A', 1)
        self.assertEquals(self.TestStreamBuffer.getvalue().splitlines().pop(), '?A 1')


    def test_setCommand(self):
        self.commander.setCommand('_G', 1, 300)
        self.assertEquals(self.TestStreamBuffer.getvalue().splitlines().pop(),'!G 1 300')


if __name__ == '__main__':
        unittest.main()
