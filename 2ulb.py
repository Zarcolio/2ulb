#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

if os.geteuid() != 0:
    exit("\nYou need to have root privileges to run this script.\nPlease try again using the sudo command.\n")

if len(sys.argv) == 1:
    print ("\nToo few arguments:")
    print ("sudo python 2ulb.py <inputfile> [-f]\n")
    print("Or after using 2ulb on 2ulb:")
    print ("sudo 2ulb <inputfile> [-f]\n")
    sys.exit(2)

if len(sys.argv) == 3:
    sForce = sys.argv[2]
else:
    sForce = ""

scriptname = sys.argv[1]
scriptfullpath = os.path.abspath(scriptname)

chmodcmd = "chmod +x " + "\"" + scriptfullpath  + "\""
retval1 = os.system(chmodcmd)

scriptfilename = os.path.split(scriptfullpath)[1]
scriptname = os.path.splitext(scriptfilename)[0]

lncmd = "ln " + sForce + " -s " + "\"" + scriptfullpath + "\"" + " \"/usr/local/bin/" + scriptname + "\"" 
retval2 = os.system(lncmd)
