#!/usr/bin/env python
"""
@file    runner.py
@author  Daniel Krajzewicz
@author  Michael Behrisch
@date    2007-10-25
@version $Id: runner.py 14221 2013-06-27 11:24:18Z behrisch $

This script is a test runner for the "Hello SUMO" Tutorial.

SUMO, Simulation of Urban MObility; see http://sumo.sourceforge.net/
Copyright (C) 2008-2013 DLR (http://www.dlr.de/) and contributors
All rights reserved
"""


import os,subprocess,sys,shutil
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', "tools")) # tutorial in tests
    sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..")), "tools")) # tutorial in docs
    from sumolib import checkBinary
except ImportError:    
    sys.exit("please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

netconvertBinary = checkBinary('netconvert')
sumoBinary = checkBinary('sumo')
# build/check network
retcode = subprocess.call([netconvertBinary, "-c", "data/hello.netccfg"], stdout=sys.stdout, stderr=sys.stderr)
try: shutil.copy("data/hello.net.xml", "net.net.xml")
except: print "Missing 'hello.net.xml'"
print ">> Netbuilding closed with status %s" % retcode
sys.stdout.flush()
# run simulation
retcode = subprocess.call([sumoBinary, "-c", "data/hello.sumocfg","--no-step-log"], stdout=sys.stdout, stderr=sys.stderr)
print ">> Simulation closed with status %s" % retcode
sys.stdout.flush()

