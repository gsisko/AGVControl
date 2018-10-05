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

print("\n#defines are:")
for define in cppHeader.defines:
    print(" %s"%define)
