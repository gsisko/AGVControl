#TODO Figure out some way to unit test thing thing

import RoboteqCommand
import serial

#General purpose commander on a StringIO object.
#Can use this class to mock behavior of RoboteQ command classes in Unittests
class RoboteqSerialCommander(RoboteqCommand.RoboteqCommandGenerator):

    #RoboteqCommander must be constructed by providing a dictionary for all commandString
    #Arguments: _CommandDictionary - dictionary that lists all command tokens
    #           _QueryDictionary - dictionary that lists all query tokens
    #           _ConfigDictionary - dictionary that lists all config tokens
    #           _SerialStream - Serial port stream using PySerial that the Commander should interact with.
    #                           This output stream should be considered as a serial port on a computer
    #TODO: create dictionary structure that can check whether supplied command aruments are valid
    def __init__(self, _CommandDictionary, _QueryDictionary, _ConfigDictionary, _SerialStream ):
        super(RoboteqCommander, self).__init__(_CommandDictionary, _QueryDictionary, _ConfigDictionary)

        self.outputStream = _SerialStream

        return

    #Function decorator to create serial object on the fly using provided settings
    @classmethod
    def connectOverRS232(cls, _CommandDictionary, _QueryDictionary, _ConfigDictionary,*SerialArgs):
        serialPort = serial.Serial(*SerialArgs)
        Serialcommander1 = cls(_CommandDictionary, _QueryDictionary, _ConfigDictionary, serialPort)
        return Serialcommander1

    #TODO make decotorator that just uses default settings to connect over a serial port

    #Function to return command string to Roboteq Device
    #Should be redefined in inherited classes to interface over any port
    #Aruments: commandString - string commander should send to RoboteQ Device
    #Returns: string that will execute on roboteq Device. Should be redefined in derived classes
    def SubmitCommandString(self, commandString):
        #Submits to user supplied outputStream
        #may want to save this functionality for derived classes
        self.outputStream.write(commandString + '_')    #Roboteq Devices accept the underscore charcter as a command terminator
        controllerResponse =  self.outputStream.readline() #TODO make sure some sort of timeout is specified
        return controllerResponse
