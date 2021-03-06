/****************************************************************************/
/// @file    MSTrigger.cpp
/// @author  Jakob Erdmann
/// @date    Sept 2012
/// @version $Id: MSTrigger.cpp 14425 2013-08-16 20:11:47Z behrisch $
///
// An abstract device that changes the state of the micro simulation
/****************************************************************************/
// SUMO, Simulation of Urban MObility; see http://sumo-sim.org/
// Copyright (C) 2001-2013 DLR (http://www.dlr.de/) and contributors
/****************************************************************************/
//
//   This file is part of SUMO.
//   SUMO is free software: you can redistribute it and/or modify
//   it under the terms of the GNU General Public License as published by
//   the Free Software Foundation, either version 3 of the License, or
//   (at your option) any later version.
//
/****************************************************************************/
// ===========================================================================
// included modules
// ===========================================================================
#include "MSTrigger.h"


// ===========================================================================
// static member definitions
// ===========================================================================
std::set<MSTrigger*> MSTrigger::myInstances;


// ===========================================================================
// method definitions
// ===========================================================================
MSTrigger::MSTrigger(const std::string& id) :
    Named(id) {
    myInstances.insert(this);
}


MSTrigger::~MSTrigger() {
    myInstances.erase(this);
}


void MSTrigger::cleanup() {
    while (!myInstances.empty()) {
        delete *myInstances.begin();
    }
}
