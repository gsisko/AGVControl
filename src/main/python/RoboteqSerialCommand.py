#TODO Figure out some way to unit test thing thing

import RoboteqCommand
import serial

#General purpose commander on a StringIO object.
#Can use this class to mock behavior of RoboteQ command classes in Unittests
class RoboteqSerialCommander(RoboteqCommand.RoboteqCommandGenerator):


    #TODO: create dictionary structure that can check whether supplied command aruments are valid
    def __init__(self, _CommandDictionary, _QueryDictionary, _ConfigDictionary, _SerialStream ):
        """#RoboteqCommander must be constructed by providing a dictionary for all commandString
        Arguments: _CommandDictionary - dictionary that lists all command tokens
                   _QueryDictionary - dictionary that lists all query tokens
                   _ConfigDictionary - dictionary that lists all config tokens
                   _SerialStream - Serial port stream using PySerial that the Commander should interact with.
                                   This output stream should be considered as a serial port on a computer"""
        super().__init__(_CommandDictionary, _QueryDictionary, _ConfigDictionary)

        self.outputStream = _SerialStream

        return

    @classmethod
    def connectOverRS232(cls, _CommandDictionary, _QueryDictionary, _ConfigDictionary,*SerialArgs):
        """Function decorator to create serial object on the fly using provided settings"""
        serialPort = serial.Serial(*SerialArgs, timeout = 1)  #specify default timeout of 1 sec using timeout keyord arg
        Serialcommander1 = cls(_CommandDictionary, _QueryDictionary, _ConfigDictionary, serialPort)
        return Serialcommander1

    #TODO make decotorator that just uses default settings to connect over a serial port

    #TODO Iplement exception raising if there is no response from Roboteq Device, or if somehting else goes wrong with the serial connection.
    def SubmitCommandString(self, commandString):
        """Function to return command string to Roboteq Device
        Should be redefined in inherited classes to interface over any port
        Aruments: commandString - string commander should send to RoboteQ Device
        Returns: Will retrun a string that is the response from the Roboteq Device"""
        #Submits to user supplied outputStream
        #may want to save this functionality for derived classes
        outputString = commandString + '_'
        self.outputStream.write(outputString.encode('utf-8'))    #Roboteq Devices accept the underscore charcter as a command terminator
        controllerResponse =  self.outputStream.readline().decode('utf-8').split('\r')[-2] #TODO fix even more of this split() ugliness
        return controllerResponse
