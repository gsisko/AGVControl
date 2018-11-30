from RoboteqCommand import RoboteqCommand, RoboteqCommander, RoboteqCommandLibrary
from RoboteqSerialCommand import RoboteqSerialCommander
from RoboteqCPPimporter import RoboteqCPPImporter

controller = RoboteqCommander(RoboteqCommandLibrary())

#connect to a Device
def connect():
    try:
        tokenList = RoboteqCPPImport.RoboteqImport('Constants.h')
        controller = RoboteqSerialCommander.connectOverRS232(tokenList)
    except SerialException:
        return 'Device not Found'
    return 'Device Connected'

 
