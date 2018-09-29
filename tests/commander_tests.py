import unittest

class RoboteqCommanderFixture(unittest.TestCase):

    def setUp(self):
        self.commander = RoboteqCommander(None, None, None)


class TestRoboteqCommanderMethods(RoboteqCommanderFixture):

    def Test_SubmitCommand(self):
        self.assertEquals(commander.SubmitCommand("!",{'_G':'G'},'_G', 1, 300), '!G 1 300')




if __name__ == '__main__':

    unittest.main()
