#TODO Figure out some way to unit test thing thing

import RoboteqCommand
import serial

#General purpose commander on a StringIO object.
#Can use this class to mock behavior of RoboteQ command classes in Unittests
class RoboteqSerialCommander(RoboteqCommand.RoboteqStreamCommander):


    @classmethod
    def connectOverRS232(cls, _TokenList,*SerialArgs):
        """Function decorator to create serial object on the fly using provided settings"""
        serialPort = serial.Serial(*SerialArgs, timeout = .1)  #specify default timeout of 1 sec using timeout keyord arg
        Serialcommander1 = cls(_TokenList, serialPort)
        return Serialcommander1

    def _FormatOaautput(self, _args):
        """Generates data chunk that gets sent as an argument to SubmitOutput"""
        CommandType, tokenString, *args = _args
        CommandOutput = [self.TokenList[tokenString].Identity[1:]]
        CommandOutput.extend(str(v) for v in args)
        return CommandType + ' '.join(CommandOutput)

    #TODO Iplement exception raising if there is no response from Roboteq Device, or if somehting else goes wrong with the serial connection.
    def _SubmitOutput(self, commandString):
        """Function to return command string to Roboteq Device
        Should be redefined in inherited classes to interface over any port
        Aruments: commandString - string commander should send to RoboteQ Device
        Returns: Will retrun a string that is the response from the Roboteq Device"""
        #Submits to user supplied outputStream
        #may want to save this functionality for derived classes
        outputString = commandString + '_'
        print(outputString)
        self.outputStream.write(outputString.encode('ascii'))    #Roboteq Devices accept the underscore charcter as a command terminator
        self.outputStream.flush()
        controllerResponse = self.outputStream.readline()
        return controllerResponse
