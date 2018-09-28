import serial

#converts roboteq Commands to
class RoboteqCommander:

    #Token Dictionaries
    #TODO: create dictionary structure that can check whether supplied command aruments are valid
    CommandDictionary = None
    QueryDictionary = None
    ConfigDictionary = None

    roboCanNode = None          #Robo Can node command should execute on
    terminatingCharacter = "_"  #Terminating character commander interface should use for submitting a command to the Roboteq Device

    #RoboteqCommander must be constructed by providing a dictionary for all commandString
    #Arguments: _CommandDictionary - dictionary that lists
    def __init__(self, _CommandDictionary, _QueryDictionary, _ConfigDictionary ):
        #todo Construct commander with corresponding command Dictionaries
        return

    #Function to print command string to Roboteq Device
    #Should be redefined in inherited classes to interface over any port
    #Aruments: commandString - string that commander should send to RoboteQ Device
    def SubmitCommandString(self, commandString):
        #TODO: print supplied command string and aply robocan node
        return

    #TODO: catch any error where an invalid token is presented

    #submit command using supplied command QueryDictionary
    #TODO: all commanders should have internal dictionaries, so we will have to make sure that this is optimized to pass dictionary.
    def SubmitCommand(self, CommandType, tokenDictionary, token, *args):
        #TODO: construct string to be be printed by self.submitCommandString
        return

    #command to call runtime commands
    def setCommand(self, token, *args):
        self.SubmitCommand("!" ,self.CommaDicationary, token, args)
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
