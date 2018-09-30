import sys, os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir) + "\\commanders"))

import unittest


from RoboteQCommandInterface import RoboteqCommander



class RoboteqCommanderFixture(unittest.TestCase):



    def setUp(self):
        self.commander = RoboteqCommander(None, None, None)


class TestRoboteqCommanderMethods(RoboteqCommanderFixture):

    def test_SubmitCommand(self):
        self.assertEquals(self.commander.SubmitCommand("!",{'_G':'G'},'_G', 1, 300), '!G 1 300')




if __name__ == '__main__':
        unittest.main()
