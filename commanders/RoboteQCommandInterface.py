#converts roboteq Commands to
class RoboteqCommander:

    #Token Dictionaries
    #TODO: create dictionary structure that can check whether supplied command aruments are valid
    CommandDictionary = None
    QueryDictionary = None
    ConfigDictionary = None


    #RoboteqCommander must be constructed by providing a dictionary for all commandString
    #Arguments: _CommandDictionary - dictionary that lists
    def __init__(self, _CommandDictionary, _QueryDictionary, _ConfigDictionary ):
        #todo Construct commander with corresponding command Dictionaries
        return

    #Function to return command string to Roboteq Device
    #Should be redefined in inherited classes to interface over any port
    #Aruments: commandString - string commander should send to RoboteQ Device
    #Returns: string that will execute on roboteq Device. Should be redefined in derived classes
    def SubmitCommandString(self, commandString):
        #TODO: Want to add optimimzations for device specific features
        #may want to save this functionality for derived classes
        return commandString

    #TODO: catch any error where an invalid token is presented

    #submit command using supplied command QueryDictionary
    #TODO: all commanders should have internal dictionaries, so we will have to make sure that this is optimized to pass dictionary.
    def SubmitCommand(self, CommandType, tokenDictionary, token, *args):

        CommandOutput = CommandType + tokenDictionary[token] + " " + " ".join(str(v) for v in args)

        return CommandOutput

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
