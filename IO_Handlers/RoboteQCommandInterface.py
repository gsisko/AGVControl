import serial

#converts roboteq Commands to
class RoboteqCommander:




    roboCanNode = None          #Robo Can node command should execute on
    terminatingCharacter = "_"  #Terminating character commander interface should use for submitting a command to the Roboteq Device

    #command to print commands
    def submitCommand(self, commandString):
        #TODO: print supplied command string and aply robocan node
        
    #command to call runtime commands
    def setCommand(self, token, *args):
        return

    #command to call runtime queries
    def getValue(self, token, *args):
        return

    #command to set configuration settings
    def setConfig(self, token, *args):
        return

    #function to get configuration settings
    def getConfig(self, token, *args):
        return

class RoboteqSerialCommander(RoboteqCommander):
