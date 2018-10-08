#!/usr/bin/python
import sys
sys.path = ["../"] + sys.path   #set sys in order to be able to locate header fileself.

import CppHeaderParser

#Blank base class for all file importer to inherit from
#By default, it imports serialized python data directly with eval(). So we can print a dictionary and it will import it directly
#TODO move Roboteq Importer to its own module
class RoboteqCommandImporter():
    #We have to give the importer the source of all the commands to be imported
    #This can be a file name or a
    def __init__(_importPath):
        self.Path = _importPath

    #gernates command dictionary from printed dictionary value, should be overwriten

    def generateCommandDict():
        with open(self.Path, 'r') as Source:
            commandDict = eval(Source.read())
            return

    #This is a class mehtod that you can use to automatically import a source
    #without keeping the importer arround
    @classmethod
    def RoboteqImport(cls, _importPath):
        Importer = cls(_importPath)
        return Importer.generateCommandDict()

    #TODO add methods to merge multiple sources, specify imports from different devices


class RoboteqCPPImporter

    def generateCommandDict():

        try:
            cppHeader = CppHeaderParser.CppHeader("Constants.h") #TODO consider reworking this module to separate out StringIO object to use as source
        except CppHeaderParser.CppParseError as e:
            print(e)
            sys.exit(1)

        print("CppHeaderParser view of %s"%cppHeader)

        RoboteqCommandDict = dict()

        print("\n#defines are:")
        for define in cppHeader.defines:
            command = define.split(' ')
            if len(command) == 2:
                 #TODO try to optimize this code to perform proper data access for fast operation.
                 #TODO there is definitely a better way to do the string formatting in python
                 #The formatting of the print statement comes from the round about way that values are #defined in the Roboteq CPP install_dependencies
                 #Their identity string is defined as a decimal representation of their HEX valueself.
                 #we need to do all of that conversion here in order to make this work with Roboteq Command Generator.
                RoboteqCommandDict[command[0]] = '${:02x}'.format(int(command[1])) #using .format() instead of fstring to match formatting in RoboteQ CPP API
        print(RoboteqCommandDict)

        ####Defines are formated as keys that will have to be formatted like '${:02X}'.format(value)
