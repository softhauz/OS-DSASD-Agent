"""
Tracker

Date: July 11, 2020
Author: Karen Urate
File: tracker.py
Description: This file demonstrates handling of user
inputs and encapsulating data into Tracker objects.

------------------------------------------------------------------
                           PROJECT DESCRIPTION
------------------------------------------------------------------
Create a knowledge-based agent that will compute and trace
the source of infection for an individual who has contracted Covid-19
disease from Location 1 to Location 6 in a span of 12-hour period on
9th of January 2019, based on fictional raw data provided.

The agent must have an ability to learn, create new models,
and find the source of infection based on built-up knowledge base.
"""

from agent import *

"""
TYPE 1: Handling user inputs for locations.
"""
input_location = "restaurant gym park 1 park 5"
places = input_location.split()
visited = []
visit = Location(0,[])

for p in places:
    try:
        visit.id = int(p)
        visited.append(visit)
        visit = Location(0,[])
    except:
        visit.quarantines.append(p)
        continue

for v in visited:
    print("Location " + str(v.id) + ": " + str(v.quarantines))

