from io import StringIO
from enum import Enum, auto


#TODO consider changing name of this away from the command since it generates confusing conflict with runtime command
class RoboteqCommand:
    """Class to use as generic class for a roboteq command"""
    __slots__ = ('Identity','HexID','Name','Function','Aliases')

    def __init__(self, _Identity, _HexID, _Name = '', _Function = '', _Aliases = []):
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

        self.Name = _Name #TODO consider manipulating __name__ from these
        self.Function = _Function

    def __iter__(self):
        return iter(self.__slots__)

    def items(self):
        for attribute in self.__slots__:
            yield attribute, getattr(self, attribute)

class RuntimeCommand(RoboteqCommand):
    pass

class RuntimeQuery(RoboteqCommand):
    pass

class ConfigSetting(RoboteqCommand):
    pass

class RoboteqCommandLibrary(dict):
    """This structure is going to have to hold a set of RoboteQ commands that can be accessed using their identity stringself.
    Each command must have a unitque identity string. Should also only allow 1 type in each dictionary"""
    pass

#Genreates Roboteqcommands for commanders to use
#acts as base class for Roboteq commanders that actually interact with Roboteq Devices
class RoboteqCommandGenerator:
    """This is the core Roboteq Command class, with a generic RoboteqCommander Being an instantiation set up to use basic StringIO

    The intention of this class is to have 3 main stages of commanding:
    1) Construction: Command is constructed with constructOutput(), which creates the actual contents of the CommandDictionary
    2) Formatting: Command is formatted based on the platform and protocol that it is being used on
    3) Submission: Command is submitted to the controllerself.


    This Class is structured like this in order to allow subclasses to be created to work with different platforms and be able to modify each step of the process for """
    def __init__(self, _TokenList):
        self.TokenList = _TokenList

    def ConstructOutput(self, CommandType, token, *args):
        """Generates arguments for format Output"""
        output = ''
        try:
            output = self.TokenList[token].Identity
        except KeyError:
            print('Key not found in commander libary!')
        return (CommandType, output, *args)

    #Creates command that can be interpreted by Roboteq device
    #command should match what user inputs in console tab of Roborun+
    #TODO: all commanders should have internal dictionaries, so we will have to make sure that this is optimized to pass dictionary.
    def FormatOutput(self, CommandType, tokenString, *args):
        """Generates arguments for SubmitOuput Output"""
        CommandOutput = [tokenString]
        CommandOutput.extend(str(v) for v in args)
        return CommandType + ' '.join(CommandOutput)



    def SubmitOutput(self, commandString):
        """Submits output to controller"""
        #Prints Command String
        #place holder function to be overwritten in dereived classes
        return commandString

    #TODO: catch any error where an invalid token is presented





#General purpose commander on a StringIO object.
#Can use this class to mock behavior of RoboteQ command classes in Unittests
class RoboteqCommander(RoboteqCommandGenerator):


    #TODO: create dictionary structure that can check whether supplied command aruments are valid
    def __init__(self, _TokenList, _outputStream ):
        """Roboteq Commander serves as the generic commander implementation, and operates on a standard string IO output. It also provides the generic commands for differentiating between different kinds of command output."""

        super(RoboteqCommander, self).__init__(_TokenList)

        self.outputStream = _outputStream

        return

    #command to call runtime commands
    def setCommand(self, token, *args):
        return self.SubmitOutput(self.FormatOutput(*self.ConstructOutput('!' , token, *args)))

    #command to call runtime queries
    def getValue(self, token, *args):
        submitToken = self.TokenList[token].Identity
        return self.SubmitOutput(self.FormatOutput('?', submitToken, *args))

    #command to set configuration settings
    def setConfig(self, token, *args):
        submitToken = self.TokenList[token].Identity
        return self.SubmitOutput(self.FormatOutput('^',  submitToken, *args))

    #function to get configuration settings
    def getConfig(self, token, *args):
        submitToken = self.TokenList[token].Identity
        return self.SubmitOutput(self.FormatOutput('~',  submitToken, *args))

    #Function to return command string to Roboteq Device
    #Should be redefined in inherited classes to interface over any port
    #Aruments: commandString - string commander should send to RoboteQ Device
    #Returns: string that will execute on roboteq Device. Should be redefined in derived classes
    def SubmitOutput(self, commandString):
        #Submits to user supplied outputStream
        #may want to save this functionality for derived classes
        self.outputStream.write(commandString + "\n")
        controllerResponse =  self.outputStream.readline()
        return controllerResponse
