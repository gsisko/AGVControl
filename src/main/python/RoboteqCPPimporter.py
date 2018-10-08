#!/usr/bin/python
import sys
sys.path = ["../"] + sys.path   #set sys in order to be able to locate header fileself.

import CppHeaderParser

try:
    cppHeader = CppHeaderParser.CppHeader("Constants.h")
except CppHeaderParser.CppParseError as e:
    print(e)
    sys.exit(1)

print("CppHeaderParser view of %s"%cppHeader)

RoboteqCommandDict = dict()

print("\n#defines are:")
for define in cppHeader.defines:
    command = define.split(' ')
    if len(command) == 2:
        RoboteqCommandDict[command[0]] = command[1] #TODO try to optimize this code to perform proper data access for fast operation.

print(RoboteqCommandDict)

####Defines are formated as keys that will have to be formatted like '${:02X}'.format(value)
