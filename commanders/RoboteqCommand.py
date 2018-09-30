from io import StringIO

#converts roboteq Commands to
class RoboteqCommander:



    #RoboteqCommander must be constructed by providing a dictionary for all commandString
    #Arguments: _CommandDictionary - dictionary that lists all command tokens
    #           _QueryDictionary - dictionary that lists all query tokens
    #           _ConfigDictionary - dictionary that lists all config tokens
    #           _outputStream - IO stream that the Commander should interact with.
    #                           This output stream should be considered as an input in Roborun+
    #TODO: create dictionary structure that can check whether supplied command aruments are valid
    def __init__(self, _CommandDictionary, _QueryDictionary, _ConfigDictionary, _outputStream ):
        self.CommandDictionary = _CommandDictionary
        self.QueryDictionary = _QueryDictionary
        self.ConfigDictionary = _ConfigDictionary

        self.outputStream = _outputStream

        return

    #Function to return command string to Roboteq Device
    #Should be redefined in inherited classes to interface over any port
    #Aruments: commandString - string commander should send to RoboteQ Device
    #Returns: string that will execute on roboteq Device. Should be redefined in derived classes
    def SubmitCommandString(self, commandString):
        #Submits to user supplied outputStream
        #may want to save this functionality for derived classes
        self.outputStream.write(commandString + "\n")
        controllerResponse =  self.outputStream.readline()
        return controllerResponse

    #TODO: catch any error where an invalid token is presented

    #Creates command that can be interpreted by Roboteq device
    #command should match what user inputs in console tab of Roborun+
    #TODO: all commanders should have internal dictionaries, so we will have to make sure that this is optimized to pass dictionary.
    def CreateCommand(self, CommandType, tokenDictionary, token, *args):

        CommandOutput = [tokenDictionary[token]]
        CommandOutput.extend(str(v) for v in args)
        return CommandType + ' '.join(CommandOutput)

    #command to call runtime commands
    def setCommand(self, token, *args):
        return self.SubmitCommandString(self.CreateCommand('!' ,self.CommandDictionary, token, *args))

    #command to call runtime queries
    def getValue(self, token, *args):
        return self.SubmitCommandString(self.CreateCommand('?',self.QueryDictionary, token, *args))

    #command to set configuration settings
    def setConfig(self, token, *args):
        return self.SubmitCommandString(self.CreateCommand('^', self.ConfigDictionary, token, *args))

    #function to get configuration settings
    def getConfig(self, token, *args):
        return self.SubmitCommandString(self.CreateCommand('~', self.ConfigDictionary, token, *args))
