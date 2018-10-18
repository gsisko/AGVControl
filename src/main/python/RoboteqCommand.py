from io import StringIO
from enum import Enum, auto

class RoboteqCommandType(Enum):
    """enum for roboteq command type, please consult RoboteQ User Manual, Section 19"""
    RUN = auto()
    QRY = auto()
    CFG = auto()

#TODO consider changing name of this away from the command since it generates confusing conflict with runtime command
class RoboteqCommand:
    """Class to use as generic class for a roboteq command"""
    __slots__ = ('Identity','HexID','Type','Name','Function','Aliases')

    def __init__(self, _Identity, _HexID, _Type, _Name = '', _Function = '', _Aliases = []):
        #TODO consider making Requied underlying values immutable after they are initialized, or at least private
        """Constructor: A Roboteq Command
        Required Values:
            Identity: Unique Identity String
            HexID: Underlying Hex value for Command
            Type: Command type, either a runtime command, a runtimequery, or a configuration command

        Optional Arguments:
            Name: Verbose name of Command
            Function: Name of argument to use as function name
            Aliases: Other working aliases that command can be called by in MicroBasic"""
        if isinstance(_Identity, str):
            self.Identity = _Identity
        else:
            raise TypeError("Alias must be a String")
            #TODO check that Alias is all CppHeaderParser
            #TODO add support for multiple aliases
        if isinstance(_HexID, int) and _HexID < 255:
            self.HexID = _HexID
        else:
            raise TypeError("HexID must be a positive number 255 or below")
        if isinstance(_Type, RoboteqCommandType):
            self.Type = _Type
        else:
            raise TypeError("Type must be a Roboteq Command Type")

        self.Name = _Name #TODO consider manipulating __name__ from these
        self.Function = _Function

    def __iter__(self):
        return iter(self.__slots__)

    def items(self):
        for attribute in self.__slots__:
            yield attribute, getattr(self, attribute)





#Genreates Roboteqcommands for commanders to use
#acts as base class for Roboteq commanders that actually interact with Roboteq Devices
class RoboteqCommandGenerator:
    #RoboteqCommander must be constructed by providing a dictionary for all commandString
    #Arguments: _CommandDictionary - dictionary that lists all command tokens
    #           _QueryDictionary - dictionary that lists all query tokens
    #           _ConfigDictionary - dictionary that lists all config tokens
    def __init__(self, _CommandDictionary, _QueryDictionary, _ConfigDictionary):
        self.CommandDictionary = _CommandDictionary
        self.QueryDictionary = _QueryDictionary
        self.ConfigDictionary = _ConfigDictionary

    def SubmitCommandString(self, commandString):
        #Prints Command String
        #place holder function to be overwritten in dereived classes
        return commandString

    #TODO: catch any error where an invalid token is presented

    #Creates command that can be interpreted by Roboteq device
    #command should match what user inputs in console tab of Roborun+
    #TODO: all commanders should have internal dictionaries, so we will have to make sure that this is optimized to pass dictionary.
    def CreateCommand(self, CommandType, tokenDictionary, token, *args):

        CommandOutput = [tokenDictionary[token].Identity]
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

#General purpose commander on a StringIO object.
#Can use this class to mock behavior of RoboteQ command classes in Unittests
class RoboteqCommander(RoboteqCommandGenerator):


    #TODO: create dictionary structure that can check whether supplied command aruments are valid
    def __init__(self, _CommandDictionary, _QueryDictionary, _ConfigDictionary, _outputStream ):
        """RoboteqCommander must be constructed by providing a dictionary for all commandString
            Arguments: _CommandDictionary - dictionary that lists all command tokens
                    _QueryDictionary - dictionary that lists all query tokens
                    _ConfigDictionary - dictionary that lists all config tokens
                    _outputStream - IO stream that the Commander should interact with.
                                   This output stream should be considered as an input in Roborun+"""

        super(RoboteqCommander, self).__init__(_CommandDictionary, _QueryDictionary, _ConfigDictionary)

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
